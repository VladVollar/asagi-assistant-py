from random import choices
from main import bot
from global_sets import *
from urllib.parse import urlparse
import aiohttp
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS

class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = '8ball', description='Шар предсказаний.')
	async def _8ball(self, ctx, *, msg):

		await ctx.trigger_typing()

		responses = [
				'Конечно нет.',
				'Вероятно, нет.',
				'Я не знаю, братан.',
				'Наверное.',
				'Да, черт возьми, чувак.',
				'Несомненно.',
				'Это определенно так.',
				'Без сомнения.',
				'Определенно да.',
				'Можешь рассчитывать на это.',
				'Как я вижу, да.',
				'Весьма вероятно.',
				'Хорошая перспектива.',
				'Да!',
				'Нет!',
				'Всё указывает на это!',
				'Пока не ясно... попробуй снова.',
				'Без понятия.',
				'Лучше тебе этого не знать...',
				'Не могу предсказать сейчас.',
				'Сконцентрируйся и спроси снова.',
				"Не рассчитывай на это.",
				'Мой ответ - нет.',
				'Мои источники говорят - нет.',
				'Мой ответ - да.',
				'Очень сомнительно.']

		response = random.choice(responses)
		embed = discord.Embed(description=f"**{ctx.author.name}** спросил(а): *{msg}*\n **Ответ**: *{response}*", colour=EMBED_COLOUR_SUCCESS)
		embed.set_author(name='Шар предсказаний', icon_url='https://i.imgur.com/IBq9qNm.png')
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'coinflip', description='Подкинуть монетку.')
	async def _coinflip(self, ctx):

		await ctx.trigger_typing()

		variable_list = [
				'*Орел*!',
				'*Решка*!']

		response = random.choice(variable_list)
		embed = discord.Embed(description=f"**{ctx.author.name}** подкинул(а) монетку и... {random.choice(variable_list)}", colour=EMBED_COLOUR_SUCCESS)
		embed.set_author(name='Подкинь монетку!', icon_url='https://i.imgur.com/2elQXxM.png')
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'dog', description='Случайная фотография собаки.')
	async def _dog(self, ctx):

		await ctx.trigger_typing()

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/dog') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, этот пёсик для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@bridge.bridge_command(name = 'panda', description='Случайная фотография панды.')
	async def _panda(self, ctx):

		await ctx.trigger_typing()

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/panda') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, эта пандочка для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@bridge.bridge_command(name = 'fox', description='Случайная фотография лисы.')
	async def _fox(self, ctx):

		await ctx.trigger_typing()

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/fox') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, эта лисичка для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@bridge.bridge_command(name = 'redpanda', description='Случайная фотография малой (красной) панды.')
	async def redpanda(self, ctx):

		await ctx.trigger_typing()

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/red_panda') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, эта малая (красная) пандочка для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@bridge.bridge_command(name = 'koala', description='Случайная фотография коалы.')
	async def koala(self, ctx):

		await ctx.trigger_typing()

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/koala') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, эта коала для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@bridge.bridge_command(name = 'animal', description='Случайная фотография животного.')
	async def animal(self, ctx):
		async with aiohttp.ClientSession() as session:

			await ctx.trigger_typing()

			responses = [
					'https://some-random-api.ml/img/dog',
					'https://some-random-api.ml/img/panda',
					'https://some-random-api.ml/img/fox',
					'https://some-random-api.ml/img/red_panda',
					'https://some-random-api.ml/img/koala']

			response = random.choice(responses)
			request = await session.get(f'{response}') # Make a request
			dogjson = await request.json() # Convert it to a JSON dictionary
		embed = discord.Embed(description=f"**{ctx.author.name}**, это животное для тебя!", colour=EMBED_COLOUR_SUCCESS) # Create embed
		embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
		await ctx.respond(embed=embed) # Send the embed

	@_8ball.error
	async def ball_error(self, ctx, error):

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи текст!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`8ball [текст]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`8ball пример?`', inline = True)
			await ctx.send(embed = emb)

def setup(bot):
	bot.add_cog(fun(bot))