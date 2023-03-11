import aiosqlite
from main import bot
from global_sets import *
from config import ERROR_EMOJI
from easy_pil import *
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument, MissingPermissions

class lvlsystem(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return
		author = message.author
		guild = message.guild
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys and not levelsys[0]:
					return
				await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
				xp = await cursor.fetchone()
				await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
				level = await cursor.fetchone()

				if not xp or not level:
					await cursor.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)", (0, 0, author.id, guild.id,))
					await db.commit()

				try:

					await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
					xp = await cursor.fetchone()
					await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
					level = await cursor.fetchone()

					xp = xp[0]
					level = level[0]
				except TypeError:

					await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
					xp = await cursor.fetchone()
					await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
					level = await cursor.fetchone()

					xp = xp[0]
					level = level[0]

				if level < 5:
					xp += random.randint(1, 3)
					await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id,))
				else:
					rand = random.randint(1, (level//4))
					if rand == 1:
						xp += random.randint(1, 3)
						await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id,))
				if xp >= 100:
					level += 1
					await cursor.execute("SELECT role FROM levelSettings WHERE levelReq = ? AND guild = ?", (level, guild.id))
					role = await cursor.fetchone()
					await cursor.execute("UPDATE levels SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id,))
					await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id,))
					if role:
						role = role[0]
						role = guild.get_role(role)
						try:
							await author.add_roles(role)
							await message.channel.send(f"{author.mention} повышает свой уровень и получает роль **{role.name}**!\nТекущий уровень: **{level}**!")
						except discord.HTTPException:
							await message.channel.send(f"{author.mention} повышает свой уровень и получает роль **{role.name}**!\nТекущий уровень: **{level}**! (невозможно выдать роль)")
					await message.channel.send(f"{author.mention} повышает свой уровень!\nТекущий уровень: **{level}**!")
			await db.commit()

	@bridge.bridge_command(name = 'rank', description='Уровень и опыт участника.')
	async def _rank(self, ctx, member: discord.Member = None):
		if member is None:
			member = ctx.author
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys and not levelsys[0]:
					return await ctx.respond("Система уровней отключена Администрацией сервера.")
				await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id,))
				xp = await cursor.fetchone()
				await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id,))
				level = await cursor.fetchone()

				if not xp or not level:
					await cursor.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)", (0, 0, member.id, ctx.guild.id,))

				try:
					xp = xp[0]
					level = level[0]
				except TypeError:
					xp = 0
					level = 0

				user_data = {
					"name": f"{member.name}",
					"xp": xp,
					"level": level,
					"next_level_up": 100,
					"percentage": xp,
				}

				background = Editor("images/levelcard.png")
				profile_picture = await load_image_async(str(member.display_avatar))
				profile = Editor(profile_picture).resize((190, 190)).rounded_corners(radius = 40, offset = 2)
				nunitoregular = Font("fonts/Nunito-Regular.ttf", size=35)
				nunitoregularsmall = Font("fonts/Nunito-Regular.ttf", size=30)
				nunitobold = Font("fonts/Nunito-Bold.ttf", size=35)

				background.paste(profile, (60, 50))
				background.rectangle((330, 125), width=530, height=40, fill="#484b4e", radius=15)
				background.bar(
					(330, 125),
					max_width=530,
					height=40,
					percentage=user_data["percentage"],
					fill="#ffcb81",
					radius=15,
				)
				background.text((330, 30), user_data["name"], font=nunitobold, color="#ffcb81")
				background.text(
					(862, 180),
					f"{user_data['xp']} / {user_data['next_level_up']} ДО СЛЕДУЮЩЕГО УРОВНЯ",
					font=nunitoregularsmall,
					color="#ffcb81",
					align="right",
				)

				background.text(
					(860, 30),
					f"#{user_data['level']}",
					font=nunitobold,
					color="#ffcb81",
					align="right",
				)

				background.show()

				file = discord.File(fp=background.image_bytes, filename="levelcard.png")
				await ctx.respond(file=file)

	@bridge.bridge_command(name = 'levels', description='Включить/Отключить систему уровней.')
	@bridge.has_permissions(administrator = True)
	async def _levels(self, ctx, enabledisable):

		if enabledisable == "enable":
			async with aiosqlite.connect('voice.db') as db:
				async with db.cursor() as cursor:
					await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
					levelsys = await cursor.fetchone()
					if levelsys:
						if levelsys[0]:
							return await ctx.respond('Система уровней уже включена!')
						await cursor.execute("UPDATE levelSettings SET levelsys = ? WHERE guild = ?", (True, ctx.guild.id,))
					else:
						await cursor.execute("INSERT INTO levelSettings VALUES (?, ?, ?, ?)", (True, 0, 0, ctx.guild.id,))
					await ctx.respond('Система уровней теперь включена!')
				await db.commit()

		if enabledisable == "disable":
			async with aiosqlite.connect('voice.db') as db:
				async with db.cursor() as cursor:
					await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
					levelsys = await cursor.fetchone()
					if levelsys:
						if not levelsys[0]:
							return await ctx.respond('Система уровней уже выключена!')
						await cursor.execute("UPDATE levelSettings SET levelsys = ? WHERE guild = ?", (False, ctx.guild.id,))
					else:
						await cursor.execute("INSERT INTO levelSettings VALUES (?, ?, ?, ?)", (False, 0, 0, ctx.guild.id,))
					await ctx.respond('Система уровней теперь выключена!')
				await db.commit()

	@bridge.bridge_command(name = 'rewards', description='Какие роли доступны на определённом уровне.')
	async def _rewards(self, ctx):
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys:
					if not levelsys[0] == 1:
						return await ctx.respond("Система уровней отключена Администрацией сервера.")
				await cursor.execute("SELECT * FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
				roleLevels = await cursor.fetchall()
				if not roleLevels:
					emb = discord.Embed(title="🏅 Награды за достижение уровней", description="На данном сервере не установлены роли, которые можно получить при достижении определенного уровня.", color=EMBED_COLOUR_SUCCESS)
					return await ctx.respond(embed=emb)
				emb = discord.Embed(title="🏅 Награды за достижение уровней", description="Список наград (ролей), которые можно получить при достижении определенного уровня.", color=EMBED_COLOUR_SUCCESS)
				for role in roleLevels:
					emb.add_field(name=f"Уровень {role[2]}", value=f"<@&{role[1]}>", inline=False)
				await ctx.respond(embed=emb)

	@bridge.bridge_command(name = 'setrole', description='Добавить получение роли на уровне.')
	@bridge.has_permissions(administrator = True)
	async def _setrole(self, ctx, level: int, *, role: discord.Role):
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:	
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys:
					if not levelsys[0] == 1:
						return await ctx.respond("Система уровней отключена Администрацией сервера.")
				await cursor.execute("SELECT role FROM levelSettings WHERE role = ? AND guild = ?", (role.id, ctx.guild.id,))
				roleTF = await cursor.fetchone()
				await cursor.execute("SELECT role FROM levelSettings WHERE levelreq = ? AND guild = ?", (level, ctx.guild.id,))
				levelTF = await cursor.fetchone()
				if roleTF or levelTF:
					return await ctx.respond("Уже существует награда (роль) для этого уровня.")
				await cursor.execute("INSERT INTO levelSettings VALUES (?, ?, ?, ?)", (True, role.id, level, ctx.guild.id,))
				await db.commit()
			await ctx.respond('Обновлены награды (роли) для уровней.')

	@bridge.bridge_command(name = 'removerole', description='Убрать получение роли на уровне.')
	@bridge.has_permissions(administrator = True)
	async def _removerole(self, ctx, level: int, *, role: discord.Role):
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:	
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild = ?", (ctx.guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys:
					if not levelsys[0] == 1:
						return await ctx.respond("Система уровней отключена Администрацией сервера.")
				await cursor.execute("DELETE FROM levelSettings WHERE levelsys = ? AND role = ? AND levelreq = ? AND guild = ?", (True, role.id, level, ctx.guild.id,))
				await db.commit()
			await ctx.respond('Обновлены награды (роли) для уровней.')

	@bridge.bridge_command(name = 'leaders', description='Топ рейтинга участников.')
	async def _leaders(self, ctx):
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute("SELECT levelsys FROM levelSettings WHERE guild - ?", (ctx.guild.id,))
				levelsys = await cursor.fetchone()
				if levelsys:
					if not levelsys[0] == 1:
						return await ctx.respond("Система уровней отключена Администрацией сервера.")
				await cursor.execute("SELECT level, xp, user FROM levels WHERE guild = ? ORDER BY level DESC, xp DESC LIMIT 10", (ctx.guild.id,))
				data = await cursor.fetchall()
				if data:
					emb = discord.Embed(title="🏆 Топ рейтинга участников", color=EMBED_COLOUR_SUCCESS)
					count = 0
					for table in data:
						count += 1
						user = ctx.guild.get_member(table[2])
						emb.add_field(name=f"#{count}. {user.name}", value=f"**Уровень**: {table[0]} | **Опыт**: {table[1]}", inline=False)
					return await ctx.respond(embed=emb)
				emb = discord.Embed(title="🏆 Топ рейтинга участников", description="Не обнаружено участников, испольщующих систему уровней. Невозможно сформировать таблицу.", color=EMBED_COLOUR_SUCCESS)
				return await ctx.respond(embed=emb)

	@_levels.error
	async def levels_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`levels disable`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`levels enable`', inline = True)
			await ctx.respond(embed = emb)

	@_setrole.error
	async def setrole_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`setrole [уровень] [@роль]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`setrole 1 @Новичок`', inline = True)
			await ctx.respond(embed = emb)

	@_setrole.error
	async def removerole_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`removerole [уровень] [@роль]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`removerole 1 @Новичок`', inline = True)
			await ctx.respond(embed = emb)

def setup(bot):
	bot.add_cog(lvlsystem(bot))