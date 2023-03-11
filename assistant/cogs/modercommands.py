from main import bot
from global_sets import *
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument, MissingPermissions
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS, BOT_USER_ID, ADMIN_ROLE_ID, CONTROL_ROLE_ID, COMMANDS_LOG_CHANNEL

class modercommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'kick', description='Кикнуть участника.')
	@bridge.has_permissions(kick_members = True)
	async def _kick(self, ctx, member: discord.Member, *, reason = "Не указана."):

		await ctx.trigger_typing()

		if member.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя кикнуть бота!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя кикнуть владельца сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя кикнуть самого себя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < member.top_role or ctx.author.top_role == member.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя кикнуть участника, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) кикнул **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Кик', icon_url='https://i.imgur.com/Wq0o3Gw.png')
			emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			emb_member = discord.Embed(description=f'Тебя кикнул модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сервера **{ctx.guild.name}**.', colour=EMBED_COLOUR_SUCCESS)
			emb_member.set_author(name='Кик', icon_url='https://i.imgur.com/Wq0o3Gw.png')
			emb_member.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb_member.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await member.send(embed = emb_member)
			await member.kick(reason=reason)

	@bridge.bridge_command(name = 'ban', description='Заблокировать участника.')
	@bridge.has_permissions(ban_members = True)
	async def _ban(self, ctx, member: discord.Member, *, reason = "Не указана."):

		await ctx.trigger_typing()
	
		if member.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать бота!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать владельца сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать самого себя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < member.top_role or ctx.author.top_role == member.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать участника, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) заблокировал **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Блокировка', icon_url='https://i.imgur.com/drNRj3M.png')
			emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			emb_member = discord.Embed(description=f'Тебя заблокировал модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сервера **{ctx.guild.name}**.', colour=EMBED_COLOUR_SUCCESS)
			emb_member.set_author(name='Блокировка', icon_url='https://i.imgur.com/drNRj3M.png')
			emb_member.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb_member.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await member.send(embed = emb_member)
			await member.ban(reason=reason)

	@bridge.bridge_command(name = 'forceban', description='Принудительно заблокировать участника.')
	@bridge.has_permissions(ban_members = True)
	async def _forceban(self, ctx, id: int, *, reason = "Не указана."):

		await ctx.trigger_typing()

		user = await bot.fetch_user(id)
		times_start = datetime.now()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать бота!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif user == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать владельца сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать самого себя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < user.top_role or ctx.author.top_role == user.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать участника, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) принудительно заблокировал **{user.name}** ({user.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Блокировка', icon_url='https://i.imgur.com/drNRj3M.png')
			emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await ctx.guild.ban(user)

	@bridge.bridge_command(name = 'softban', description='Заблокировать участника с очисткой сообщений.')
	@bridge.has_permissions(ban_members = True)
	async def _softban(self, ctx, member: discord.Member, *, reason = "Не указана."):

		await ctx.trigger_typing()

		if member.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать бота!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать владельца сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать самого себя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < member.top_role or ctx.author.top_role == member.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя заблокировать участника, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) заблокировал с очисткой сообщений **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Блокировка', icon_url='https://i.imgur.com/drNRj3M.png')
			emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await member.ban(reason=reason, delete_message_days=7)

	@bridge.bridge_command(name = 'unban', description='Снять блокировку с участника.')
	@bridge.has_permissions(ban_members = True)
	async def _unban(self, ctx, id: int, *, reason = "Не указана."):

		await ctx.trigger_typing()

		user = await bot.fetch_user(id)

		if user == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя снять блокировку с владельца сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя снять блокировку с самого себя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) снял блокировку с **{user.name}** ({user.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Блокировка', icon_url='https://i.imgur.com/drNRj3M.png')
			emb.add_field(name=f">>> Причина:", value=f"```{reason}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await ctx.guild.unban(user)

	@bridge.bridge_command(name = 'purge', description='Очистить сообщения в текущем канале.')
	@bridge.has_permissions(manage_messages = True)
	async def _purge(self, ctx, limit: int, member: discord.Member=None):

		await ctx.trigger_typing()

		msg = []

		if limit > 1000:
			emb = discord.Embed(description = f'**{ctx.author.name}**, количество сообщений не должно превышать 1000.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		if not member:
			await ctx.channel.purge(limit=limit+1)

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) очистил сообщения в текущем канале.', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Очистка сообщений', icon_url='https://i.imgur.com/v2B4eNY.png')
			emb.add_field(name=f">>> Количество:", value=f"```{limit}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			return await ctx.respond(embed=emb)

		async for m in ctx.channel.history():
			if len(msg) == limit:
				break
			if m.author == member:
				msg.append(m)
		await ctx.channel.delete_messages(msg)

		now = datetime.now()
		punish_start_time = now.timestamp()

		emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) очистил сообщения от участника **{member.name}#{member.discriminator}** ({member.mention}) в текущем канале.', colour=EMBED_COLOUR_SUCCESS)
		emb.set_author(name='Очистка сообщений', icon_url='https://i.imgur.com/v2B4eNY.png')
		emb.add_field(name=f">>> Количество:", value=f"```{limit}```", inline=True)
		emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

		await ctx.respond(embed=emb)

	@bridge.bridge_command(name = 'setnick', description='Установить серверный никнейм участнику.')
	@bridge.has_permissions(change_nickname=True)
	async def _setnick(self, ctx, member: discord.Member, *, nick):

		await ctx.trigger_typing()

		if len(nick) > 32:
			emb = discord.Embed(description = f'**{ctx.author.name}**, максимальное количество символов = 32!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.guild.owner:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя сменить никнейм владельцу сервера!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif member == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя сменить никнейм самому себе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		elif ctx.author.top_role < member.top_role or ctx.author.top_role == member.top_role:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя сменить никнейм участнику, у которого роли выше или равны тебе!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		else:

			now = datetime.now()
			punish_start_time = now.timestamp()

			emb= discord.Embed(description=f'Модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сменил никнейм **{member.name}** ({member.mention}).', colour=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Никнеймы', icon_url='https://i.imgur.com/pciFZgN.png')
			emb.add_field(name=f">>> Сменено на:", value=f"```{nick}```", inline=True)
			emb.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			emb_member = discord.Embed(description=f'Тебе сменил никнейм модератор **{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) сервера **{ctx.guild.name}**.', colour=EMBED_COLOUR_SUCCESS)
			emb_member.set_author(name='Никнеймы', icon_url='https://i.imgur.com/pciFZgN.png')
			emb_member.add_field(name=f">>> Сменено на:", value=f"```{nick}```", inline=True)
			emb_member.add_field(name=f">>> Дата:", value=f"<t:{int(punish_start_time)}:f>\n <t:{int(punish_start_time)}:R>", inline=True)

			await ctx.respond(embed=emb)
			await member.send(embed = emb_member)
			await member.edit(nick=nick)

	@_kick.error
	async def kick_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`kick [@участник] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`kick @vollar#0074 пример`', inline = True)
			await ctx.respond(embed = emb)

	@_ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`ban [@участник] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`ban @vollar#0074 пример`', inline = True)
			await ctx.respond(embed = emb)

	@_softban.error
	async def softban_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`softban [@участник] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`softban @vollar#0074 пример`', inline = True)
			await ctx.respond(embed = emb)

	@_forceban.error
	async def forceban_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи ID пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`forceban [ID] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`forceban 440407587037642783 пример`', inline = True)
			await ctx.respond(embed = emb)

	@_unban.error
	async def unban_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи ID пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`unban [ID] [причина]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`unban 440407587037642783 пример`', inline = True)
			await ctx.respond(embed = emb)

	@_purge.error
	async def purge_error(self, ctx, error):
		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи необходимые параметры!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`purge [количество]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`purge 1000`', inline = True)
			emb.add_field(name = '⠀', value = f'⠀', inline = True)
			emb.add_field(name = '>>> Пример №3:', value = f'`purge [количество] [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №4:', value = f'`purge 1000 @vollar#0074`', inline = True)
			await ctx.respond(embed = emb)

	@_setnick.error
	async def setnick_error(self, ctx, error):

		if isinstance(error, MissingPermissions): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, недостаточно прав для выполнения команды.', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			await ctx.respond(embed=emb)

		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`setnick [@участник] [ник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`setnick @vollar#0074 Воллар`', inline = True)
			await ctx.respond(embed = emb)

def setup(bot):
	bot.add_cog(modercommands(bot))