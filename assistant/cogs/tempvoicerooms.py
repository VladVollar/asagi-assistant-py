from dataclasses import replace
from discord.ext import bridge
from main import bot
from global_sets import *
from config import DELETE_COMMANDS, PREFIX, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS

class tempvoicerooms(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	# Запрет заходить в голосовой канал человеку с роью бана
	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):

		cogwheel = bot.get_emoji(1028245358842744872)
		lock = bot.get_emoji(1027963072268226592)
		unlock = bot.get_emoji(1027964989052563486)
		pencil = bot.get_emoji(1027967103371845642)
		people = bot.get_emoji(1027968530919981127)
		crown = bot.get_emoji(1027969189878698065)
		downward = bot.get_emoji(1027973195988471908)
		upward = bot.get_emoji(1027973197624254535)
		bin = bot.get_emoji(1027970672581951498)
		question = bot.get_emoji(1027971290927214713)
		hiddeneye = bot.get_emoji(1031257736077381773)
		vieweye = bot.get_emoji(1031257734605197363)

		class LimUsersModal(discord.ui.Modal): #button 3
			def __init__(self, title: str) -> None:
				item = discord.ui.InputText(label="От 0 до 99:")
				super().__init__(item, title=title)

			async def callback(self, interaction: discord.Interaction):
				conn = sqlite3.connect('voice.db')
				c = conn.cursor()
				id = interaction.user.id
				c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
				voice=c.fetchone()
				channelID = voice[0]
				channel = bot.get_channel(channelID)
				await channel.edit(user_limit = self.children[0].value)
				c.execute("SELECT channelName FROM userSettings WHERE userID = ?", (id,))
				voice=c.fetchone()
				if voice is None:
					c.execute("INSERT INTO userSettings VALUES (?, ?, ?)", (id,f'{interaction.user}',self.children[0].value))
				else:
					c.execute("UPDATE userSettings SET channelLimit = ? WHERE userID = ?", (self.children[0].value, id))
					conn.commit()
				await interaction.response.send_message(f'{people} **|** **{interaction.user.name}**, изменен лимит участников на '+ '{}.'.format(self.children[0].value), delete_after=5)

		class NameModal(discord.ui.Modal): #button 4
			def __init__(self, title: str) -> None:
				item = discord.ui.InputText(label="Текст:")
				super().__init__(item, title=title)

			async def callback(self, interaction: discord.Interaction):
				conn = sqlite3.connect('voice.db')
				c = conn.cursor()
				id = interaction.user.id
				c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
				voice=c.fetchone()
				channelID = voice[0]
				channel = bot.get_channel(channelID)
				await channel.edit(name = self.children[0].value)
				c.execute("SELECT channelName FROM userSettings WHERE userID = ?", (id,))
				voice=c.fetchone()
				if voice is None:
					c.execute("INSERT INTO userSettings VALUES (?, ?, ?)", (id,self.children[0].value,0))
				else:
					c.execute("UPDATE userSettings SET channelName = ? WHERE userID = ?", (self.children[0].value, id))
					conn.commit()
				await interaction.response.send_message(f'{pencil} **|** **{interaction.user.name}**, название комнаты изменено на '+ '**{}**.'.format(self.children[0].value), delete_after=5)

		class DownWardModal(discord.ui.Modal): #button 5
			def __init__(self, title: str) -> None:
				item = discord.ui.InputText(label="ID:")
				super().__init__(item, title=title)

			async def callback(self, interaction: discord.Interaction):
				conn = sqlite3.connect('voice.db')
				c = conn.cursor()
				id = interaction.user.id
				c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
				voice=c.fetchone()
				channelID = voice[0]
				channel = bot.get_channel(channelID)
				userid = int(self.children[0].value)
				user = await interaction.guild.fetch_member(userid)
				await channel.set_permissions(user, connect=True)
				await interaction.response.send_message(f'{downward}  **|** Предоставлен доступ к комнате пользователю **{user.name}**.', delete_after=5)

		class UpWardModal(discord.ui.Modal): #button 6
			def __init__(self, title: str) -> None:
				item = discord.ui.InputText(label="ID:")
				super().__init__(item, title=title)

			async def callback(self, interaction: discord.Interaction):
				conn = sqlite3.connect('voice.db')
				c = conn.cursor()
				id = interaction.user.id
				c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
				voice=c.fetchone()
				channelID = voice[0]
				channel = bot.get_channel(channelID)
				userid = int(self.children[0].value)
				user = await interaction.guild.fetch_member(userid)
				await channel.set_permissions(user, connect=False)
				await interaction.response.send_message(f'{upward}  **|** Забран доступ к комнате у пользователя **{user.name}**.', delete_after=5)

		class MyView(discord.ui.View):
			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{lock}", row=0)
			async def first_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()
					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)

					else:
						channelID = voice[0]
						c.execute("UPDATE voiceChannel SET locked = TRUE WHERE userID = ?", (id,))
						role = discord.utils.get(interaction.guild.roles, name='@everyone')
						channel = interaction.guild.get_channel(channelID)
						await channel.set_permissions(role, connect=False, read_messages=True)
						await interaction.response.send_message(f"{lock} **|** Приватная комната закрыта.", ephemeral=True)
					conn.commit()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{unlock}", row=0)
			async def second_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()
					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)

					else:
						channelID = voice[0]
						c.execute("UPDATE voiceChannel SET locked = TRUE WHERE userID = ?", (id,))
						role = discord.utils.get(interaction.guild.roles, name='@everyone')
						channel = interaction.guild.get_channel(channelID)
						await channel.set_permissions(role, connect=True, read_messages=True)
						await interaction.response.send_message(f"{unlock} **|** Приватная комната открыта.", ephemeral=True)
					conn.commit()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{people}", row=0)
			async def third_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()

					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)
					
					if voice:

							modal = LimUsersModal("Лимит пользователей")
							await interaction.response.send_modal(modal)
							await modal.wait()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{pencil}", row=0)
			async def fourth_button_callback(self, button, interaction):
	
					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()

					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)
					
					if voice:

							modal = NameModal("Название комнаты")
							await interaction.response.send_modal(modal)
							await modal.wait()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{crown}", row=0)
			async def tenth_button_callback(self, button, interaction):

				error = bot.get_emoji(1013499170356723853)
				x = False
				conn = sqlite3.connect('voice.db')
				c = conn.cursor()
				channel = interaction.user.voice

				if channel == None:

					emb = discord.Embed(description = f'**{interaction.user.name}**, необходимо находиться в приватной комнате.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

				if channel:
					id = interaction.user.id
					c.execute("SELECT userID FROM voiceChannel WHERE voiceID = ?", (channel.channel.id,))
					voice=c.fetchone()
					if voice is None:
						await interaction.response.send_message(f'{crown} **|** Ты не можешь владеть этой комнатой.', ephemeral=True)
					else:
						for data in channel.channel.members:
							if data.id == voice[0]:
								owner = interaction.guild.get_member(voice [0])
								await interaction.response.send_message(f'{crown} **|** Эта комната уже принадлежит **{owner.name}**.', ephemeral=True)
								x = True
						if x == False:
							await interaction.response.send_message(f'{crown} **|** Ты стал новым владельцем комнаты.', ephemeral=True)
							c.execute("UPDATE voiceChannel SET userID = ? WHERE voiceID = ?", (id, channel.channel.id))
					conn.commit()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{downward}", row=1)
			async def fifth_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()

					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						return await interaction.response.send_message(embed=emb, ephemeral=True)
					
					if voice:
							modal = DownWardModal("Выдача доступа")
							await interaction.response.send_modal(modal)
							await modal.wait()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{upward}", row=1)
			async def sixth_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()

					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						return await interaction.response.send_message(embed=emb, ephemeral=True)
					
					if voice:
							modal = UpWardModal("Забрать доступ")
							await interaction.response.send_modal(modal)
							await modal.wait()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{bin}", row=1)
			async def seventh_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()

					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						return await interaction.response.send_message(embed=emb, ephemeral=True)
					
					if voice:
						channelID = voice[0]
						channel = bot.get_channel(channelID)
						if channel is not None:
							await channel.delete()
							c.execute('DELETE FROM voiceChannel WHERE userID=?', (id,))
							await interaction.response.send_message(f'{bin} **|** Комната удалена.', ephemeral=True)
					conn.commit()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{hiddeneye}", row=1)
			async def eighth_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()
					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)

					else:
						channelID = voice[0]
						c.execute("UPDATE voiceChannel SET locked = TRUE WHERE userID = ?", (id,))
						role = discord.utils.get(interaction.guild.roles, name='@everyone')
						channel = interaction.guild.get_channel(channelID)
						if channel is not None:
							await channel.set_permissions(role, view_channel=False)
							await interaction.response.send_message(f"{hiddeneye} **|** Приватная комната скрыта.", ephemeral=True)
					conn.commit()

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f"{vieweye}", row=1)
			async def ninth_button_callback(self, button, interaction):

					error = bot.get_emoji(1013499170356723853)
					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					id = interaction.user.id
					c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
					voice=c.fetchone()
					if voice is None:

						emb = discord.Embed(description = f'**{interaction.user.name}**, для управления необходимо находиться в своей комнате.', color=EMBED_COLOUR_SUCCESS)
						emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

						await interaction.response.send_message(embed=emb, ephemeral=True)

					else:
						channelID = voice[0]
						c.execute("UPDATE voiceChannel SET locked = TRUE WHERE userID = ?", (id,))
						role = discord.utils.get(interaction.guild.roles, name='@everyone')
						channel = interaction.guild.get_channel(channelID)
						if channel is not None:
							await channel.set_permissions(role, view_channel=True)
							await interaction.response.send_message(f"{vieweye} **|** Приватная комната показана.", ephemeral=True)
					conn.commit()

		info =  discord.Embed(description = f'Ты можешь изменить конфигурацию своей комнаты с помощью взаимодействий.\n\n {lock} **—** закрыть комнату\n {unlock} **—** открыть комнату\n {people} **—** задать новый лимит участников\n {pencil} **—** изменить название комнаты\n {crown} **—** получить права владельца комнаты\n {downward} **—** выдать доступ к комнате\n {upward} **—** ограничить доступ к комнате\n {bin} **—** удалить комнату\n {hiddeneye} **—** скрыть комнату\n {vieweye} **—** показать комнату', colour=EMBED_COLOUR_SUCCESS)
		info.set_author(name='Управление приватными комнатами', icon_url='https://i.imgur.com/jJqa7OQ.png')

		view = MyView(timeout=None)
	
		channel = before.channel or after.channel

		conn = sqlite3.connect('voice.db')
		c = conn.cursor()
		guildID = member.guild.id
		c.execute("SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
		voice=c.fetchone()
		if voice is None:
			pass
		else:
			voiceID = voice[0]
			try:
				if after.channel.id == voiceID:
					c.execute("SELECT * FROM voiceChannel WHERE userID = ?", (member.id,))
					cooldown=c.fetchone()
					if cooldown is None:
						pass
					c.execute("SELECT voiceCategoryID FROM guild WHERE guildID = ?", (guildID,))
					voice=c.fetchone()
					c.execute("SELECT channelName, channelLimit FROM userSettings WHERE userID = ?", (member.id,))
					setting=c.fetchone()
					c.execute("SELECT channelLimit FROM guildSettings WHERE guildID = ?", (guildID,))
					guildSetting=c.fetchone()
					if setting is None:
						name = f"🍪 Комната {member.name}"
						if guildSetting is None:
							limit = 0
						else:
							limit = guildSetting[0]
					else:
						if guildSetting is None:
							name = setting[0]
							limit = setting[1]
						elif guildSetting is not None and setting[1] == 0:
							name = setting[0]
							limit = guildSetting[0]
						else:
							name = setting[0]
							limit = setting[1]
					categoryID = voice[0]
					id = member.id
					category = bot.get_channel(categoryID)
					channel2 = await member.guild.create_voice_channel(name,category=category)
					channelID = channel2.id
					await member.move_to(channel2)
					await channel2.send(embed=info, view=view)
					await channel2.set_permissions(bot.user, connect=True,read_messages=True)
					await channel2.edit(name= name, user_limit = limit)
					c.execute("INSERT INTO voiceChannel VALUES (?, ?, FALSE)", (id,channelID))
					conn.commit()
					def check(x,y,z):
						return len(channel2.members) == 0
					await bot.wait_for('voice_state_update', check=check)
					await channel2.delete()
					await asyncio.sleep(3)
					c.execute('DELETE FROM voiceChannel WHERE userID=?', (id,))
			except:
				pass
		conn.commit()

	@bridge.bridge_command(name = 'setvoice', description='Управление приватными комнатами.')
	@bridge.has_permissions(administrator = True)
	async def _setvoice(self, ctx):

		await ctx.trigger_typing()

		class View(discord.ui.View):

			@discord.ui.button(label='Установить', style=discord.ButtonStyle.grey, row=1)
			async def first_button_callback(self, button, interaction):

				await ctx.trigger_typing()

				if interaction.user.id == ctx.author.id:

					conn = sqlite3.connect('voice.db')
					c = conn.cursor()
					guildID = ctx.guild.id
					id = ctx.author.id
					cogwheel = bot.get_emoji(1028245358842744872)

					new_cat = await ctx.guild.create_category_channel('Приватные комнаты')
					channel = await ctx.guild.create_voice_channel('Создать [+]', category=new_cat)
					await channel.edit(user_limit = 1)
					c.execute("SELECT * FROM guild WHERE guildID = ? AND ownerID=?", (guildID, id))
					voice=c.fetchone()
					if voice is None:
						c.execute ("INSERT INTO guild VALUES (?, ?, ?, ?)",(guildID,id,channel.id,new_cat.id))
					else:
						c.execute ("UPDATE guild SET guildID = ?, ownerID = ?, voiceChannelID = ?, voiceCategoryID = ? WHERE guildID = ?",(guildID,id,channel.id,new_cat.id, guildID))
					conn.commit()

					await interaction.response.send_message(f"Приватные комнаты установлены и готовы к использованию!", ephemeral=True)

				else:

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(label='Панель управления', style=discord.ButtonStyle.grey, row=1)
			async def second_button_callback(self, button, interaction):

				await ctx.trigger_typing()

				if interaction.user.id == ctx.author.id:

					await interaction.response.send_message(f'Панель управления приватной комнатой находиться в самой комнате (текстовый чат голосового чата).', ephemeral=True)

				else:

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

		view = View(timeout=None)
			
		await ctx.respond(f'**Приватные голосовые комнаты**\nЭто временные комнаты, которые создаются при входе в определённый канал и удаляются, если в них нет участников.\nУправление приватной комнатой доступно лишь через панель управления.', view=view)

def setup(bot):
	bot.add_cog(tempvoicerooms(bot))