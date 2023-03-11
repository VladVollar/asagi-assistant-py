import aiosqlite
from main import bot
from global_sets import *
from config import ERROR_EMOJI
from easy_pil import *
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument, MissingPermissions

class welcomesystem(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_member_join(self, member):

		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:

				await cursor.execute("SELECT welcomesys FROM welcomeSettings WHERE guild = ?", (member.guild.id,))
				welcomesys = await cursor.fetchone()
				if welcomesys:
					if not welcomesys[0] == 1:
						return

				await cursor.execute("SELECT channel FROM welcomeSettings WHERE guild = ?", (member.guild.id,))
				data = await cursor.fetchone()
				if data:

					channel = await bot.fetch_channel(data[0])

					background = Editor("images/welcomecard.png")
					profile_picture = await load_image_async(str(member.display_avatar))
					profile = Editor(profile_picture).resize((190, 190)).rounded_corners(radius = 40, offset = 2)
					nunitoregular = Font("fonts/Nunito-Regular.ttf", size=35)
					nunitoregularsmall = Font("fonts/Nunito-Regular.ttf", size=30)
					nunitoboldsmall = Font("fonts/Nunito-Bold.ttf", size=40)
					nunitobold = Font("fonts/Nunito-Bold.ttf", size=50)
					nunitoboldbig = Font("fonts/Nunito-Bold.ttf", size=70)

					background.paste(profile, (60, 50))
					background.text((315, 70), "ПРИВЕТСТВУЕМ", font=nunitoboldbig, color="#ffcb81")
					background.text((600, 140), f"{member.name}", font=nunitobold, color="#ffcb81", align="center")

					background.text(
						(315, 240),
						f"#{member.guild.member_count}",
						font=nunitoboldsmall,
						color="#ffcb81",
						align="right",
					)

					background.show()

					file = discord.File(fp=background.image_bytes, filename="welcomecard.png")
					await channel.send(file=file)

				else:

					return

	@bridge.bridge_command(name = 'welcome', description='Включить/Отключить приветствие.')
	@bridge.has_permissions(administrator = True)
	async def _welcome(self, ctx, enabledisable):

		if enabledisable == "enable":
			async with aiosqlite.connect('voice.db') as db:
				async with db.cursor() as cursor:
					await cursor.execute("SELECT welcomesys FROM welcomeSettings WHERE guild = ?", (ctx.guild.id,))
					welcomesys = await cursor.fetchone()
					if welcomesys:
						if welcomesys[0]:
							return await ctx.respond('Система приветствий уже включена!')
						await cursor.execute("UPDATE welcomeSettings SET welcomesys = ? WHERE guild = ?", (True, ctx.guild.id,))
					else:
						await cursor.execute("INSERT INTO welcomeSettings VALUES (?, ?, ?)", (True, 0, ctx.guild.id,))
					await ctx.respond('Система приветствий теперь включена!')
				await db.commit()

		if enabledisable == "disable":
			async with aiosqlite.connect('voice.db') as db:
				async with db.cursor() as cursor:
					await cursor.execute("SELECT welcomesys FROM welcomeSettings WHERE guild = ?", (ctx.guild.id,))
					levelsys = await cursor.fetchone()
					if levelsys:
						if not levelsys[0]:
							return await ctx.respond('Система приветствий уже выключена!')
						await cursor.execute("UPDATE welcomeSettings SET welcomesys = ? WHERE guild = ?", (False, ctx.guild.id,))
					else:
						await cursor.execute("INSERT INTO welcomeSettings VALUES (?, ?, ?)", (False, 0, ctx.guild.id,))
					await ctx.respond('Система приветствий теперь выключена!')
				await db.commit()

	@bridge.bridge_command(name = 'setwelcome', description='Выбрать канал для приветствий.')
	@bridge.has_permissions(administrator = True)
	async def _setwelcome(self, ctx, channel: discord.TextChannel):
		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:

				await cursor.execute("SELECT welcomesys FROM welcomeSettings WHERE guild = ?", (ctx.guild.id,))
				welcomesys = await cursor.fetchone()
				if welcomesys:
					if not welcomesys[0] == 1:
						return await ctx.respond('Система приветствий отключена Администрацией сервера.')

				await cursor.execute("SELECT channel FROM welcomeSettings WHERE guild = ?", (ctx.guild.id,))
				channelData = await cursor.fetchone()
				if channelData:
					channelData = channelData[0]
					if channelData == channel.id:
						return await ctx.respond(f"Канал {channel.mention} уже используется для приветствий.")
					await cursor.execute("UPDATE welcomeSettings SET channel = ? WHERE guild = ?", (channel.id, ctx.guild.id,))
					await ctx.respond(f"Канал {channel.mention} теперь используется для приветствий.")
				else:
					await cursor.execute("INSERT INTO welcomeSettings VALUES (?, ?, ?)", (True, channel.id, ctx.guild.id,))
					await ctx.respond(f"Канал {channel.mention} теперь используется для приветствий.")
			await db.commit()

	@_welcome.error
	async def welcome_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`welcome disable`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`welcome enable`', inline = True)
			await ctx.respond(embed = emb)

	@_setwelcome.error
	async def setwelcome_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`setwelcome [#канал]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`setwelcome #чат`', inline = True)
			await ctx.respond(embed = emb)

def setup(bot):
	bot.add_cog(welcomesystem(bot))