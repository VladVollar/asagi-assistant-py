from main import bot
from global_sets import *
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS
import aiosqlite
from googletrans import Translator
import time
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument

conn = sqlite3.connect('voice.db')
c = conn.cursor()

class utilities(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'avatarka', description='Аватар участника.')
	async def _avatarka(self, ctx, member: discord.Member = None):

				await ctx.trigger_typing()

				members = bot.get_emoji(1019884454338101300)
				arrow = bot.get_emoji(1026444971781398608)

				if member == None:  # если не упоминать участника тогда выводит аватар автора сообщения
					member = ctx.author

				embed = discord.Embed(description=f"{arrow} [**PNG**]({member.display_avatar.with_format('png')}) / [**JPG**]({member.display_avatar.with_format('jpg')}) / [**WEBP**]({member.display_avatar.with_format('webp')})", colour=EMBED_COLOUR_SUCCESS)
				embed.set_image(url=member.display_avatar.with_format('webp'))
				embed.set_author(name= f'Аватар участника {member.name}#{member.discriminator}', icon_url= 'https://i.imgur.com/Iyw8Unf.png')
				await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'wiki', description='Статья из Википедии.')
	async def _wiki(self, ctx, *, text):

		await ctx.trigger_typing()

		wikipedia.set_lang("ru")
		new_page = wikipedia.page(text)
		summ = wikipedia.summary(text)
		emb = discord.Embed(title= new_page.title, description= summ, colour=EMBED_COLOUR_SUCCESS)
		emb.set_author(name= 'Wiki', url= new_page.url, icon_url= 'https://i.imgur.com/ry6zJmx.png')
		await ctx.respond(embed=emb)

	@bridge.bridge_command(name = 'ping', description='Задержки бота.')
	async def _ping(self, ctx):

			await ctx.trigger_typing()

			time_1 = time.perf_counter()
			await ctx.trigger_typing()
			time_2 = time.perf_counter()
			latency = round((time_2-time_1)*1000)

			ping = bot.ws.latency

			embed =  discord.Embed(description = f'Задержка (API): {latency // 10:.0f}мс\nОбработка команд: {ping * 1000:.0f}мс', colour=EMBED_COLOUR_SUCCESS)
			embed.set_author(name='Задержки бота', icon_url='https://i.imgur.com/qwsOc2r.png')

			await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'say', description='Отправить сообщение от лица бота.')
	@commands.has_permissions(administrator = True)
	async def _say(self, ctx, *, text):

		await ctx.trigger_typing()
		await ctx.respond(f'Отправлено сообщение "{text}"', delete_after=1)
		await ctx.send(text)

	@bridge.bridge_command(name = 'emoji-list', description='Список эмодзи сервера.')
	async def _emojilist(self, ctx):

			await ctx.trigger_typing()

			server = ctx.guild
			emojis = [str(x) for x in server.emojis]
			await ctx.respond("".join(emojis))

	@bridge.bridge_command(name = 'code', description='Сообщение с форматированием кода.')
	async def _code(self, ctx, *, msg):

			await ctx.trigger_typing()
			await ctx.respond('Отправлено!', delete_after=1)
			await ctx.send("```" + msg.replace("`", "") + "```")

	@bridge.bridge_command(name = 'translate', description='Перевести текст на другой язык.')
	async def _translate(self, ctx, lang, *, thing):

		await ctx.trigger_typing()

		translator = Translator()
		translation = translator.translate(thing, dest=lang)
		embed =  discord.Embed(title=f'Перевод на `{lang}`', description = translation.text, colour=EMBED_COLOUR_SUCCESS)
		embed.add_field(name='Оригинальный текст', value=f"{thing}")
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'choose', description='Выбрать между тем или иным предметом.')
	async def _choose(self, ctx, *, choices):

			await ctx.trigger_typing()

			if choices == None:
				return await ctx.send('Необходимо указать, в формате: Пить чай|Кушать|Поспать')

			await ctx.respond('Я выбираю: ``{}``'.format(random.choice(choices.split("|"))))

	@_wiki.error
	async def wiki_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`wiki [текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`wiki discord`', inline = True)
			await ctx.send(embed = emb)

	@_say.error
	async def say_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`say [текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`say пример`', inline = True)
			await ctx.send(embed = emb)

	@_code.error
	async def code_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`code [текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`code пример`', inline = True)
			await ctx.send(embed = emb)

	@_translate.error
	async def translate_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`translate [язык] [текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`translate de пример`', inline = True)
			await ctx.send(embed = emb)

	@_choose.error
	async def choose_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`choose [текст|текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`choose пример|пример`', inline = True)
			await ctx.send(embed = emb)

def setup(bot):
	bot.add_cog(utilities(bot))