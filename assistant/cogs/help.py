from main import bot
from discord.ext import bridge
from global_sets import *
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS

class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'help', description='Помощь по командам.')
	async def help(self, ctx):

		await ctx.trigger_typing()

		docs = bot.get_emoji(1029389523685216276)
		info = bot.get_emoji(1029291627681951764)
		interactions = bot.get_emoji(1029300403151573042)
		star = bot.get_emoji(1029303284617465867)
		settings = bot.get_emoji(1029305371552137236)
		cogwheel = bot.get_emoji(1028245358842744872)
		crown = bot.get_emoji(1029308239193591808)

		class View(discord.ui.View):

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{info}', row=0)
			async def first_button_callback(self, button, interaction):

					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{info} **Информация**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", f"`bio` **—** Биография участника.\n `help` **—** Посмотреть список доступных команд.\n `info` **—** Информация о боте.\n `leaders` **—** Топ рейтинга участников.\n `rank` **—** Уровень и опыт участника.\n `rewards` **—** Список наград за достижение уровней.\n `roleinfo` **—** Информация о роли.\n `serverinfo` **—** Информация о сервере.\n `stats` **—** Статистика пользователей.\n `userinfo` **—** Информация об участнике.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{interactions}', row=0)
			async def second_button_callback(self, button, interaction):


					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{interactions} **Взаимодействия**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", f"`bite` **—** Укусить человека.\n `blush` **—** Покраснеть.\n `clap` **—** Хлопать в ладоши.\n `coffee` **—** Пить кофе. \n `cooking` **—** Готовить вкусную еду.\n `cringe` **—** Кринжовать.\n `cry` **—** Плакать.\n `cuddle` **—** Обнять человека.\n `dance` **—** Танцевать.\n `drink` **—** Выпить много алкоголя.\n `facedesk` **—** Биться головой об стол.\n `feed` **—** Накормить человека.", False),
								(f"⠀", f"`fight` **—** Бороться с человеком.\n `game` **—** Играть в видеоигру.\n `happy` **—** Быть счастливым.\n `highfive` **—** Дать пять человеку.\n `hit` **—** Ударить человека.\n `hug` **—** Обнять человека.\n `kill` **—** Убить человека.\n `kiss` **—** Поцеловать человека.\n `kisscheek` **—** Поцеловать человека в щеку.\n `knees` **—** Сесть на колени к человеку.\n `laugh` **—** Смеяться.\n `lick` **—** Облизать человека.", False),
								(f"⠀", f"`love` **—** Показать любовь к человеку.\n `lurk` **—** Пытаться спрятаться.\n `music` **—** Слушать свою любимую музыку.\n `panic` **—** Паниковать.\n `pat` **—** Погладить человека.\n `poke` **—** Тыкнуть в человека.\n `pout` **—** Дуться на человека.\n `raise` **—** Взять человека на руки.\n `scare` **—** Напугать человека.\n `shoot` **—** Стрелять в человека.\n `shrug` **—** Пожимать плечами.\n `slap` **—** Дать пощечину человеку.", False),
								(f"⠀", f"`sleep` **—** Спать.\n `smile` **—** Улыбаться.\n  `smoke` **—** Курить.\n `smug` **—** Выглядить самодовольно.\n `takehand` **—** Взять человека за руку.\n `tea` **—** Пить чай.\n `think` **—** Думать о чем-то.\n `tickle` **—** Щекотать человека.\n `tie` **—** Связать человека.\n `wave` **—** Поприветствовать человека.\n `wink` **—** Подмигнуть человеку.\n `yawn` **—** Зевать.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{star}', row=0)
			async def third_button_callback(self, button, interaction):

					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{star} **Развлечения**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", f"`8ball` **—** Задать вопрос шару предсказаний.\n `animal` **—** Случайная фотография животного.\n `coinflip` **—** Подкинуть монетку.\n `dog` **—** Случайная фотография собаки.\n `fox` **—** Случайная фотография лисы.\n `koala` **—** Случайная фотография коалы.\n `panda` **—** Случайная фотография панды.\n `redpanda` **—** Случайная фотография малой (красной) панды.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{settings}', row=1)
			async def fourth_button_callback(self, button, interaction):

					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{settings} **Утилиты**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", f"`avatarka` **—** Посмотреть аватар участника.\n `choose` **—** Сделать выбор между тем или иным предметом.\n `code` **—** Отправить сообщение с форматированием кода.\n `emoji-list` **—** Список кастомных эмодзи сервера.\n `ping` **—** Узнать текущую задержку бота.\n`say` **—** Отправить сообщение от имени бота.\n `translate` **—** Перевести текст.\n `wiki` **—** Найти статью с Википедии.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{crown}', row=1)
			async def fifth_button_callback(self, button, interaction):

					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{crown} **Модерация**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", "`ban` **—** Заблокировать участника.\n `forceban` **—** Принудительно заблокировать участника.\n `kick` **—** Выгнать участника.\n `purge` **—** Очистить сообщения в чате.\n `resetbio` **—** Удалить биографию участнику.\n `setnick` **—** Установить серверный никнейм участнику. \n `softban` **—** Заблокировать участника с очисткой сообщений.\n `unban` **—** Разблокировать участника.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

			@discord.ui.button(style=discord.ButtonStyle.grey, emoji=f'{cogwheel}', row=1)
			async def sixth_button_callback(self, button, interaction):

					if interaction.user.id == ctx.author.id:

						emb = discord.Embed(description=f'{cogwheel} **Настройки**', colour=EMBED_COLOUR_SUCCESS)


						fields = [(f"{docs} Команды категории", f"`automod links` **—** Автоматическая модерация (ссылки).\n `levels` **—** Управление системой уровней.\n `removerole` **—** Убрать получение награды на определённом уровне.\n `setprefix` **—** Управление префиксами бота на сервере.\n `setrole` **—** Добавить получение награды на определённом уровне.\n `setvoice` **—** Управление приватными голосовыми комнатами.\n `setwelcome` **—** Выбрать канал для приветствий.\n `welcome` **—** Управление системой приветствий.", False)]

						for name, value, inline in fields:
							emb.add_field(name=name, value=value, inline=inline)
						
						return await interaction.response.send_message(embed=emb, ephemeral=True)

					emb = discord.Embed(description = f'**{interaction.user.name}**, это взаимодействие доступно автору, запросившему команду.', color=EMBED_COLOUR_SUCCESS)
					emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

					return await interaction.response.send_message(embed=emb, ephemeral=True)

		view = View(timeout=None)

		emb = discord.Embed(description=f'・Узнать детальную информацию о каждом разделе можно при помощи кнопок снизу.', colour=EMBED_COLOUR_SUCCESS)

		fields = [(f"{info} Информация", f"`bio`, `help`, `info`, `leaders`, `rank`, `rewards`, `roleinfo`, `serverinfo`, `stats`, `userinfo`", False),
				(f"{interactions} Взаимодействия", f"`bite`, `blush`, `clap`, `coffee`, `cooking`, `cringe`, `cry`, `cuddle`, `dance`, `drink`, `facedesk`, `feed`, `fight`, `game`, `happy`, `highfive`, `hit`, `hug`, `kill`, `kiss`, `kisscheek`, `knees`, `laugh`, `lick`, `love`, `lurk`, `music`, `panic`, `pat`, `poke`, `pout`, `raise`, `scare`, `shoot`, `shrug`, `slap`, `sleep`, `smile`, `smoke`, `smug`, `takehand`, `tea`,`think`, `tickle`, `tie`, `wave`, `wink`, `yawn`", False),
				(f"{star} Развлечения", f"`8ball`, `animal`, `coinflip`, `dog`, `fox`, `koala`, `panda`, `redpanda`", False),
				(f"{settings} Утилиты", f"`avatarka`, `choose`, `code`, `emoji-list`, `ping`, `say`, `translate`, `wiki`", False),
				(f"{crown} Модерация", f"`ban`, `forceban`, `kick`, `purge`, `resetbio`, `setnick`, `softban`, `unban`", False),
				(f"{cogwheel} Настройки", f"`automod links`, `levels`, `removerole`, `setprefix`, `setrole`, `setvoice`, `setwelcome`, `welcome`", False)]

		for name, value, inline in fields:
			emb.add_field(name=name, value=value, inline=inline)
			emb.set_thumbnail(url=bot.user.display_avatar.with_size(128))
			emb.set_author(name='Информация о командах', icon_url='https://i.imgur.com/nXPCSIX.png')

		await ctx.respond(embed=emb, view=view)

def setup(bot):
	bot.add_cog(help(bot))