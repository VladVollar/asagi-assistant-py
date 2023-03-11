import aiosqlite
from main import bot
from global_sets import *
from config import ERROR_EMOJI
import datetime
from datetime import timedelta
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument, MissingPermissions

class automod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_message(self, message):

		if message.guild is None:
			return

		async with aiosqlite.connect('voice.db') as db:
			async with db.cursor() as cursor:

				await cursor.execute("SELECT automodsys FROM automodSettings WHERE guild = ?", (message.guild.id,))
				automodsys = await cursor.fetchone()
				if automodsys:
					if not automodsys[0] == 1:
						return

				if message.author.id == bot.user.id:
					return

				msg_content = message.content.lower()

				links = ['http://', 'https://', '.com', '.gg']

				await cursor.execute("SELECT automodsys FROM automodSettings WHERE guild = ?", (message.guild.id,))
				automodsys = await cursor.fetchone()
				if automodsys:
					if automodsys[0]:

						if any(word in msg_content for word in links):
							if message.author.guild_permissions.administrator:
								return
							else:
								await message.delete()
								await message.author.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=900), reason='asd')
								emb = discord.Embed(description = f'**{message.author.name}** ({message.author.mention}), отправлять ссылки запрещено!\n (необходимо иметь права **Администратор**)', color=EMBED_COLOUR_SUCCESS)
								emb.set_author(name='Автомодерация: Ссылки', icon_url='https://i.imgur.com/drNRj3M.png')
								await message.channel.send(embed=emb)

					else:

						return

	@bridge.bridge_command(name = 'automod', description='Настройки автомодерации.')
	@bridge.has_permissions(administrator = True)
	async def _automod(self, ctx, mod, enabledisable):

		if mod == "links":
			if enabledisable == "enable":
				async with aiosqlite.connect('voice.db') as db:
					async with db.cursor() as cursor:
						await cursor.execute("SELECT automodsys FROM automodSettings WHERE guild = ?", (ctx.guild.id,))
						automodsys = await cursor.fetchone()
						if automodsys:
							if automodsys[0]:
								return await ctx.respond('Система автомодерации (ссылки) уже включена!')
							await cursor.execute("UPDATE automodSettings SET automodsys = ? WHERE guild = ?", (True, ctx.guild.id,))
						else:
							await cursor.execute("INSERT INTO automodSettings VALUES (?, ?)", (True, ctx.guild.id,))
						await ctx.respond('Система автомодерации (ссылки) теперь включена!')
					await db.commit()

		if mod == "links":
			if enabledisable == "disable":
				async with aiosqlite.connect('voice.db') as db:
					async with db.cursor() as cursor:
						await cursor.execute("SELECT automodsys FROM automodSettings WHERE guild = ?", (ctx.guild.id,))
						automodsys = await cursor.fetchone()
						if automodsys:
							if not automodsys[0]:
								return await ctx.respond('Система автомодерации (ссылки) уже выключена!')
							await cursor.execute("UPDATE automodSettings SET automodsys = ? WHERE guild = ?", (False, ctx.guild.id,))
						else:
							await cursor.execute("INSERT INTO welcomeSettings VALUES (?, ?)", (False, ctx.guild.id,))
						await ctx.respond('Система автомодерации (ссылки) теперь выключена!')
					await db.commit()

	@_automod.error
	async def automod_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые аргументы!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`automod links disable`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`automod links enable`', inline = True)
			await ctx.respond(embed = emb)

def setup(bot):
	bot.add_cog(automod(bot))