from ast import Interactive
import discord
import os
import random
import sqlite3
import re
import aiosqlite
from easy_pil import *
from discord.ui import Button, View
from discord.ext import commands, bridge
from dotenv import load_dotenv
from config import *

token = os.environ['DISCORD_ASAGI_TOKEN']

# Функция с кастомным префиксом
async def getprefix(bot, message):
	async with aiosqlite.connect("voice.db") as db:
		async with db.cursor() as cursor:
			await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (message.guild.id,))
			data = await cursor.fetchone()
			if data:
				return commands.when_mentioned_or(*data)(bot, message)
			else:
				try:
					await cursor.execute('INSERT INTO main (prefix, guildID) VALUES (?, ?)', ('a!', message.guild.id,))
					await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (message.guild.id,))
					data = await cursor.fetchone()
					if data:
						await cursor.execute('UPDATE main SET prefix = ? WHERE guild = ? ', ('a!', message.guild.id,))
				except Exception:
					return commands.when_mentioned_or('a!')(bot, message)

bot = bridge.Bot(command_prefix = getprefix, intents=discord.Intents.all(), help_command=None)

# Подключение когов
for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

# Функции при загрузке бота
@bot.event
async def on_ready():
		print('Бот успешно запущен!')
		print(f'Моё имя - {bot.user.name}')
		print(f'Мой айди - {bot.user.id}')
		await bot.change_presence(status=discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.playing, name = f'a!help' ))
		for guild in bot.guilds:
			print(f'Подключен к серверам, у которых айди: {guild.id}')

@bot.event
async def on_message(message):

	if message.guild is None:
		return

	mention = f'<@{bot.user.id}>'

	conn = sqlite3.connect('voice.db')
	c = conn.cursor()

	for row in c.execute('SELECT prefix FROM main WHERE guildID = ?', (message.guild.id,)):

		if message.content == mention:
			prefix = discord.Embed(description=f"Текущий серверный префикс: `{row[0]}`\n В качестве префикса можно использовать слэш команды (`/`) или упоминание `{bot.user.name}`", colour=EMBED_COLOUR_SUCCESS)
			await message.channel.send(embed=prefix)

	await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
	async with aiosqlite.connect("voice.db") as db:
		async with db.cursor() as cursor:
			await cursor.execute('INSERT INTO main (prefix, guildID) VALUES (?,?)', ('a!', guild.id,))
		await db.commit()

	button1 = Button(label="Сервер поддержки", url="https://discord.gg/Pc3QfCwryz")
	view = View()
	view.add_item(button1)

	user = bot.get_user(guild.owner.id)
	await user.send(f'**Приветствую!**\nНастроить {bot.user.name} можно при помощи команд.\n\nВесь список команд можно просмотреть тут: `a!help`.', view=view)

@bot.event
async def on_guild_remove(guild):
	async with aiosqlite.connect("voice.db") as db:
		async with db.cursor() as cursor:
			await cursor.execute('SELECT prefix FROM main WHERE guildID = ?', (guild.id,))
			data = await cursor.fetchone()
			if data:
				await cursor.execute('DELETE FROM main WHERE guildID = ?', (guild.id,))
		await db.commit()

	button1 = Button(label="Сервер поддержки", url="https://discord.gg/Pc3QfCwryz")
	view = View()
	view.add_item(button1)

	user = bot.get_user(guild.owner.id)
	await user.send(f'**Мы обязательно постараемся улучшить бота!**\nНам очень жаль, что ты уже уходишь от нас.\n\nОставить свои предложения по улучшению сервиса можешь на сервере поддержки.', view=view)

# КД на использование команды
@bot.listen("on_command_error")
async def on_command_error(ctx, error):

		if isinstance(error, commands.CommandOnCooldown):
			time = round(error.retry_after)
			emb = discord.Embed(description = f'**{ctx.author.name}**, подожди {time} секунд!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.send(embed = emb, delete_after=time)

# Бот не будет реагировать на сообщения в ЛС
@bot.check
async def global_guild_only(ctx):
    if not ctx.guild:
        raise commands.NoPrivateMessage()
    return True

# Загрузить определённый ког-файл командой
@bot.bridge_command(name = 'load', description='Загрузить ког-файл(ы).', guild_ids=[1002113370763317378])
async def _load(ctx, extensions):

	if ctx.author.id == 440407587037642783:
	
		bot.load_extension(f'cogs.{extensions}')
		await ctx.respond(f'**{ctx.author.name}**, ког-файл "{extensions}" загружен.')

	else:

		emb = discord.Embed(description = f'**{ctx.author.name}**, эта команда доступна разработчикам бота!', color=EMBED_COLOUR_SUCCESS)
		emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

		await ctx.respond(embed=emb)

# Перезагрузить определённый ког-файл командой
@bot.bridge_command(name = 'reload', description='Перезагрузить ког-файл(ы).', guild_ids=[1002113370763317378])
async def _reload(ctx, extensions):

	if ctx.author.id == 440407587037642783:

		bot.unload_extension(f'cogs.{extensions}')
		bot.load_extension(f'cogs.{extensions}')
		await ctx.respond(f'**{ctx.author.name}**, ког-файл "{extensions}" перезагружен.')

	else:

		emb = discord.Embed(description = f'**{ctx.author.name}**, эта команда доступна разработчикам бота!', color=EMBED_COLOUR_SUCCESS)
		emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

		await ctx.respond(embed=emb)

# Выгрузить определённый ког-файл командой
@bot.bridge_command(name = 'unload', description='Выгрузить ког-файл(ы).', guild_ids=[1002113370763317378])
async def _unload(ctx, extensions):

	if ctx.author.id == 440407587037642783:

		bot.unload_extension(f'cogs.{extensions}')
		await ctx.respond(f'**{ctx.author.name}**, ког-файл "{extensions}" выгружен.')

	else:

		emb = discord.Embed(description = f'**{ctx.author.name}**, эта команда доступна разработчикам бота!', color=EMBED_COLOUR_SUCCESS)
		emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')

		await ctx.respond(embed=emb)
		
bot.run(token)