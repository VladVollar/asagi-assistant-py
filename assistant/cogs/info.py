import time
import psutil
from unicodedata import category
from main import bot
from global_sets import *
from easy_pil import *
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument
from discord.ui import Button, View
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS

class info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_ready(self):
			global startTime
			startTime = time.time()

	@bridge.bridge_command(name = 'info', description='Информация о боте.')
	async def _info(self, ctx):

			await ctx.trigger_typing()

			time_1 = time.perf_counter()
			await ctx.trigger_typing()
			time_2 = time.perf_counter()
			latency = round((time_2-time_1)*1000)

			current_time = time.time()
			difference = int(round(current_time - startTime))

			seconds = difference % (24 * 3600)
			hour = seconds // 3600
			seconds %= 3600
			minutes = seconds // 60
			seconds %= 60

			emb = discord.Embed(description=f'Информация о **{bot.user.name}**:', colour=EMBED_COLOUR_SUCCESS)

			ping = bot.get_emoji(1034402414624768000)
			servers = bot.get_emoji(1034516446140715088)
			users = bot.get_emoji(1027968530919981127)
			cpu = bot.get_emoji(1034517244778123284)
			ram = bot.get_emoji(1034517747708743840)
			uptime = bot.get_emoji(1034518283535253574)
			monitorings = bot.get_emoji(1034519066565689407)
			topgg = bot.get_emoji(1034521076639739965)
			infinitybotsgg = bot.get_emoji(1034555161135284244)
			botlistme = bot.get_emoji(1035243278318190664)
			discordbotlistcom = bot.get_emoji(1036654825401749514)
			disforgecom = bot.get_emoji(1036655001948405870)

			fields = [
					(f"{ping} Задержка (API)", f'```python\n{latency // 10:.0f}мс```', True),
					(f"{servers} Серверов", f'```python\n{len(self.bot.guilds)}```', True),
					(f"{users} Пользователей", f'```python\n{len(set(self.bot.get_all_members()))}```', True),
					(f"{cpu} ЦП", f'```python\n{psutil.cpu_percent()}%```', True),
					(f"{ram} ОЗУ", f'```python\n{psutil.virtual_memory().percent}%```', True),
					(f"{uptime} Время работы", f'```python\n%02dч %02dм %02dс```' % (hour, minutes, seconds), True),
					(f"{monitorings} Мониторинги:", f'— {topgg} Top.gg\n — {infinitybotsgg} Infinitybots.gg\n — {botlistme} Botlist.me\n — {discordbotlistcom} Discordbotlist.com\n — {disforgecom} Disforge.com', True)
					]

			for name, value, inline in fields:
				emb.add_field(name=name, value=value, inline=inline)
				emb.set_thumbnail(url=bot.user.display_avatar.with_size(128))

			button1 = Button(emoji=f"{topgg}", url="https://top.gg/bot/1006168648622288936", row=0)
			button2 = Button(emoji=f"{infinitybotsgg}", url="https://infinitybots.gg/bots/1006168648622288936", row=0)
			button3 = Button(emoji=f"{botlistme}", url="https://botlist.me/bots/1006168648622288936", row=0)
			button4 = Button(emoji=f"{discordbotlistcom}", url="https://discordbotlist.com/bots/asagi-assistant", row=0)
			button5 = Button(emoji=f"{disforgecom}", url="https://disforge.com/bot/2758-asagi-assistant", row=0)
			view = View()
			view.add_item(button1)
			view.add_item(button2)
			view.add_item(button3)
			view.add_item(button4)
			view.add_item(button5)

			await ctx.respond(embed=emb, view=view)

	@bridge.bridge_command(name="userinfo", description='Информация об участнике.')
	async def _userinfo(self, ctx, member: discord.Member = None):

			await ctx.trigger_typing()

			if member == None:  # если не упоминать участника тогда выводит аватар автора сообщения
				member = ctx.author

			online = bot.get_emoji(1019871972139741194)
			idle = bot.get_emoji(1019872278474924042)
			dnd = bot.get_emoji(1019872276855935026)
			offline = bot.get_emoji(1019872275434049556)

			t = member.status
			if t == discord.Status.online:
				d = f"{online} В сети"

			t = member.status
			if t == discord.Status.idle:
				d = f"{idle} Не активен"

			t = member.status
			if t == discord.Status.dnd:
				d = f"{dnd} Не беспокоить"

			t = member.status
			if t == discord.Status.offline:
				d = f"{offline} Не в сети"

			datejoin = member.joined_at.timestamp()
			datecreated = member.created_at.timestamp()

			roles = member.roles
			role_list = ""
			for role in roles:
				role_list += f"<@&{role.id}> "
			readylist = role_list[23:]

			voice_state = "Нет." if not member.voice else member.voice.channel

			conn = sqlite3.connect('voice.db')
			c = conn.cursor()
			checkbio = c.execute(f"SELECT bio FROM bio where userID={member.id} AND guildID={ctx.guild.id}")

			if checkbio.fetchone() is None:
				embed = discord.Embed(title=f'Информация о {member.name}#{member.discriminator}', description=f'Биография отсутствует.', colour=EMBED_COLOUR_SUCCESS)
				embed.add_field(name=f'**Основная информация**', value=f"**Имя пользователя:** {member.name}#{member.discriminator} ({member.display_name})\n **Статус:** {d}\n **Присоединился:** <t:{int(datejoin)}:R>\n **Дата регистрации:** <t:{int(datecreated)}:R>\n **В голосовом канале:** {voice_state}\n  **Высшая роль:** {member.top_role.mention} \n **Роли ({format(len(member.roles)-1)}):** {readylist}")
				embed.set_footer(text = f"ID: {member.id}")
				embed.set_thumbnail(url=member.avatar.with_size(128))
				await ctx.respond(embed=embed)

			else:
				for row in c.execute(f"SELECT bio FROM bio where userID={member.id} AND guildID={ctx.guild.id}"):
					embed = discord.Embed(title=f'Информация о {member.name}#{member.discriminator}', description=f'{row[0]}', colour=EMBED_COLOUR_SUCCESS)
					embed.add_field(name=f'**Основная информация**', value=f"**Имя пользователя:** {member.name}#{member.discriminator} ({member.display_name})\n **Статус:** {d}\n **Присоединился:** <t:{int(datejoin)}:R>\n **Дата регистрации:** <t:{int(datecreated)}:R>\n **В голосовом канале:** {voice_state}\n **Высшая роль:** {member.top_role.mention} \n **Роли ({format(len(member.roles)-1)}):** {readylist}")
					embed.set_footer(text = f"ID: {member.id}")
					embed.set_thumbnail(url=member.avatar.with_size(128))
					await ctx.respond(embed=embed)

	@bridge.bridge_command(name="stats", description='Статистика пользователей.')
	async def _stats(self, ctx):

			await ctx.trigger_typing()

			statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
						len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
						len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
						len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

			background = Editor("images/statscard.png")
			nunitoregular = Font("fonts/Nunito-Regular.ttf", size=35)
			nunitoregularsmall = Font("fonts/Nunito-Regular.ttf", size=30)
			nunitoboldsmall = Font("fonts/Nunito-Bold.ttf", size=40)
			nunitobold = Font("fonts/Nunito-Bold.ttf", size=50)
			nunitoboldbig = Font("fonts/Nunito-Bold.ttf", size=70)

			background.text((235, 20), "СТАТИСТИКА", font=nunitoboldbig, color="#ffcb81")
			background.text((620, 123), f"{statuses[2]}", font=nunitobold, color="#ffcb81", align="center")
			background.text((320, 123), f"{statuses[0]}", font=nunitobold, color="#ffcb81", align="center")
			background.text((620, 176), f"{statuses[3]}", font=nunitobold, color="#ffcb81", align="center")
			background.text((320, 176), f"{statuses[1]}", font=nunitobold, color="#ffcb81", align="center")

			background.show()

			file = discord.File(fp=background.image_bytes, filename="statscard.png")
			await ctx.respond(file=file)

	@bridge.bridge_command(name="serverinfo", description='Информация о сервере.')
	async def _serverinfo(self, ctx):

			await ctx.trigger_typing()

			online = bot.get_emoji(1019871972139741194)
			idle = bot.get_emoji(1019872278474924042)
			dnd = bot.get_emoji(1019872276855935026)
			offline = bot.get_emoji(1019872275434049556)

			members_total = bot.get_emoji(1030389726965923860)
			members = bot.get_emoji(1030390993847058442)
			bots = bot.get_emoji(1030391625471508510)

			channels_total = bot.get_emoji(1030377972416393236)
			text_channel = bot.get_emoji(1030377973959901304)
			voice_channel = bot.get_emoji(1030380699062124544)
			categories = bot.get_emoji(1030377970520559677)

			t = ctx.guild.verification_level
			if t == discord.VerificationLevel.none:
				d = "Отсутствует"

			t = ctx.guild.verification_level
			if t == discord.VerificationLevel.low:
				d = "Низкий"

			t = ctx.guild.verification_level
			if t == discord.VerificationLevel.medium:
				d = "Средний"

			t = ctx.guild.verification_level
			if t == discord.VerificationLevel.high:
				d = "Высокий"

			t = ctx.guild.verification_level
			if t == discord.VerificationLevel.highest :
				d = "Очень высокий"

			datecreate = ctx.guild.created_at.timestamp()

			emb = discord.Embed(title=f'Информация о сервере {ctx.guild.name}', colour=EMBED_COLOUR_SUCCESS)

			fields = [("Каналы:", f"{channels_total} Всего: **{len(ctx.guild.text_channels + ctx.guild.voice_channels)}**\n {text_channel} Текстовых: **{len(ctx.guild.text_channels)}**\n {voice_channel} Голосовых: **{len(ctx.guild.voice_channels)}**\n {categories} Категорий: **{len(ctx.guild.categories)}**", True),
					("Участники", f"{members_total} Всего: **{len(ctx.guild.members)}**\n {members} Людей: **{len(list(filter(lambda m: not m.bot, ctx.guild.members)))}**\n {bots} Ботов: **{len(list(filter(lambda m: m.bot, ctx.guild.members)))}**", True),
					("Владелец:", ctx.guild.owner.mention, True),	
					("Дата создания:", f"<t:{int(datecreate)}:R>", True),
					("Уровень проверки:", f'{d}', True),
					("Количество ролей:", f'**{len(ctx.guild.roles)}**', True)]

			for name, value, inline in fields:
				emb.add_field(name=name, value=value, inline=inline)
				emb.set_thumbnail(url=ctx.guild.icon.url)
				emb.set_footer(text = "ID: " + str(ctx.guild.id))

			await ctx.respond(embed=emb)

	@bridge.bridge_command(name="roleinfo", description='Информация о роле.')
	async def _roleinfo(self, ctx, *, msg, guild = None):

			await ctx.trigger_typing()

			guild = ctx.guild
			guild_roles = ctx.guild.roles

			for role in guild_roles:
				if msg.lower() == role.name.lower() or msg == role.id:

					all_users = [str(x) for x in role.members]
					all_users.sort()
					all_users = ', '.join(all_users)
					datecreate = role.created_at.timestamp()
					em = discord.Embed(title='Информация о роли', description=f'**Название:** {role.name}\n **ID:** {role.id}\n **Участников с ролью:** {str(len(role.members))}\n **HEX:** {str(role.color)}\n **RGB:** {role.color.to_rgb()}\n **Создана:** <t:{int(datecreate)}:R>', color=role.color)
					em.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(str(role.color).strip("#")))
					return await ctx.respond(embed=em)

			await ctx.respond('Роль ``{}`` не найдена.'.format(msg))

	@_roleinfo.error
	async def roleinfo_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи название роли!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`roleinfo [роль]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`roleinfo {bot.user.name}`', inline = True)
			await ctx.send(embed = emb)

def setup(bot):
	bot.add_cog(info(bot))