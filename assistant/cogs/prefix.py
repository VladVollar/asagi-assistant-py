from dataclasses import replace
from main import bot
from global_sets import *
import aiosqlite
from discord.ext import bridge
from config import DELETE_COMMANDS, PREFIX, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS

class prefix(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'setprefix', description='Управление префиксами бота.')
	@bridge.has_permissions(administrator = True)
	async def setprefix(self, ctx):

		cogwheel = bot.get_emoji(1028245358842744872)
		lock = bot.get_emoji(1027963072268226592)

		await ctx.trigger_typing()

		class MyView(discord.ui.View):

			conn = sqlite3.connect('voice.db')
			c = conn.cursor()

			for prefix in c.execute('SELECT prefix FROM main WHERE guildID = ?', (ctx.guild.id,)):

				@discord.ui.select(placeholder = f"Текущий префикс сервера: {prefix[0]}", options = [discord.SelectOption(label="Vanilla",description="Pick this if you like vanilla!")], disabled = True, row=0)

				@discord.ui.button(label='none', style=discord.ButtonStyle.grey, row=1, disabled=True)
				async def first_button_callback(self, button, interaction):

						if interaction.user.id == ctx.author.id:

							await interaction.response.send_message(f"Отлично! Укажи новый префикс для сервера, отправив сообщение в текущий чат.\nОбрати внимание, что длина префикса не должна превышать 2 символов.", ephemeral=True)

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

							await interaction.response.send_message(f"У тебя есть 30 секунд, чтобы указать новый префикс для сервера, отправив сообщение в текущий чат.\nОбрати внимание, что длина префикса не должна превышать 15 символов.", ephemeral=True)

							def check(m: discord.Message):  # m = discord.Message.
								return m.author.id == interaction.user.id and m.channel.id == ctx.channel.id

							#              event = on_message without on_
							msg = await bot.wait_for('message', check = check, timeout = 30.0)

							if len(msg.content) > 15:
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

				@discord.ui.button(label='Сбросить', style=discord.ButtonStyle.grey, row=1)
				async def third_button_callback(self, button, interaction):

						await ctx.trigger_typing()

						if interaction.user.id == ctx.author.id:

							await interaction.response.send_message(f"Префикс был успешно сброшен на начальный.", ephemeral=True)

							async with aiosqlite.connect('voice.db') as db:
								async with db.cursor() as cursor:
									await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (ctx.guild.id,))
									data = await cursor.fetchone()
									if data:
										await cursor.execute('UPDATE main SET prefix = ? WHERE guildID = ? ', ('a!', ctx.guild.id,))
									else:
										await cursor.execute('INSERT INTO main (prefix, guildID) VALUES (?, ?)', ('a!', ctx.guild.id,))
										await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (ctx.guild.id,))
										data = await cursor.fetchone()
										if data:
											await cursor.execute('UPDATE main SET prefix = ? WHERE guildID = ? ', ('a!', ctx.guild.id,))
										else:
											return
								await db.commit()

						else:

							emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
							emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

							return await interaction.response.send_message(embed=emb, ephemeral=True)

		view = MyView(timeout=None)
		await ctx.respond('**Настройка префикса**\nПозволяет настроить префикс сервера, на который бот будет отвечать при вызове команд.\n\n P.S. Если ты забудешь префикс, просто упомяни бота.', view=view)

def setup(bot):
	bot.add_cog(prefix(bot))