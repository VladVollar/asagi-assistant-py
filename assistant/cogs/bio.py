import aiosqlite
from main import bot
from global_sets import *
from config import ERROR_EMOJI
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument, MissingPermissions

class bio(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'resetbio', description='Удалить биографию участнику.')
	@bridge.has_permissions(administrator = True)
	async def _resetbio(self, ctx, member: discord.Member, *, reason = "Не указана."):
		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if member.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя удалить биографию боту!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя удалить биографию владельцу сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя удалить свою биографию! (setbio)', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < member.top_role or ctx.author.top_role == member.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя удалить биографию участника, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			async with aiosqlite.connect('voice.db') as db:
				async with db.cursor() as cursor:

					await cursor.execute('SELECT bio FROM bio WHERE userID = ?', (member.id,))
					data = await cursor.fetchone()

					if data:
						await cursor.execute('DELETE from bio WHERE userID = ? AND guildID = ?', (member.id, ctx.guild.id,))
						punish_start_time = ctx.message.created_at.timestamp()

						emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) удалил биографию **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Биографии', icon_url='https://i.imgur.com/6xgTS17.png')
						emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
						emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

						emb_member = discord.Embed(description=f'Твою биографию удалил модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сервера **{ctx.guild.name}**.', colour=EMBED_COLOUR_SUCCESS)
						emb_member.set_author(name='Биографии', icon_url='https://i.imgur.com/6xgTS17.png')
						emb_member.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
						emb_member.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

						await ctx.respond(embed=emb)
						await member.send(embed = emb_member)

					else:

						await cursor.execute('INSERT INTO bio (bio, userID, guildID) VALUES (?, ?, ?)', ('a', member.id, ctx.guild.id,))
						await cursor.execute('SELECT bio FROM bio WHERE userID = ? AND guildID = ?', (member.id, ctx.guild.id,))
						data = await cursor.fetchone()

						if data:
							await cursor.execute('DELETE from bio WHERE userID = ? AND guildID = ?', (member.id, ctx.guild.id,))
							now = datetime.now()
							punish_start_time = now.timestamp()

							emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) удалил биографию **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
							emb.set_author(name='Биографии', icon_url='https://i.imgur.com/6xgTS17.png')
							emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
							emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

							emb_member = discord.Embed(description=f'Твою биографию удалил модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сервера **{ctx.guild.name}**.', colour=EMBED_COLOUR_SUCCESS)
							emb_member.set_author(name='Биографии', icon_url='https://i.imgur.com/6xgTS17.png')
							emb_member.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
							emb_member.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

							await ctx.respond(embed=emb)
							await member.send(embed = emb_member)

						else:

							return
				await db.commit()

	@_resetbio.error
	async def resetbio_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.send(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`resetbio [@участник] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`resetbio @vollar#0074 пример`', inline = True)
			await ctx.send(embed = emb)

	@bridge.bridge_command(name = 'bio', description='Биография участника.')
	async def _bio(self, ctx, member: discord.Member = None):

		await ctx.trigger_typing()

		if member == None:  # если не упоминать участника тогда выводит аватар автора сообщения
			member = ctx.author

		conn = sqlite3.connect('voice.db')
		c = conn.cursor()
		checkbio = c.execute(f"SELECT bio FROM bio where userID={member.id} AND guildID={ctx.guild.id}")

		if checkbio.fetchone() is None:
				embed = discord.Embed(title=f'Биография {member.display_name}',description=f'Сейчас тут пусто, но ты можешь написать сюда что-нибудь, при помощи команды `setbio`', colour=EMBED_COLOUR_SUCCESS)
				embed.set_thumbnail(url=member.avatar.with_size(128))
				await ctx.respond(embed=embed)
		else:

			for row in c.execute(f"SELECT bio FROM bio where userID={member.id} AND guildID={ctx.guild.id}"):
				embed = discord.Embed(title=f'Биография {member.display_name}',description=f'{row[0]}', colour=EMBED_COLOUR_SUCCESS)
				embed.set_thumbnail(url=member.avatar.with_size(128))
				await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'setbio', description='Установить биографию.')
	async def _setbio(self,ctx):

		await ctx.trigger_typing()

		class View(discord.ui.View):

			@discord.ui.select(placeholder = f"Посмотреть текущую биографию: bio", options = [discord.SelectOption(label="Vanilla",description="Pick this if you like vanilla!")], disabled = True, row=0)

			@discord.ui.button(label='none', style=discord.ButtonStyle.grey, row=1, disabled=True)
			async def first_button_callback(self, button, interaction):

					await ctx.trigger_typing()

					if interaction.user.id == ctx.author.id:

						await interaction.response.send_message(f"У тебя есть 30 секунд, чтобы указать новый префикс для сервера, отправив сообщение в текущий чат.\nОбрати внимание, что длина префикса не должна превышать 2 символов.", ephemeral=True)

						def check(m: discord.Message):  # m = discord.Message.
							return m.author.id == interaction.user.id and m.channel.id == ctx.channel.id

						#              event = on_message without on_
						msg = await bot.wait_for('message', check = check, timeout = 30.0)

						if len(msg.content) > 2:
							return await ctx.send(f'**{interaction.user.name}**, превышена длина префикса, попробуй еще раз.', delete_after=5)
						else:

							async with aiosqlite.connect('voice.db') as db:
								async with db.cursor() as cursor:
									await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (ctx.guild.id,))
									data = await cursor.fetchone()
									if data:
										await cursor.execute('UPDATE main SET prefix = ? WHERE guildID = ? ', (msg.content, ctx.guild.id,))
										await ctx.send(f'**{ctx.author.name}**, префикс `{msg.content}` успешно сохранен.', delete_after=5)
									else:
										await cursor.execute('INSERT INTO main (prefix, guildID) VALUES (?, ?)', ('a!', ctx.guild.id,))
										await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (ctx.guild.id,))
										data = await cursor.fetchone()
										if data:
											await cursor.execute('UPDATE main SET prefix = ? WHERE guildID = ? ', (msg.content, ctx.guild.id,))
											await ctx.send(f'**{ctx.author.name}**, префикс `{msg.content}` успешно сохранен.', delete_after=5)
										else:
											return
								await db.commit()

					else:

						emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(label='Изменить', style=discord.ButtonStyle.grey, row=1)
			async def second_button_callback(self, button, interaction):

				await ctx.trigger_typing()

				if interaction.user.id == ctx.author.id:

					await interaction.response.send_message(f"У тебя есть 30 секунд, чтобы указать новую биографию, отправив сообщение в текущий чат.\nОбрати внимание, что длина биографии не должна превышать 180 символов.", ephemeral=True)

					def check(m: discord.Message):  # m = discord.Message.
						return m.author.id == interaction.user.id and m.channel.id == ctx.channel.id

					#              event = on_message without on_
					msg = await bot.wait_for('message', check = check, timeout = 30.0)

					if len(msg.content) > 180:
						return await ctx.send(f'**{interaction.user.name}**, превышена длина биографии, попробуй еще раз.', delete_after=5)
					else:

						async with aiosqlite.connect('voice.db') as db: # установить биографию
							async with db.cursor() as cursor:
								await cursor.execute('SELECT bio FROM bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))
								data = await cursor.fetchone()
								if data:
									await cursor.execute('UPDATE bio SET bio = ? WHERE userID = ? AND guildID = ? ', (msg.content, ctx.author.id, ctx.guild.id,))
									await ctx.send(f'**{ctx.author.name}**, биография успешно сохранена.', delete_after=5)
								else:
									await cursor.execute('INSERT INTO bio (bio, userID, guildID) VALUES (?, ?, ?)', ('a', ctx.author.id, ctx.guild.id,))
									await cursor.execute('SELECT bio FROM bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))
									data = await cursor.fetchone()
									if data:
										await cursor.execute('UPDATE bio SET bio = ? WHERE userID = ? AND guildID = ? ', (msg.content, ctx.author.id, ctx.guild.id,))
										await ctx.send(f'**{ctx.author.name}**, биография успешно сохранена.', delete_after=5)
									else:
										return
							await db.commit()

				else:

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(label='Очистить', style=discord.ButtonStyle.grey, row=1)
			async def third_button_callback(self, button, interaction):

				await ctx.trigger_typing()

				if interaction.user.id == ctx.author.id:

					await interaction.response.send_message(f"Биография была успешно очищена.", ephemeral=True)

					async with aiosqlite.connect('voice.db') as db:
						async with db.cursor() as cursor:

							await cursor.execute('SELECT bio FROM bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))
							data = await cursor.fetchone()

							if data:
								await cursor.execute('DELETE from bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))

							else:

								await cursor.execute('INSERT INTO bio (bio, userID, guildID) VALUES (?, ?, ?)', ('a', ctx.author.id, ctx.guild.id,))
								await cursor.execute('SELECT bio FROM bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))
								data = await cursor.fetchone()

								if data:
									await cursor.execute('DELETE from bio WHERE userID = ? AND guildID = ?', (ctx.author.id, ctx.guild.id,))

								else:

									return
						await db.commit()

				else:

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

		view = View(timeout=None)
			
		await ctx.respond(f'**Настройка биографии**\nПозволяет изменить биографию, которая будет отображаться в `bio` и `userinfo`.', view=view)

def setup(bot):
	bot.add_cog(bio(bot))