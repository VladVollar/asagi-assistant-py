from main import bot
from global_sets import *
from discord.ext import bridge
from discord.ext.commands import MissingRequiredArgument
from config import DELETE_COMMANDS, EMBED_COLOUR_ERROR, EMBED_COLOUR_SUCCESS, ERROR_EMOJI

class interaction(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	@bridge.bridge_command(name = 'bite', description='Укусить участника.')
	async def _bite(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://i.waifu.pics/uLaSSOF.gif',
			'https://i.waifu.pics/iErgSVO.gif',
			'https://i.waifu.pics/asvURcX.gif',
			'https://i.waifu.pics/0eShqy~.gif',
			'https://i.waifu.pics/8AdNq9W.gif',
			'https://i.waifu.pics/9WRtGbr.gif',
			'https://i.waifu.pics/W0VmZno.gif',
			'https://i.waifu.pics/Mz~1TKA.gif',
			'https://i.waifu.pics/UgYmj1t.gif',
			'https://i.waifu.pics/pQ1rb_d.gif',
			'https://i.waifu.pics/T_qYUxK.gif',
			'https://i.waifu.pics/-r7iPPN.gif',
			'https://i.waifu.pics/m71ri9g.gif',
			'https://i.waifu.pics/pi4nDsc.png',
			'https://i.waifu.pics/K5Amzkb.gif',
			'https://i.waifu.pics/Bn-ITNy.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** укусил(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'blush', description='Покраснеть.')
	async def _blush(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://i.waifu.pics/6dp-Tu2.gif',
			'https://i.waifu.pics/0y6U0OI.gif',
			'https://i.waifu.pics/1OUw5ve.gif',
			'https://i.waifu.pics/omFJRuf.gif',
			'https://i.waifu.pics/S6TyrfT.gif',
			'https://i.waifu.pics/2thWaSw.gif',
			'https://i.waifu.pics/3XteioK.gif',
			'https://i.waifu.pics/-LSfn~O.gif',
			'https://i.waifu.pics/z1enfIu.gif',
			'https://i.waifu.pics/v0O9TYs.gif',
			'https://i.waifu.pics/hzR2Waj.gif',
			'https://i.waifu.pics/dxS7BM7.gif',
			'https://i.waifu.pics/SG~JcKH.gif',
			'https://i.waifu.pics/_drflhc.gif',
			'https://i.waifu.pics/8rmSHzK.gif',
			'https://i.waifu.pics/_GixPwJ.gif',
			'https://i.waifu.pics/LGzDX-H.gif',
			'https://i.waifu.pics/kfFbx6B.gif',
			'https://i.waifu.pics/FHEG7k8.gif',
			'https://i.waifu.pics/6Rf2p0i.gif',
			'https://i.waifu.pics/51Bpr~F.gif',
			'https://i.waifu.pics/-Cf_23g.gif',
			'https://i.waifu.pics/WJ1kH-~.gif',
			'https://i.waifu.pics/6rca2uM.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** покраснел.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'clap', description='Хлопать в ладоши.')
	async def _clap(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/4LlTKTRd0Q0AAAAC/sushichaeng-anime.gif',
			'https://c.tenor.com/peuqWYmwHscAAAAC/tears-of-joy-clapping.gif',
			'https://c.tenor.com/kaRCm9ELxKgAAAAC/menhera-chan-chibi.gif',
			'https://c.tenor.com/YgkED1S-Or0AAAAC/clapping-clapping-hands.gif',
			'https://c.tenor.com/zVvMxtmpRaMAAAAC/taiga-asaka-clapping.gif',
			'https://c.tenor.com/2RMlQdkpG1cAAAAC/clapping-anime.gif',
			'https://c.tenor.com/xdj7XE8llU8AAAAC/nekopara-clap.gif',
			'https://c.tenor.com/jncqY9-RbqcAAAAd/mushoku-tensei-roxy.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** хлопает в ладоши.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'coffee', description='Пить кофе.')
	async def _coffee(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://media.tenor.com/images/e001c352aed2d545e8873ffbbdbeb664/tenor.gif',
			'https://c.tenor.com/9oZmHkACCFcAAAAC/anime-coffee.gif',
			'https://c.tenor.com/yoXaDbOdqb4AAAAC/coffee-overflow.gif',
			'https://c.tenor.com/KceeOIOM8IcAAAAC/coffee-anime.gif',
			'https://media.tenor.com/_h5RONFrRawAAAAC/cafe-coffee.gif',
			'https://media.tenor.com/HJJrgYOmHT8AAAAC/coffee-anime.gif',
			'https://i.pinimg.com/originals/90/0d/40/900d4092592c8c76514825702e0b1871.gif',
			'https://cdn57.picsart.com/169819573000201.gif?to=crop&type=webp&r=1456x789&q=85',
			'https://i.pinimg.com/originals/4f/a3/63/4fa3632e36eee33fc8aa8a9a9757c6df.gif',
			'https://gifdb.com/images/high/anime-stirring-coffee-5rjv66szisw69q5n.webp',
			'https://i.kym-cdn.com/photos/images/original/001/750/043/d0a.gif',
			'https://i.gifer.com/DWbF.gif',
			'https://i.pinimg.com/originals/92/20/28/92202875e165f0d415357d384e37ee69.gif',
			'https://gifimage.net/wp-content/uploads/2017/09/anime-coffee-gif-9.gif',
			'https://i.pinimg.com/originals/b8/dc/a8/b8dca8f02de9a513ddbe10aec2033946.gif',
			'https://i.pinimg.com/originals/2f/ae/0e/2fae0e42254c6c152af35ef58edcc792.gif',
			'https://i.pinimg.com/originals/a0/d4/ce/a0d4ce3a21e9f0e12c3f685469840025.gif',
			'https://p.favim.com/orig/2018/08/20/food-coffee-gif-Favim.com-6156842.gif',
			'https://i.pinimg.com/originals/18/9b/73/189b73d8bfa9e2244744dca531cddc35.gif',
			'https://animesher.com/orig/1/193/1935/19351/animesher.com_anime-food-food-coffee-1935160.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** пьёт кофе.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'cooking', description='Готовить вкусную еду.')
	async def _cooking(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/7QzBAuqQW6oAAAAC/2dfood-food.gif',
			'https://c.tenor.com/-cmMYhIgKwAAAAAC/anime-anime-gif.gif',
			'https://c.tenor.com/AQIDiqxaVSkAAAAC/anime-cooking.gif',
			'https://c.tenor.com/N2iY9o5RMUIAAAAC/food-wars.gif',
			'https://c.tenor.com/NbTORHRkL8oAAAAC/anime-fo-anime.gif',
			'https://c.tenor.com/r97d8qE5-8IAAAAC/anime-food-food.gif',
			'https://c.tenor.com/flX5arjPeDcAAAAC/sora-cooking.gif',
			'https://c.tenor.com/C5bWpsCtnCsAAAAC/tempura.gif',
			'https://c.tenor.com/li8Bg6row1gAAAAC/cucumber-hamtaro.gif',
			'https://c.tenor.com/grXjogd18YIAAAAC/anime-tomato.gif',
			'https://c.tenor.com/zCFABRtIOyIAAAAC/food-anime-food.gif',
			'https://c.tenor.com/bMKqP414820AAAAC/neet-anime.gif',
			'https://c.tenor.com/nWsm-nX-DLUAAAAC/excited-cooking.gif',
			'https://c.tenor.com/yZCowKJy4UoAAAAd/anime-anime-gif.gif',
			'https://c.tenor.com/_D_4FTntHhsAAAAC/shokugeki-no-soma-food-wars.gif',
			'https://c.tenor.com/O_EFeZerCmUAAAAC/siri-cooking-anime.gif',
			'https://c.tenor.com/gAvAdxKRn9MAAAAC/dorohedoro-nikaido.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** готовит вкусную еду.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'cringe', description='Кринжовать.')
	async def _cringe(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/ew7hDhIqUFkAAAAC/anime-tanjiro.gif',
			'https://c.tenor.com/7dWlqDyO8wYAAAAC/anime-angry.gif',
			'https://c.tenor.com/fiWdHp6pHbAAAAAC/annoyed-anime-face-angry-anime-boy.gif',
			'https://c.tenor.com/vUmgC1eRtl0AAAAC/heanna-sumire-love-live-superstar.gif',
			'https://c.tenor.com/b7Y2mhaX6F8AAAAC/cringe-uneasy.gif',
			'https://c.tenor.com/K8jGB-xcdnoAAAAC/cringe-anime.gif',
			'https://media.tenor.com/0Uf0-C5vSHMAAAAC/died-of-cringe-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** кринжует.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'cry', description='Плакать.')
	async def _cry(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/cry/001.gif',
			'https://nekos.best/api/v2/cry/002.gif',
			'https://nekos.best/api/v2/cry/003.gif',
			'https://nekos.best/api/v2/cry/004.gif',
			'https://nekos.best/api/v2/cry/005.gif',
			'https://nekos.best/api/v2/cry/006.gif',
			'https://nekos.best/api/v2/cry/007.gif',
			'https://nekos.best/api/v2/cry/008.gif',
			'https://nekos.best/api/v2/cry/009.gif',
			'https://nekos.best/api/v2/cry/010.gif',
			'https://nekos.best/api/v2/cry/011.gif',
			'https://nekos.best/api/v2/cry/012.gif',
			'https://nekos.best/api/v2/cry/013.gif',
			'https://nekos.best/api/v2/cry/014.gif',
			'https://nekos.best/api/v2/cry/015.gif',
			'https://nekos.best/api/v2/cry/016.gif',
			'https://nekos.best/api/v2/cry/017.gif',
			'https://nekos.best/api/v2/cry/018.gif',
			'https://nekos.best/api/v2/cry/019.gif',
			'https://nekos.best/api/v2/cry/020.gif',
			'https://nekos.best/api/v2/cry/021.gif',
			'https://nekos.best/api/v2/cry/022.gif',
			'https://nekos.best/api/v2/cry/023.gif',
			'https://nekos.best/api/v2/cry/024.gif',
			'https://nekos.best/api/v2/cry/025.gif',
			'https://nekos.best/api/v2/cry/026.gif',
			'https://nekos.best/api/v2/cry/027.gif',
			'https://nekos.best/api/v2/cry/028.gif',
			'https://nekos.best/api/v2/cry/029.gif',
			'https://nekos.best/api/v2/cry/030.gif',
			'https://nekos.best/api/v2/cry/031.gif',
			'https://nekos.best/api/v2/cry/032.gif',
			'https://nekos.best/api/v2/cry/033.gif',
			'https://nekos.best/api/v2/cry/034.gif',
			'https://nekos.best/api/v2/cry/035.gif',
			'https://nekos.best/api/v2/cry/036.gif',
			'https://nekos.best/api/v2/cry/037.gif',
			'https://nekos.best/api/v2/cry/038.gif',
			'https://nekos.best/api/v2/cry/039.gif',
			'https://nekos.best/api/v2/cry/040.gif',
			'https://i.waifu.pics/X2~B7zv.gif',
			'https://i.waifu.pics/F2owLQG.gif',
			'https://i.waifu.pics/Vz~LV2J.gif',
			'https://i.waifu.pics/tK9Qfqy.gif',
			'https://i.waifu.pics/YjORwmK.gif',
			'https://i.waifu.pics/f-f60kK.gif',
			'https://i.waifu.pics/sJmYw5w.gif',
			'https://i.waifu.pics/R96xAxE.gif',
			'https://i.waifu.pics/MT1xRHu.gif',
			'https://i.waifu.pics/fmX3C31.gif',
			'https://i.waifu.pics/Mqpc-H0.gif',
			'https://i.waifu.pics/kKtk3r_.gif',
			'https://i.waifu.pics/W1vb9i~.gif',
			'https://i.waifu.pics/6x-~igD.gif',
			'https://i.waifu.pics/k2r~YJ0.gif',
			'https://i.waifu.pics/ABIGqvR.gif',
			'https://i.waifu.pics/Pw3Y-ug.gif',
			'https://i.waifu.pics/NvYspNo.gif',
			'https://i.waifu.pics/u0O-PDM.gif',
			'https://i.waifu.pics/owz~e8r.gif',
			'https://i.waifu.pics/yfg1Ba4.gif',
			'https://i.waifu.pics/W1vb9i~.gif',
			'https://i.waifu.pics/KbHNNlO.gif',
			'https://i.waifu.pics/UbEWz9r.gif',
			'https://i.waifu.pics/vpNr0RD.gif',
			'https://i.waifu.pics/Oyvh5pb.gif',
			'https://i.waifu.pics/YGUgMhs.gif',
			'https://i.waifu.pics/ed4T9wI.gif',
			'https://i.waifu.pics/USePcuV.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** плачет.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'cuddle', description='Обнять участника.')
	async def _cuddle(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://cdn.nekos.life/cuddle/cuddle_001.gif',
			'https://cdn.nekos.life/cuddle/cuddle_002.gif',
			'https://cdn.nekos.life/cuddle/cuddle_003.gif',
			'https://cdn.nekos.life/cuddle/cuddle_004.gif',
			'https://cdn.nekos.life/cuddle/cuddle_005.gif',
			'https://cdn.nekos.life/cuddle/cuddle_006.gif',
			'https://cdn.nekos.life/cuddle/cuddle_007.gif',
			'https://cdn.nekos.life/cuddle/cuddle_008.gif',
			'https://cdn.nekos.life/cuddle/cuddle_009.gif',
			'https://cdn.nekos.life/cuddle/cuddle_010.gif',
			'https://cdn.nekos.life/cuddle/cuddle_011.gif',
			'https://cdn.nekos.life/cuddle/cuddle_012.gif',
			'https://cdn.nekos.life/cuddle/cuddle_013.gif',
			'https://cdn.nekos.life/cuddle/cuddle_014.gif',
			'https://cdn.nekos.life/cuddle/cuddle_015.gif',
			'https://cdn.nekos.life/cuddle/cuddle_016.gif',
			'https://cdn.nekos.life/cuddle/cuddle_017.gif',
			'https://cdn.nekos.life/cuddle/cuddle_020.gif',
			'https://cdn.nekos.life/cuddle/cuddle_021.gif',
			'https://cdn.nekos.life/cuddle/cuddle_022.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** обнял(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'dance', description='Танцевать.')
	async def _dance(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/dance/001.gif',
			'https://nekos.best/api/v2/dance/002.gif',
			'https://nekos.best/api/v2/dance/003.gif',
			'https://nekos.best/api/v2/dance/004.gif',
			'https://nekos.best/api/v2/dance/005.gif',
			'https://nekos.best/api/v2/dance/006.gif',
			'https://nekos.best/api/v2/dance/007.gif',
			'https://nekos.best/api/v2/dance/008.gif',
			'https://nekos.best/api/v2/dance/009.gif',
			'https://nekos.best/api/v2/dance/010.gif',
			'https://nekos.best/api/v2/dance/011.gif',
			'https://nekos.best/api/v2/dance/012.gif',
			'https://nekos.best/api/v2/dance/013.gif',
			'https://nekos.best/api/v2/dance/014.gif',
			'https://nekos.best/api/v2/dance/015.gif',
			'https://nekos.best/api/v2/dance/016.gif',
			'https://nekos.best/api/v2/dance/017.gif',
			'https://nekos.best/api/v2/dance/018.gif',
			'https://nekos.best/api/v2/dance/019.gif',
			'https://nekos.best/api/v2/dance/020.gif',
			'https://nekos.best/api/v2/dance/021.gif',
			'https://i.waifu.pics/ZMfBvh5.gif',
			'https://i.waifu.pics/urWfg8X.gif',
			'https://i.waifu.pics/_aPDF1R.gif',
			'https://i.waifu.pics/oI~t28j.gif',
			'https://i.waifu.pics/d5J29kk.gif',
			'https://i.waifu.pics/GAD~oBd.gif',
			'https://i.waifu.pics/GNw8eK7.gif',
			'https://i.waifu.pics/maB4-hQ.gif',
			'https://i.waifu.pics/Fzhg8rD.gif',
			'https://i.waifu.pics/fm6qpsc.gif',
			'https://i.waifu.pics/tlPg1K7.gif',
			'https://i.waifu.pics/UWuqvzI.gif',
			'https://i.waifu.pics/3Ug_RJ9.gif',
			'https://i.waifu.pics/K1sfljp.gif',
			'https://i.waifu.pics/M8G5bSN.gif',
			'https://i.waifu.pics/PCTp3I3.gif',
			'https://i.waifu.pics/dWcXWF0.gif',
			'https://i.waifu.pics/Rv-lh_B.gif',
			'https://i.waifu.pics/_BHLCbF.gif',
			'https://i.waifu.pics/J06YCu7.gif',
			'https://i.waifu.pics/o1vg08f.gif',
			'https://i.waifu.pics/_aPDF1R.gif',
			'https://i.waifu.pics/afr4ScV.gif',
			'https://i.waifu.pics/JESnpUS.gif',
			'https://i.waifu.pics/iVDuV9y.gif',
			'https://i.waifu.pics/YTiV2fl.gif',
			'https://i.waifu.pics/V4ztx1j.gif',
			'https://i.waifu.pics/mKuJrYc.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** танцует.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'drink', description='Пить много алкоголя.')
	async def _drink(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://cdn.discordapp.com/attachments/813336203213537300/997981326890237952/video_1_1.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981327204823101/video_3.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981326588256336/video_1.gif',
			'https://c.tenor.com/n_cTk-xpCCsAAAAd/merkatz-drink.gif',
			'https://c.tenor.com/fAb9H6KFL5oAAAAC/michiko-to-hatchin-michiko-and-hatchin.gif',
			'https://c.tenor.com/m6db5fdc38wAAAAC/anime-drinking-anime-alcohol.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981328400207982/video_8.gif',
			'https://c.tenor.com/Af11VJi0qBsAAAAd/anime-drinking-anime.gif',
			'https://c.tenor.com/4YMLsd4fSK8AAAAC/kozuki-oden-drinking.gif',
			'https://c.tenor.com/lk8yVO8VOEsAAAAC/drinking-kobayashi.gif',
			'https://c.tenor.com/WkrtHIR7-pYAAAAC/anime-beer-bottle.gif',
			'https://c.tenor.com/ePMGSPDxkp8AAAAC/anime-cheers-anime-alcohol.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981327682969640/video_4.gif',
			'https://c.tenor.com/PTKbiZDT8JwAAAAC/one-piece-cheers.gif',
			'https://c.tenor.com/U20VhSWkO-EAAAAC/anime-cheers-anime-alcohol.gif',
			'https://c.tenor.com/aPSQxKarUAsAAAAd/nananiji-drink.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981328031092836/video_4_1.gif',
			'https://c.tenor.com/vP8ox9xxvlMAAAAC/anime-smile.gif',
			'https://cdn.discordapp.com/attachments/813336203213537300/997981326588256336/video_1.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** пьет чертовски много алкоголя.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'facedesk', description='Биться головой о стол.')
	async def _facedesk(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/iLKTcYbVzJQAAAAC/kuroko-anime.gif',
			'https://c.tenor.com/gkNbkv0dDpYAAAAC/anime-girl-facepalm.gif',
			'https://c.tenor.com/6dRXjgbOSp0AAAAC/kuroko-anime.gif',
			'https://c.tenor.com/JYmoPxlrgrUAAAAC/anime-head-bang.gif',
			'https://c.tenor.com/9RYGWZUJ6PgAAAAC/saki-kasukabe-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** бьется головой о стол.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'feed', description='Накормить участника.')
	async def _feed(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://cdn.nekos.life/feed/feed_001.gif',
			'https://cdn.nekos.life/feed/feed_002.gif',
			'https://cdn.nekos.life/feed/feed_003.gif',
			'https://cdn.nekos.life/feed/feed_004.gif',
			'https://cdn.nekos.life/feed/feed_005.gif',
			'https://cdn.nekos.life/feed/feed_006.gif',
			'https://cdn.nekos.life/feed/feed_007.gif',
			'https://cdn.nekos.life/feed/feed_008.gif',
			'https://cdn.nekos.life/feed/feed_009.gif',
			'https://cdn.nekos.life/feed/feed_010.gif',
			'https://cdn.nekos.life/feed/feed_011.gif',
			'https://cdn.nekos.life/feed/feed_012.gif',
			'https://cdn.nekos.life/feed/feed_013.gif',
			'https://cdn.nekos.life/feed/feed_014.gif',
			'https://cdn.nekos.life/feed/feed_015.gif',
			'https://cdn.nekos.life/feed/feed_016.gif',
			'https://cdn.nekos.life/feed/feed_017.gif',
			'https://i.waifu.pics/chsjsyO.gif',
			'https://i.waifu.pics/06dGwQn.gif',
			'https://i.waifu.pics/2qqO27z.gif',
			'https://i.waifu.pics/-BiHx-0.gif',
			'https://i.waifu.pics/hsnaF2q.gif',
			'https://i.waifu.pics/qjjIrLt.gif',
			'https://i.waifu.pics/DO_DtXt.gif',
			'https://i.waifu.pics/lL98Wc0.gif',
			'https://i.waifu.pics/g6ISmbU.gif',
			'https://i.waifu.pics/PC57VxN.gif',
			'https://i.waifu.pics/n~C0SnU.gif',
			'https://i.waifu.pics/_Xhrs1u.gif',
			'https://i.waifu.pics/4FQ3SVe.gif',
			'https://i.waifu.pics/3F4NP~X.gif',
			'https://i.waifu.pics/Oci~KID.gif',
			'https://i.waifu.pics/3OZp3xq.gif',
			'https://i.waifu.pics/FJyxFzB.gif',
			'https://i.waifu.pics/3RgqSsF.gif',
			'https://i.waifu.pics/7hfyVIh.gif',
			'https://i.waifu.pics/XuMPaN9.gif',
			'https://i.waifu.pics/GfZNQ63.gif',
			'https://i.waifu.pics/adfkjmr.gif',
			'https://i.waifu.pics/fWfQO0f.gif',
			'https://i.waifu.pics/GDv4riP.gif',
			'https://i.waifu.pics/Fj1a1_r.gif',
			'https://i.waifu.pics/QH~dBDJ.gif',
			'https://i.waifu.pics/OSFgl1_.gif',
			'https://i.waifu.pics/-OvwPE6.gif',
			'https://i.waifu.pics/kff8lW2.gif',
			'https://i.waifu.pics/_yNoVRZ.gif',
			'https://i.waifu.pics/c2LToYU.gif',
			'https://i.waifu.pics/CqR0xX2.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** накормил(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'fight', description='Бороться с участником.')
	async def _fight(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://c.tenor.com/EfhPfbG0hnMAAAAC/slap-handa-seishuu.gif',
			'https://c.tenor.com/EdV_frZ4e_QAAAAC/anime-naruto.gif',
			'https://c.tenor.com/YuR7uAqxHPkAAAAd/fighting-anime.gif',
			'https://c.tenor.com/d44VyilsgeMAAAAd/vegeta-anime.gif',
			'https://c.tenor.com/o8RbiF5-9dYAAAAd/killua-hxh.gif',
			'https://c.tenor.com/Y_4_saaGYwUAAAAC/jujutsu-kaisen-mahito.gif',
			'https://c.tenor.com/Zj2qbOjt9_AAAAAC/mei-ling-fmab.gif',
			'https://c.tenor.com/gOh4Yk4on3kAAAAC/anime-fight.gif',
			'https://c.tenor.com/qQ5Eu-nhIOQAAAAd/naruto-sasuke.gif',
			'https://c.tenor.com/4p2gwNLsxBEAAAAC/whizzy-imposterfox.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** борется с **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'game', description='Играть в видеоигры.')
	async def _game(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/ml-Znu6s0q0AAAAC/anime-gaming.gif',
			'https://c.tenor.com/QCnolPnSaAsAAAAC/keima-katsuragi-keima.gif',
			'https://c.tenor.com/L1TNbrAUXfMAAAAC/anime-game.gif',
			'https://c.tenor.com/zKowF7AjXk4AAAAC/chiaki-nanami-danganronpa.gif',
			'https://c.tenor.com/ELKnB8G-0IwAAAAC/kon-yui.gif',
			'https://c.tenor.com/OQwvF2gsxvsAAAAC/anime-playing.gif',
			'https://c.tenor.com/ELKnB8G-0IwAAAAC/kon-yui.gif',
			'https://c.tenor.com/I3PQi7EnJuEAAAAC/anime-ijiranaide-nagatoro.gif',
			'https://c.tenor.com/Ed5ftruUF7EAAAAd/game-gamer.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** играет в видеоигры.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'happy', description='Быть счастливым.')
	async def _happy(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://i.waifu.pics/nxIuFgL.gif',
			'https://i.waifu.pics/Vk_UEkj.gif',
			'https://i.waifu.pics/GTqw3qe.gif',
			'https://i.waifu.pics/vgmgptj.gif',
			'https://i.waifu.pics/zCYkbZ_.gif',
			'https://i.waifu.pics/Y74CXhF.gif',
			'https://i.waifu.pics/jHsOPQX.gif',
			'https://i.waifu.pics/GasY2d0.gif',
			'https://i.waifu.pics/yiso92r.gif',
			'https://i.waifu.pics/MjP8LHh.png',
			'https://i.waifu.pics/M~X5w4e.gif',
			'https://i.waifu.pics/-ZeGw8v.gif',
			'https://i.waifu.pics/FTwUuPj.gif',
			'https://i.waifu.pics/ksBpRuX.gif',
			'https://i.waifu.pics/IWgv2sL.gif',
			'https://i.waifu.pics/81v5ro2.gif',
			'https://i.waifu.pics/jHsOPQX.gif',
			'https://i.waifu.pics/7g_nzKq.gif',
			'https://i.waifu.pics/555iqKW.gif',
			'https://i.waifu.pics/ksBpRuX.gif',
			'https://i.waifu.pics/SWMEyvi.gif',
			'https://i.waifu.pics/VT14ln7.gif',
			'https://i.waifu.pics/~bRfkTQ.gif',
			'https://i.waifu.pics/ll1i0po.gif',
			'https://i.waifu.pics/7UFAxs2.gif',
			'https://i.waifu.pics/f4yuYhw.gif',
			'https://i.waifu.pics/i0bxhu9.gif',
			'https://i.waifu.pics/7ELy73A.gif',
			'https://i.waifu.pics/eMN_w1U.gif',
			'https://i.waifu.pics/Hv9zTuk.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** счастлив(а).", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'highfive', description='Дать пять участнику.')
	async def _highfive(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://nekos.best/api/v2/highfive/001.gif',
			'https://nekos.best/api/v2/highfive/002.gif',
			'https://nekos.best/api/v2/highfive/003.gif',
			'https://nekos.best/api/v2/highfive/004.gif',
			'https://nekos.best/api/v2/highfive/005.gif',
			'https://nekos.best/api/v2/highfive/006.gif',
			'https://nekos.best/api/v2/highfive/007.gif',
			'https://nekos.best/api/v2/highfive/008.gif',
			'https://nekos.best/api/v2/highfive/009.gif',
			'https://nekos.best/api/v2/highfive/010.gif',
			'https://nekos.best/api/v2/highfive/011.gif',
			'https://nekos.best/api/v2/highfive/012.gif',
			'https://nekos.best/api/v2/highfive/013.gif',
			'https://nekos.best/api/v2/highfive/014.gif',
			'https://nekos.best/api/v2/highfive/015.gif',
			'https://nekos.best/api/v2/highfive/016.gif',
			'https://nekos.best/api/v2/highfive/017.gif',
			'https://nekos.best/api/v2/highfive/018.gif',
			'https://nekos.best/api/v2/highfive/019.gif',
			'https://nekos.best/api/v2/highfive/020.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** дал(а) пять **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'hit', description='Ударить участника.')
	async def _hit(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://i.waifu.pics/yukGfeE.gif',
			'https://i.waifu.pics/~eSaT3X.gif',
			'https://i.waifu.pics/PVm4fOI.gif',
			'https://i.waifu.pics/5S6AVgU.gif',
			'https://i.waifu.pics/fxL8rm_.gif',
			'https://i.waifu.pics/F~JEuzF.gif',
			'https://i.waifu.pics/9btNk6_.gif',
			'https://i.waifu.pics/I9DcxVn.gif',
			'https://i.waifu.pics/u9g-HyK.gif',
			'https://i.waifu.pics/O8qm8aU.gif',
			'https://i.waifu.pics/0lp0nMR.gif',
			'https://i.waifu.pics/BZ38S3s.gif',
			'https://i.waifu.pics/Qjuht_q.gif',
			'https://i.waifu.pics/ve8lHum.gif',
			'https://i.waifu.pics/I~Gkbc0.gif',
			'https://i.waifu.pics/0wrsj79.gif',
			'https://i.waifu.pics/duyVtsX.gif',
			'https://i.waifu.pics/LkaAY1h.gif',
			'https://i.waifu.pics/S~2Hqgm.gif',
			'https://i.waifu.pics/0eJi-OS.gif',
			'https://i.waifu.pics/G6Pa8ek.gif',
			'https://i.waifu.pics/~9t_55m.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** ударил(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'hug', description='Обнять участника.')
	async def _hug(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-3.gif',
			'https://acegif.com/wp-content/uploads/gif/anime-hug-38.gif',
			'https://c.tenor.com/6hwwSXEoVnkAAAAC/аниме-обнимашки.gif',
			'https://i.waifu.pics/HWhukIP.gif',
			'https://i.waifu.pics/~p7kgce.gif',
			'https://i.waifu.pics/S7HrqqC.gif',
			'https://i.waifu.pics/SdoexEO.gif',
			'https://i.waifu.pics/RM2NjNt.gif',
			'https://i.waifu.pics/_J9_Lfv.gif',
			'https://i.waifu.pics/C2_DXCM.gif',
			'https://i.waifu.pics/Y6COnB-.gif',
			'https://i.waifu.pics/VFUqk8B.gif',
			'https://i.waifu.pics/eZCLENy.gif',
			'https://i.waifu.pics/UVOaZuA.gif',
			'https://i.waifu.pics/YXY3bxv.gif',
			'https://i.waifu.pics/c7JsUDX.gif',
			'https://i.waifu.pics/Ngdh2a8.gif',
			'https://i.waifu.pics/RdiKF2f.gif',
			'https://i.waifu.pics/1fzx9SW.gif',
			'https://i.waifu.pics/hl7ZFQ2.gif',
			'https://i.waifu.pics/ztvx9hE.gif',
			'https://i.waifu.pics/jT8iHBU.gif',
			'https://i.waifu.pics/_5gCZMa.gif',
			'https://i.waifu.pics/~p7kgce.gif',
			'https://i.waifu.pics/YXY3bxv.gif',
			'https://i.waifu.pics/Id2_s-~.gif',
			'https://i.waifu.pics/JlT~_wG.gif',
			'https://i.waifu.pics/zzIKkSW.gif',
			'https://i.waifu.pics/Oh4HzqX.gif',
			'https://i.waifu.pics/mj~uAm~.gif',
			'https://i.waifu.pics/sQP_mgS.gif',
			'https://i.waifu.pics/PXfD8FU.gif',
			'https://i.waifu.pics/EYcAlMR.gif',
			'https://i.waifu.pics/Dxp5TtV.gif',
			'https://i.waifu.pics/~wgpe1b.gif',
			'https://i.waifu.pics/shkxTih.gif',
			'https://i.waifu.pics/3_7mVJQ.gif',
			'https://i.waifu.pics/EgW6S9x.gif',
			'https://i.waifu.pics/A3ljLak.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** обнял(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'kill', description='Убить участника.')
	async def _kill(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://i.waifu.pics/OByL0MA.gif',
			'https://i.waifu.pics/6Izshr4.gif',
			'https://i.waifu.pics/8uhQSdY.gif',
			'https://i.waifu.pics/hsAy9-u.gif',
			'https://i.waifu.pics/Qug33iz.gif',
			'https://i.waifu.pics/Oz4aaul.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** убил(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'kiss', description='Поцеловать участника.')
	async def _kiss(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://thumbs.gfycat.com/BestWarlikeEeve-size_restricted.gif',
			'https://c.tenor.com/pJltEFXK0noAAAAC/поцелуй.gif',
			'https://img.wattpad.com/8faff188a866269f6cfe68d676b136ebca059a4e/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f64775435645f3959576d366932513d3d2d34372e313636333033326536616632353930303339343730333836353235382e676966',
			'https://i.gifer.com/B82h.gif',
			'https://i.waifu.pics/cYQ9bDe.gif',
			'https://i.waifu.pics/3k-Ea7T.gif',
			'https://i.waifu.pics/iE6ENOO.gif',
			'https://i.waifu.pics/6ApTQ4Z.gif',
			'https://i.waifu.pics/-CgQNpM.gif',
			'https://i.waifu.pics/5K6laMC.gif',
			'https://i.waifu.pics/w2P9Awj.gif',
			'https://i.waifu.pics/InsjcaW.gif',
			'https://i.waifu.pics/DTzt9TY.gif',
			'https://i.waifu.pics/q2xa_Cx.gif',
			'https://i.waifu.pics/4Y46O9k.gif',
			'https://i.waifu.pics/s2vaEPB.gif',
			'https://i.waifu.pics/x6XaUk8.gif',
			'https://i.waifu.pics/_S~90nZ.gif',
			'https://i.waifu.pics/IIjltcS.gif',
			'https://i.waifu.pics/5ZBZIYF.gif',
			'https://i.waifu.pics/9o~tu3U.gif',
			'https://i.waifu.pics/IVHT1cf.gif',
			'https://i.waifu.pics/X_Sc6tf.gif',
			'https://i.waifu.pics/UB4ILHd.gif',
			'https://i.waifu.pics/YWhrijG.gif',
			'https://i.waifu.pics/L0F3pYp.gif',
			'https://i.waifu.pics/Nz~~57H.gif',
			'https://i.waifu.pics/_6IlQnv.gif',
			'https://i.waifu.pics/58jTTrF.gif',
			'https://i.waifu.pics/0dcpfw-.gif',
			'https://i.waifu.pics/RLEWFvd.gif',
			'https://i.waifu.pics/-H2dvsl.gif',
			'https://i.waifu.pics/~cFkADL.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** поцеловал(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'kisscheek', description='Поцеловать в щеку участника.')
	async def _kisscheek(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://c.tenor.com/etSTc3aWspcAAAAC/yuri-kiss.gif',
			'https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif',
			'https://c.tenor.com/QGBHSiS4VzsAAAAC/surprise-cheek-kiss.gif',
			'https://c.tenor.com/mBIQcqqhmMYAAAAC/yuri-kiss.gif',
			'https://c.tenor.com/h9A4bnxJys8AAAAC/cheek-kiss.gif',
			'https://c.tenor.com/JQ9jjb_JTqEAAAAC/anime-kiss.gif',
			'https://c.tenor.com/-dABEHEyU-AAAAAC/love-you-cheek-kiss.gif',
			'https://c.tenor.com/0LMxPQdFBKAAAAAC/nekopara-kiss.gif',
			'https://c.tenor.com/_vI2MlAN-EUAAAAC/anime-couple-kiss-cheek.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** поцеловал(а) в щеку **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'knees', description='Сидеть на коленях у участника.')
	async def _knees(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://media.tenor.com/images/f3187d0be9b1201b55b8a5a0c0e39b26/tenor.gif',
			'https://media.tenor.com/images/d71442c9f278d6f088e41d1fc8ecdf0f/tenor.gif',
			'https://media.tenor.com/images/7015ab0749e353533bd372ba13c34e36/tenor.gif',
			'https://media.tenor.com/images/3b8d06b3689af7196642b81517b0dd8e/tenor.gif',
			'https://media.tenor.com/images/1bea69621140d37d80669609b095f0a3/tenor.gif',
			'https://media.tenor.com/images/4c1a74b42e4b961e7aa6299c018c8c6b/tenor.gif',
			'https://media.tenor.com/images/8fc52cf63e1eed654576eed34dc9d580/tenor.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** сидит на коленях у **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'laugh', description='Смеяться.')
	async def _laugh(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/laugh/001.gif',
			'https://nekos.best/api/v2/laugh/002.gif',
			'https://nekos.best/api/v2/laugh/003.gif',
			'https://nekos.best/api/v2/laugh/004.gif',
			'https://nekos.best/api/v2/laugh/005.gif',
			'https://nekos.best/api/v2/laugh/006.gif',
			'https://nekos.best/api/v2/laugh/007.gif',
			'https://nekos.best/api/v2/laugh/008.gif',
			'https://nekos.best/api/v2/laugh/009.gif',
			'https://nekos.best/api/v2/laugh/010.gif',
			'https://nekos.best/api/v2/laugh/011.gif',
			'https://nekos.best/api/v2/laugh/012.gif',
			'https://nekos.best/api/v2/laugh/013.gif',
			'https://nekos.best/api/v2/laugh/014.gif',
			'https://nekos.best/api/v2/laugh/015.gif',
			'https://nekos.best/api/v2/laugh/016.gif',
			'https://nekos.best/api/v2/laugh/017.gif',
			'https://nekos.best/api/v2/laugh/018.gif',
			'https://nekos.best/api/v2/laugh/019.gif',
			'https://nekos.best/api/v2/laugh/020.gif',
			'https://nekos.best/api/v2/laugh/021.gif',
			'https://nekos.best/api/v2/laugh/022.gif',
			'https://nekos.best/api/v2/laugh/023.gif',
			'https://nekos.best/api/v2/laugh/024.gif',
			'https://nekos.best/api/v2/laugh/025.gif',
			'https://nekos.best/api/v2/laugh/026.gif',
			'https://nekos.best/api/v2/laugh/027.gif',
			'https://nekos.best/api/v2/laugh/028.gif',
			'https://nekos.best/api/v2/laugh/029.gif',
			'https://nekos.best/api/v2/laugh/030.gif',
			'https://nekos.best/api/v2/laugh/031.gif',
			'https://nekos.best/api/v2/laugh/032.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** смеется.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'lick', description='Облизать участника.')
	async def _lick(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://i.waifu.pics/JxQolYt.gif',
			'https://i.waifu.pics/at~DQwu.gif',
			'https://i.waifu.pics/iL8UVFd.gif',
			'https://i.waifu.pics/RIMRo9T.gif',
			'https://i.waifu.pics/p0FcuY4.gif',
			'https://i.waifu.pics/K-_RyvK.gif',
			'https://i.waifu.pics/RpQBJ5j.gif',
			'https://i.waifu.pics/LyVaHfl.gif',
			'https://i.waifu.pics/kanHQ0f.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** облизал(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'love', description='Любить участника.')
	async def _love(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://media.tenor.com/PGXshKPAUh4AAAAC/my-dress-up-darling-anime-love.gif',
			'https://media.tenor.com/2DB6eQl33-8AAAAd/anime-couple.gif',
			'https://media.tenor.com/0PIj7XctFr4AAAAC/a-whisker-away-hug.gif',
			'https://media.tenor.com/V3GQKvQjej0AAAAC/love-gif-sad.gif',
			'https://media.tenor.com/g9HjxRZM2C8AAAAd/anime-love.gif',
			'https://media.tenor.com/doc8uMAT5ssAAAAC/anime-love.gif',
			'https://media.tenor.com/EKS8EWkhZJUAAAAC/anime-anime-hug.gif',
			'https://media.tenor.com/58PKyK5xlIoAAAAC/anime.gif',
			'https://media.tenor.com/IQCyn7dd9PwAAAAC/val-ally-hug.gif',
			'https://media.tenor.com/mB_y2KUsyuoAAAAd/cuddle-anime-hug.gif',
			'https://media.tenor.com/J7eGDvGeP9IAAAAC/enage-kiss-anime-hug.gif',
			'https://media.tenor.com/1PSvBKNcNtUAAAAC/love-anime.gif',
			'https://media.tenor.com/WUZAwo5KFdMAAAAd/love-holding-hands.gif',
			'https://media.tenor.com/Q83w83J1VzUAAAAC/hug-love.gif',
			'https://media.tenor.com/QbYxVBr1p5MAAAAC/rikekoi-anime-love-kiss.gif',
			'https://media.tenor.com/_QghPjf6QH0AAAAd/anime-love.gif',
			'https://media.tenor.com/fVMPQro2eZAAAAAC/anime-kiss.gif',
			'https://media.tenor.com/NO6j5K8YuRAAAAAC/leni.gif',
			'https://media.tenor.com/jRtbBYdf0mwAAAAd/love-cute-hug-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** любит **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'lurk', description='Пытаться спрятаться.')
	async def _lurk(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://media.tenor.com/t1KZ9IeCxpEAAAAC/junkolurk.gif',
			'https://media.tenor.com/O5URZERslMgAAAAC/katarina-claes-hiding.gif',
			'https://media.tenor.com/V899AbBcjZoAAAAC/anime-lurk-paiyumi-lurk.gif',
			'https://media.tenor.com/Tbr9XIUrMdYAAAAC/anime-hide-anime-peek.gif',
			'https://media.tenor.com/JHt_Vom9RRoAAAAC/hiding-anime.gif',
			'https://media.tenor.com/4G90ufIvHccAAAAC/anime-lurk.gif',
			'https://media.tenor.com/7bMncZY3qX8AAAAd/madhouse-madhouse_eboy.gif',
			'https://media.tenor.com/VmJiPKN4r7AAAAAd/anime-vrchat.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** пытается спрятаться.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'music', description='Слушать свою любимую музыку.')
	async def _music(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://media.tenor.com/bO8WaQit_l8AAAAC/anime-music.gif',
			'https://media.tenor.com/y4xV8nATdXgAAAAC/aharen-san-aharen-san-rap.gif',
			'https://media.tenor.com/-_DwVF4yZGwAAAAC/florgifqwert.gif',
			'https://media.tenor.com/9Mm4Kd_Dr2YAAAAC/asuka-shinji.gif',
			'https://media.tenor.com/_OA-44hy1-4AAAAC/anime-music.gif',
			'https://media.tenor.com/5FmfYNNPcwQAAAAC/dance-music.gif',
			'https://media.tenor.com/4U3vb8oBqKAAAAAC/anime-headphones.gif',
			'https://media.tenor.com/Z76fFsciEhUAAAAC/anime-sensual-touch-love-anime-music.gif',
			'https://media.tenor.com/ik8b9JsAuUQAAAAd/music-ssss.gif',
			'https://media.tenor.com/1BnONnrd9soAAAAC/anime-music-phone.gif',
			'https://media.tenor.com/bYtR62v4-McAAAAC/retro-retro-disco.gif',
			'https://media.tenor.com/dN976uhxB0kAAAAC/aimoto-rinku-listening-to-music.gif',
			'https://media.tenor.com/gaxGj7lADG8AAAAC/anime-girl-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** слушает свою любимую музыку.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'panic', description='Паниковать.')
	async def _panic(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://media.tenor.com/NhD7YfCeQXMAAAAC/panic-anime.gif',
			'https://media.tenor.com/RVlKw-lkIm0AAAAC/nervous-scared.gif',
			'https://media.tenor.com/pGopKd9Rr6UAAAAC/spy-x-family-anya.gif',
			'https://media.tenor.com/gzHrqAoompkAAAAd/mnmiko-panic.gif',
			'https://media.tenor.com/ziR2x6w-rLMAAAAC/anime-panic.gif',
			'https://media.tenor.com/ynic9Fc1AEkAAAAd/kaguya-sama-maki-shijo.gif',
			'https://media.tenor.com/pSgkMXMFlrsAAAAC/panic-aochan-cant-study.gif',
			'https://media.tenor.com/Un4g4XbnUqkAAAAC/kaguya-sama-love-is-war-chika-fujiwara.gif',
			'https://media.tenor.com/bDwqOPyEI2UAAAAd/kaguya-shinomiya-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** паникует.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'pat', description='Погладить участника.')
	async def _pat(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://cdn.nekos.life/pat/pat_001.gif',
			'https://cdn.nekos.life/pat/pat_002.gif',
			'https://cdn.nekos.life/pat/pat_003.gif',
			'https://cdn.nekos.life/pat/pat_004.gif',
			'https://cdn.nekos.life/pat/pat_005.gif',
			'https://cdn.nekos.life/pat/pat_006.gif',
			'https://cdn.nekos.life/pat/pat_007.gif',
			'https://cdn.nekos.life/pat/pat_008.gif',
			'https://cdn.nekos.life/pat/pat_009.gif',
			'https://cdn.nekos.life/pat/pat_010.gif',
			'https://cdn.nekos.life/pat/pat_011.gif',
			'https://cdn.nekos.life/pat/pat_012.gif',
			'https://cdn.nekos.life/pat/pat_013.gif',
			'https://cdn.nekos.life/pat/pat_014.gif',
			'https://cdn.nekos.life/pat/pat_015.gif',
			'https://cdn.nekos.life/pat/pat_016.gif',
			'https://cdn.nekos.life/pat/pat_017.gif',
			'https://cdn.nekos.life/pat/pat_018.gif',
			'https://cdn.nekos.life/pat/pat_019.gif',
			'https://cdn.nekos.life/pat/pat_020.gif',
			'https://cdn.nekos.life/pat/pat_021.gif',
			'https://cdn.nekos.life/pat/pat_022.gif',
			'https://cdn.nekos.life/pat/pat_023.gif',
			'https://cdn.nekos.life/pat/pat_024.gif',
			'https://cdn.nekos.life/pat/pat_025.gif',
			'https://cdn.nekos.life/pat/pat_026.gif',
			'https://cdn.nekos.life/pat/pat_027.gif',
			'https://cdn.nekos.life/pat/pat_028.gif',
			'https://cdn.nekos.life/pat/pat_029.gif',
			'https://cdn.nekos.life/pat/pat_030.gif',
			'https://cdn.nekos.life/pat/pat_031.gif',
			'https://cdn.nekos.life/pat/pat_032.gif',
			'https://cdn.nekos.life/pat/pat_033.gif',
			'https://cdn.nekos.life/pat/pat_034.gif',
			'https://cdn.nekos.life/pat/pat_035.gif',
			'https://cdn.nekos.life/pat/pat_036.gif',
			'https://cdn.nekos.life/pat/pat_037.gif',
			'https://cdn.nekos.life/pat/pat_038.gif',
			'https://cdn.nekos.life/pat/pat_039.gif',
			'https://cdn.nekos.life/pat/pat_040.gif',
			'https://cdn.nekos.life/pat/pat_041.gif',
			'https://cdn.nekos.life/pat/pat_042.gif',
			'https://cdn.nekos.life/pat/pat_043.gif',
			'https://cdn.nekos.life/pat/pat_044.gif',
			'https://cdn.nekos.life/pat/pat_045.gif',
			'https://cdn.nekos.life/pat/pat_046.gif',
			'https://cdn.nekos.life/pat/pat_047.gif',
			'https://cdn.nekos.life/pat/pat_048.gif',
			'https://cdn.nekos.life/pat/pat_049.gif',
			'https://cdn.nekos.life/pat/pat_050.gif',
			'https://cdn.nekos.life/pat/pat_051.gif',
			'https://cdn.nekos.life/pat/pat_052.gif',
			'https://cdn.nekos.life/pat/pat_053.gif',
			'https://cdn.nekos.life/pat/pat_054.gif',
			'https://cdn.nekos.life/pat/pat_055.gif',
			'https://cdn.nekos.life/pat/pat_056.gif',
			'https://cdn.nekos.life/pat/pat_057.gif',
			'https://cdn.nekos.life/pat/pat_058.gif',
			'https://cdn.nekos.life/pat/pat_059.gif',
			'https://cdn.nekos.life/pat/pat_060.gif',
			'https://cdn.nekos.life/pat/pat_061.gif',
			'https://cdn.nekos.life/pat/pat_062.gif',
			'https://cdn.nekos.life/pat/pat_063.gif',
			'https://cdn.nekos.life/pat/pat_064.gif',
			'https://cdn.nekos.life/pat/pat_065.gif',
			'https://cdn.nekos.life/pat/pat_066.gif',
			'https://cdn.nekos.life/pat/pat_067.gif',
			'https://cdn.nekos.life/pat/pat_068.gif',
			'https://cdn.nekos.life/pat/pat_069.gif',
			'https://cdn.nekos.life/pat/pat_070.gif',
			'https://cdn.nekos.life/pat/pat_071.gif',
			'https://cdn.nekos.life/pat/pat_072.gif',
			'https://cdn.nekos.life/pat/pat_073.gif',
			'https://cdn.nekos.life/pat/pat_074.gif',
			'https://i.waifu.pics/I~znmj2.gif',
			'https://i.waifu.pics/vWeHXrP.gif',
			'https://i.waifu.pics/cHILIVK.gif',
			'https://i.waifu.pics/TcLUOP9.gif',
			'https://i.waifu.pics/IDQRV1N.gif',
			'https://i.waifu.pics/rOU~HpB.gif',
			'https://i.waifu.pics/Sa5NHfn.gif',
			'https://i.waifu.pics/OtdCiXp.gif',
			'https://i.waifu.pics/MqgjYTF.gif',
			'https://i.waifu.pics/UQ~PSLN.gif',
			'https://i.waifu.pics/idPxli-.gif',
			'https://i.waifu.pics/0x-pKQY.gif',
			'https://i.waifu.pics/PAoNo~Z.gif',
			'https://i.waifu.pics/vAcG_hT.gif',
			'https://i.waifu.pics/3vtet9Z.gif',
			'https://i.waifu.pics/nsvdMrv.gif',
			'https://i.waifu.pics/nsvdMrv.gif',
			'https://i.waifu.pics/vWeHXrP.gif',
			'https://i.waifu.pics/rA_peKb.gif',
			'https://i.waifu.pics/4z7nzIy.gif',
			'https://i.waifu.pics/fyGPXe_.gif',
			'https://i.waifu.pics/HANUasC.gif',
			'https://i.waifu.pics/s7ee7AI.gif',
			'https://i.waifu.pics/MGSjX0_.gif',
			'https://i.waifu.pics/GK2-wHv.gif',
			'https://i.waifu.pics/678OYtu.gif',
			'https://i.waifu.pics/kSE4Ypd.gif',
			'https://i.waifu.pics/esNCuKp.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** погладил(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'poke', description='Тыкнуть участника.')
	async def _poke(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://i.waifu.pics/5du1H~U.gif',
			'https://i.waifu.pics/1YxdKac.gif',
			'https://i.waifu.pics/8OpJmQ1.gif',
			'https://i.waifu.pics/ff7LRWR.gif',
			'https://i.waifu.pics/s446j9L.gif',
			'https://i.waifu.pics/tqhmLSK.gif',
			'https://i.waifu.pics/xfIn2c8.gif',
			'https://i.waifu.pics/GX_5XBb.gif',
			'https://i.waifu.pics/SkfA6gM.gif',
			'https://i.waifu.pics/ZNu8L4F.gif',
			'https://i.waifu.pics/A4SyFip.gif',
			'https://i.waifu.pics/kO_~ywd.gif',
			'https://i.waifu.pics/5tc8WuP.gif',
			'https://i.waifu.pics/9KOZvNA.gif',
			'https://i.waifu.pics/v-9VxXU.gif',
			'https://i.waifu.pics/Yf8glJM.gif',
			'https://i.waifu.pics/DWmZwNP.gif',
			'https://i.waifu.pics/cyHeaeY.gif',
			'https://i.waifu.pics/Yu8QR7N.gif',
			'https://i.waifu.pics/JlDu4xg.gif',
			'https://i.waifu.pics/jWRdbHV.jpg',
			'https://i.waifu.pics/beT0l4e.gif',
			'https://i.waifu.pics/hOM9tLO.gif',
			'https://i.waifu.pics/ZXMLQBn.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** тыкнул(а) в **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'pout', description='Дуться на участника.')
	async def _pout(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://media.tenor.com/iNu8LXx2ECgAAAAC/senko-poute-hmph.gif',
			'https://media.tenor.com/4tXvn7g292oAAAAC/shikimoris-not-just-cute-shikimori.gif',
			'https://media.tenor.com/hR8XdCeC2psAAAAC/cute-pouting.gif',
			'https://media.tenor.com/yCR6JOoxS6wAAAAd/anime-angry.gif',
			'https://media.tenor.com/03VCLMyKfL4AAAAC/pout-anime-pout.gif',
			'https://media.tenor.com/wtSs_VCHYmEAAAAC/noela-angry.gif',
			'https://media.tenor.com/3EgO4ozQzp4AAAAC/anime-raphtalia.gif',
			'https://media.tenor.com/Up7hRFmFY9AAAAAd/anime-sad-anime-pout.gif',
			'https://media.tenor.com/qpzuTRtY0pYAAAAd/wataten-watashi-ni-tenshi-ga-maiorita.gif',
			'https://media.tenor.com/bqdATAYxLd4AAAAC/senpai-hachioji-naoto.gif',
			'https://media.tenor.com/MH-k-cCCirwAAAAC/vtuber-foxplushy.gif',
			'https://media.tenor.com/wNGKIj1GvaMAAAAd/karyl-kyaru.gif',
			'https://media.tenor.com/L2eobON0t84AAAAC/anime-pout.gif',
			'https://media.tenor.com/cWxPBSDYndgAAAAd/shikimori-shikimoris-not-just-cute.gif',
			'https://media.tenor.com/s5MLRsiWGSYAAAAd/girl-kitagawa.gif',
			'https://media.tenor.com/VidlGXLXk3gAAAAC/anime-girl.gif',
			'https://media.tenor.com/4IOr7C2BdbMAAAAd/kitagawa-kitagawa-marin.gif',
			'https://media.tenor.com/ldU51iXobP4AAAAC/ameri-azazel-ameri.gif',
			'https://media.tenor.com/qk93vQUrYWsAAAAC/anime-blush.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** дуется на **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'raise', description='Взять участника на руки.')
	async def _raise(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://c.tenor.com/6NtMGzdTIC8AAAAC/picking-up.gif',
			'https://c.tenor.com/W4Voi07VHcsAAAAC/anime-josee.gif',
			'https://c.tenor.com/sSsxDoFXdj0AAAAC/anime-girl.gif',
			'https://c.tenor.com/SvOmKXm9RN8AAAAC/miyano-pick-up.gif',
			'https://c.tenor.com/H38F447xwxEAAAAC/servamp-pick-up.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** взял(а) на руки **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'scare', description='Напугать участника.')
	async def _scare(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://media.tenor.com/pGopKd9Rr6UAAAAC/spy-x-family-anya.gif',
			'https://media.tenor.com/RhyxCbENd6YAAAAC/umaru-chan-scared.gif',
			'https://media.tenor.com/ndt-tUES-qAAAAAC/my-dress-up-darling-anime-scared.gif',
			'https://media.tenor.com/oDaR_1ydefIAAAAC/scared-anime.gif',
			'https://media.tenor.com/wWmjeJgcFr4AAAAC/nervous-anime.gif',
			'https://media.tenor.com/zaA5Pjj5uLEAAAAC/what-anime.gif',
			'https://media.tenor.com/-JR_teNMOXEAAAAC/ijiranaide-nagatoro-nagataro.gif',
			'https://media.tenor.com/WcxwXmB-YiIAAAAC/anime-pillow.gif',
			'https://media.tenor.com/ooWeeqeK6pMAAAAC/scared-shiver.gif',
			'https://media.tenor.com/iSnMzt3ZtmQAAAAd/anime-love-after-world-domination.gif',
			'https://media.tenor.com/J0pSGU_uzTAAAAAC/scared-anime.gif',
			'https://media.tenor.com/rHmAe09OWBQAAAAC/anime-scared.gif',
			'https://media.tenor.com/Y009LewGjowAAAAC/isekai-quartet-aqua.gif',
			'https://media.tenor.com/GnqphCoc8zEAAAAC/anime-baby.gif',
			'https://media.tenor.com/FNqZHylgNicAAAAC/mushoku-tensei-anime.gif',
			'https://media.tenor.com/j04Be3CZDFUAAAAd/komi-scared.gif',
			'https://media.tenor.com/k-20hdZMXZcAAAAC/scared-anime.gif',
			'https://media.tenor.com/OPw0QTGMU8QAAAAd/heroines-anime-heroines-run-the-show.gif',
			'https://media.tenor.com/TffcsLG7VAYAAAAd/slow-loop-anime-blush.gif',
			'https://media.tenor.com/Qtxx5a7UiFAAAAAd/sushichaeng-anime-reaction.gif',
			'https://media.tenor.com/pN95aMcZsQ0AAAAC/vanitas-vanitas-no-carte.gif',
			'https://media.tenor.com/jCpVtnxjkYIAAAAC/killua-scared.gif',
			'https://media.tenor.com/Rh_FNuFbtQ4AAAAC/anime-princess-connect.gif',
			'https://media.tenor.com/GeisCcWiTU4AAAAC/rin-shima-terrified.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** напугал(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'shoot', description='Стрелять в участника.')
	async def _shoot(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://media.tenor.com/CLfZB6_HcoYAAAAC/anime-mirai.gif',
			'https://media.tenor.com/gQkJLMcaZiIAAAAd/anime-gun.gif',
			'https://media.tenor.com/Am61DGzxpGoAAAAC/anime-laughing.gif',
			'https://media.tenor.com/RdfB0I6L0FIAAAAC/anime-triela.gif',
			'https://media.tenor.com/Vja2MkojIgsAAAAC/anime-gun.gif',
			'https://media.tenor.com/guXgm-Ie55wAAAAC/anime-gun.gif',
			'https://media.tenor.com/-4iB5H1jnL4AAAAC/teppen-anime-shoot.gif',
			'https://media.tenor.com/iMtcqbBzc5sAAAAC/anime-shooting.gif',
			'https://media.tenor.com/_vp7KTrr4WMAAAAC/karma-akabane-anime.gif',
			'https://media.tenor.com/y0W3bmFYQMsAAAAC/gun-anime.gif',
			'https://media.tenor.com/qigZamts4wAAAAAC/saber-anime.gif',
			'https://media.tenor.com/C3dIGhDlBF8AAAAC/anime-gun-x-box.gif',
			'https://media.tenor.com/LIELXkY5vCAAAAAC/anime-gun.gif',
			'https://media.tenor.com/0XYRdBVKZQgAAAAC/anime-finger-gun.gif',
			'https://media.tenor.com/f2aJEoV95rMAAAAC/anime-shot.gif',
			'https://media.tenor.com/Pq3EQbsynG8AAAAd/fire-power.gif',
			'https://media.tenor.com/VqW-j6TouUMAAAAC/akechi-water-gun.gif',
			'https://media.tenor.com/9xF9nWcq-6AAAAAC/shoot-pow.gif',
			'https://media.tenor.com/8yAPBe4IHaAAAAAd/hilda-stella-glow.gif',
			'https://media.tenor.com/jGTWpl871jEAAAAC/nichijou-gatlinggun.gif',
			'https://media.tenor.com/pyMCwqm1pVEAAAAC/bleach-kurosaki-ichigo.gif',
			'https://media.tenor.com/5ZlP12pXBGQAAAAC/shoot-anime.gif',
			'https://media.tenor.com/FJoZJt6BcAIAAAAC/anime-in-the-feels.gif',
			'https://media.tenor.com/ANfWGCi3gV0AAAAC/majima-lycoris-recoil.gif',
			'https://media.tenor.com/3Gxw4JNPlnsAAAAC/hi-score-girl-shoot.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** стреляет в **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'shrug', description='Пожимать плечами.')
	async def _shrug(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/zb9WDwe-lMYAAAAd/yuigahama-yui.gif',
			'https://media.tenor.com/0GOwPHgcUj0AAAAC/anime-shrug.gif',
			'https://media.tenor.com/ZaxUeXcUtDkAAAAd/shrug-smug.gif',
			'https://media.tenor.com/F6ekeSqr9OsAAAAd/renge-shrug.gif',
			'https://media.tenor.com/U06tekgz-OQAAAAd/city-hunter-ryo-saeba.gif',
			'https://media.tenor.com/YdK9JDmImKUAAAAC/senyuu-anime.gif',
			'https://media.tenor.com/nlSDG33ptOoAAAAC/geto-suguru.gif',
			'https://media.tenor.com/TMczSTtaXxgAAAAC/naruto-kakashi.gif',
			'https://media.tenor.com/SxvUPdLQfrgAAAAC/uzaki-chan-uzaki.gif',
			'https://media.tenor.com/1MuoFDWKpZAAAAAC/shrug-jakethedog.gif',
			'https://media.tenor.com/ZS4tAPRPQ6EAAAAd/anime-anime-girl.gif',
			'https://media.tenor.com/GR9ILf06D4MAAAAC/woah-sorry.gif',
			'https://media.tenor.com/-f4M0nxR048AAAAC/dont-hurt-me-my-healer-anime-shrug.gif',
			'https://media.tenor.com/eqOgEfMrNLoAAAAC/akudama-drive-hacker.gif',
			'https://media.tenor.com/LvU6efscTfcAAAAC/shrug.gif',
			'https://media.tenor.com/XAdtlGThtf0AAAAC/obi-idk.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** пожал(а) плечами.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'slap', description='Дать пощечину участнику.')
	async def _slap(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://cdn.nekos.life/slap/slap_001.gif',
			'https://cdn.nekos.life/slap/slap_002.gif',
			'https://cdn.nekos.life/slap/slap_003.gif',
			'https://cdn.nekos.life/slap/slap_004.gif',
			'https://cdn.nekos.life/slap/slap_005.gif',
			'https://cdn.nekos.life/slap/slap_006.gif',
			'https://cdn.nekos.life/slap/slap_007.gif',
			'https://cdn.nekos.life/slap/slap_008.gif',
			'https://cdn.nekos.life/slap/slap_009.gif',
			'https://cdn.nekos.life/slap/slap_010.gif',
			'https://cdn.nekos.life/slap/slap_011.gif',
			'https://cdn.nekos.life/slap/slap_012.gif',
			'https://cdn.nekos.life/slap/slap_013.gif',
			'https://cdn.nekos.life/slap/slap_014.gif',
			'https://cdn.nekos.life/slap/slap_015.gif',
			'https://cdn.nekos.life/slap/slap_016.gif',
			'https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif',
			'https://i.pinimg.com/originals/68/de/67/68de679cc20000570e8a7d9ed9218cd3.gif',
			'https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif',
			'https://c.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif',
			'https://i.waifu.pics/zFe9vib.gif',
			'https://i.waifu.pics/vX9nrsn.gif',
			'https://i.waifu.pics/mXj8i8S.gif',
			'https://i.waifu.pics/6-_UTFD.gif',
			'https://i.waifu.pics/cvKQqp-.gif',
			'https://i.waifu.pics/gsskphB.gif',
			'https://i.waifu.pics/CJRHy2-.gif',
			'https://i.waifu.pics/puI2pTf.gif',
			'https://i.waifu.pics/JOKXwLd.gif',
			'https://i.waifu.pics/Q9-IX~O.gif',
			'https://i.waifu.pics/s~CLnmA.gif',
			'https://i.waifu.pics/zU38OkI.jpg',
			'https://i.waifu.pics/52OhdHw.gif',
			'https://i.waifu.pics/QFGN4vE.gif',
			'https://i.waifu.pics/28V06Sq.gif',
			'https://i.waifu.pics/VPwmf~k.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** дал(а) пощечину **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'sleep', description='Спать.')
	async def _sleep(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/sleep/001.gif',
			'https://nekos.best/api/v2/sleep/002.gif',
			'https://nekos.best/api/v2/sleep/003.gif',
			'https://nekos.best/api/v2/sleep/004.gif',
			'https://nekos.best/api/v2/sleep/005.gif',
			'https://nekos.best/api/v2/sleep/006.gif',
			'https://nekos.best/api/v2/sleep/007.gif',
			'https://nekos.best/api/v2/sleep/008.gif',
			'https://nekos.best/api/v2/sleep/009.gif',
			'https://nekos.best/api/v2/sleep/010.gif',
			'https://nekos.best/api/v2/sleep/011.gif',
			'https://nekos.best/api/v2/sleep/012.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** спит.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'smile', description='Улыбаться.')
	async def _smile(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/smile/001.gif',
			'https://nekos.best/api/v2/smile/002.gif',
			'https://nekos.best/api/v2/smile/003.gif',
			'https://nekos.best/api/v2/smile/004.gif',
			'https://nekos.best/api/v2/smile/005.gif',
			'https://nekos.best/api/v2/smile/006.gif',
			'https://nekos.best/api/v2/smile/007.gif',
			'https://nekos.best/api/v2/smile/008.gif',
			'https://nekos.best/api/v2/smile/009.gif',
			'https://nekos.best/api/v2/smile/010.gif',
			'https://nekos.best/api/v2/smile/011.gif',
			'https://nekos.best/api/v2/smile/012.gif',
			'https://nekos.best/api/v2/smile/013.gif',
			'https://nekos.best/api/v2/smile/014.gif',
			'https://nekos.best/api/v2/smile/015.gif',
			'https://nekos.best/api/v2/smile/016.gif',
			'https://nekos.best/api/v2/smile/017.gif',
			'https://nekos.best/api/v2/smile/018.gif',
			'https://nekos.best/api/v2/smile/019.gif',
			'https://nekos.best/api/v2/smile/020.gif',
			'https://nekos.best/api/v2/smile/021.gif',
			'https://nekos.best/api/v2/smile/022.gif',
			'https://nekos.best/api/v2/smile/023.gif',
			'https://i.waifu.pics/7-IijAs.gif',
			'https://i.waifu.pics/WMsGAJX.gif',
			'https://i.waifu.pics/HxbnbPv.gif',
			'https://i.waifu.pics/zSHfe_p.gif',
			'https://i.waifu.pics/Kd0~WdT.gif',
			'https://i.waifu.pics/wSJHUmH.gif',
			'https://i.waifu.pics/x6Z7OdU.gif',
			'https://i.waifu.pics/gOFPmr4.gif',
			'https://i.waifu.pics/YSXDI2N.gif',
			'https://i.waifu.pics/606vZkF.gif',
			'https://i.waifu.pics/gGX~reJ.gif',
			'https://i.waifu.pics/nET606g.gif',
			'https://i.waifu.pics/pRC1t7C.gif',
			'https://i.waifu.pics/Eh5rPXy.gif',
			'https://i.waifu.pics/A~JTaYZ.gif',
			'https://i.waifu.pics/Eh5rPXy.gif',
			'https://i.waifu.pics/WlgtakZ.gif',
			'https://i.waifu.pics/xkSIwtZ.gif',
			'https://i.waifu.pics/JHv38Cd.gif',
			'https://i.waifu.pics/Mzyrw_f.gif',
			'https://i.waifu.pics/xyuju7Q.gif',
			'https://i.waifu.pics/73ri7VG.gif',
			'https://i.waifu.pics/Uvqo6Mz.gif',
			'https://i.waifu.pics/ozIc0J9.gif',
			'https://i.waifu.pics/u8drjx7.gif',
			'https://i.waifu.pics/MGiBjN-.gif',
			'https://i.waifu.pics/Ix3HkVJ.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** улыбнулся(ась).", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'smoke', description='Курить.')
	async def _smoke(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/YCQu4tfHd1sAAAAC/anime-retro-anime.gif',
			'https://media.tenor.com/images/e83cf3d01335d3126d189b9b9836b55e/tenor.gif',
			'https://c.tenor.com/NwaHqdSbYusAAAAC/sekaiichi-hatsukoi-anime.gif',
			'https://media.tenor.com/images/272b0260b241a2977ff5b7e36c35d7d9/tenor.gif',
			'https://c.tenor.com/ZQ5Loe2l6X4AAAAd/anime-smoke.gif',
			'https://c.tenor.com/zlH-V5mnn2sAAAAd/smoke.gif',
			'https://c.tenor.com/Wzi49q_0pI4AAAAC/brook-chill.gif',
			'https://c.tenor.com/jtsbdCBXD-YAAAAd/anime-hair-wind.gif',
			'https://c.tenor.com/zmMWDXNqQBYAAAAC/tsukikochai-anime-cig.gif',
			'https://c.tenor.com/HqerwyiKpwwAAAAC/aki-csm.gif',
			'https://media.tenor.com/images/b5e2f6755fb9d887d68e71ed4e8ecc4e/tenor.gif',
			'https://media.tenor.com/images/e7c05ea75a71182f966f3d9a5aa1574d/tenor.gif',
			'https://media.tenor.com/images/3d0d9744c192ff7d905a863d0ef335ae/tenor.gif',
			'https://c.tenor.com/RsFj4O1goJkAAAAC/smoking-smoke.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** курит.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'smug', description='Выглядить самодовольно.')
	async def _smug(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://cdn.nekos.life/smug/smug_001.gif',
			'https://cdn.nekos.life/smug/smug_002.gif',
			'https://cdn.nekos.life/smug/smug_003.gif',
			'https://cdn.nekos.life/smug/smug_004.gif',
			'https://cdn.nekos.life/smug/smug_005.gif',
			'https://cdn.nekos.life/smug/smug_006.gif',
			'https://cdn.nekos.life/smug/smug_007.gif',
			'https://cdn.nekos.life/smug/smug_009.gif',
			'https://cdn.nekos.life/smug/smug_010.gif',
			'https://cdn.nekos.life/smug/smug_011.gif',
			'https://cdn.nekos.life/smug/smug_012.gif',
			'https://cdn.nekos.life/smug/smug_013.gif',
			'https://cdn.nekos.life/smug/smug_014.gif',
			'https://cdn.nekos.life/smug/smug_015.gif',
			'https://cdn.nekos.life/smug/smug_016.gif',
			'https://cdn.nekos.life/smug/smug_017.gif',
			'https://cdn.nekos.life/smug/smug_018.gif',
			'https://cdn.nekos.life/smug/smug_019.gif',
			'https://cdn.nekos.life/smug/smug_021.gif',
			'https://cdn.nekos.life/smug/smug_022.gif',
			'https://cdn.nekos.life/smug/smug_023.gif',
			'https://cdn.nekos.life/smug/smug_024.gif',
			'https://cdn.nekos.life/smug/smug_025.gif',
			'https://cdn.nekos.life/smug/smug_026.gif',
			'https://cdn.nekos.life/smug/smug_027.gif',
			'https://cdn.nekos.life/smug/smug_028.gif',
			'https://cdn.nekos.life/smug/smug_029.gif',
			'https://cdn.nekos.life/smug/smug_030.gif',
			'https://cdn.nekos.life/smug/smug_031.gif',
			'https://cdn.nekos.life/smug/smug_032.gif',
			'https://cdn.nekos.life/smug/smug_033.gif',
			'https://cdn.nekos.life/smug/smug_034.gif',
			'https://cdn.nekos.life/smug/smug_035.gif',
			'https://cdn.nekos.life/smug/smug_036.gif',
			'https://cdn.nekos.life/smug/smug_037.gif',
			'https://cdn.nekos.life/smug/smug_038.gif',
			'https://cdn.nekos.life/smug/smug_039.gif',
			'https://cdn.nekos.life/smug/smug_040.gif',
			'https://cdn.nekos.life/smug/smug_041.gif',
			'https://cdn.nekos.life/smug/smug_042.gif',
			'https://cdn.nekos.life/smug/smug_043.gif',
			'https://cdn.nekos.life/smug/smug_044.gif',
			'https://cdn.nekos.life/smug/smug_045.gif',
			'https://cdn.nekos.life/smug/smug_046.gif',
			'https://cdn.nekos.life/smug/smug_047.gif',
			'https://cdn.nekos.life/smug/smug_048.gif',
			'https://cdn.nekos.life/smug/smug_049.gif',
			'https://cdn.nekos.life/smug/smug_050.gif',
			'https://cdn.nekos.life/smug/smug_051.gif',
			'https://cdn.nekos.life/smug/smug_052.gif',
			'https://cdn.nekos.life/smug/smug_053.gif',
			'https://cdn.nekos.life/smug/smug_054.gif',
			'https://cdn.nekos.life/smug/smug_055.gif',
			'https://cdn.nekos.life/smug/smug_056.gif',
			'https://cdn.nekos.life/smug/smug_057.gif',
			'https://cdn.nekos.life/smug/smug_058.gif',
			'https://cdn.nekos.life/smug/smug_059.gif',
			'https://i.waifu.pics/atydFSL.gif',
			'https://i.waifu.pics/8Py2vAi.gif',
			'https://i.waifu.pics/54lZVFx.gif',
			'https://i.waifu.pics/Wf2wxtM.gif',
			'https://i.waifu.pics/TavGjAi.gif',
			'https://i.waifu.pics/I3ZnurL.gif',
			'https://i.waifu.pics/V-vCX34.gif',
			'https://i.waifu.pics/i~xb7c2.gif',
			'https://i.waifu.pics/TpHg_I3.gif',
			'https://i.waifu.pics/djTUASr.gif',
			'https://i.waifu.pics/hEHBgzb.gif',
			'https://i.waifu.pics/p76dKMM.gif',
			'https://i.waifu.pics/djTUASr.gif',
			'https://i.waifu.pics/icBplLR.gif',
			'https://i.waifu.pics/175w1G-.gif',
			'https://i.waifu.pics/SQMCRFn.gif',
			'https://i.waifu.pics/Jp8Eg_o.gif',
			'https://i.waifu.pics/PRXwZXJ.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** выглядит самодовольно.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'takehand', description='Взять участника на руки.')
	async def _takehand(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://c.tenor.com/o672iHxCWngAAAAC/thankyou-mr-take-my-hand.gif',
			'https://c.tenor.com/IPrG0Zl0ktAAAAAC/hands-hand.gif',
			'https://c.tenor.com/8SS414qnk70AAAAd/hayase-nagatoro-x-hachioji-naoto-hayase-nagatoro.gif',
			'https://c.tenor.com/_TtNJsBXkOAAAAAC/noragami-anime.gif',
			'https://c.tenor.com/pqve83ZQ8d8AAAAC/anime-shida-kuroha.gif',
			'https://c.tenor.com/5loUs7FfC80AAAAC/vanitas-no-carte-vanitas.gif',
			'https://c.tenor.com/rU3xZo2_jaIAAAAC/anime-hold.gif',
			'https://c.tenor.com/7d5gxoNZTQYAAAAC/hold-hands-holding-hands.gif',
			'https://c.tenor.com/wC3hJXbQtYMAAAAd/touch-hands.gif',
			'https://c.tenor.com/LIkJArfAgQIAAAAd/holding-hands-lewd.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** взял(а) за руку **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'tea', description='Пить чай.')
	async def _tea(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://c.tenor.com/KnWv5CsCILQAAAAC/tea-anime.gif',
			'https://c.tenor.com/kTG1SkG6LPoAAAAC/anime-gif-anime.gif',
			'https://c.tenor.com/RfqmJ8SKdHMAAAAC/hyouka-anime.gif',
			'https://c.tenor.com/Nn4ydcdsdbEAAAAC/manga-rascal-does-not-dream-of-bunny-girl-senpai.gif',
			'https://c.tenor.com/lFgNDWZT7fkAAAAd/fox-anime.gif',
			'https://c.tenor.com/q-eQ3zpUxx0AAAAC/tea-drink.gif',
			'https://c.tenor.com/jWbFWAuohTkAAAAC/noblesse-raivi.gif',
			'https://c.tenor.com/RJ9qC27CvCEAAAAC/giorno-tea.gif',
			'https://c.tenor.com/ENTKSiTMXWoAAAAC/tea-time.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** пьет чай.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'think', description='Думать о чем-то.')
	async def _think(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://nekos.best/api/v2/think/001.gif',
			'https://nekos.best/api/v2/think/002.gif',
			'https://nekos.best/api/v2/think/003.gif',
			'https://nekos.best/api/v2/think/004.gif',
			'https://nekos.best/api/v2/think/005.gif',
			'https://nekos.best/api/v2/think/006.gif',
			'https://nekos.best/api/v2/think/007.gif',
			'https://nekos.best/api/v2/think/008.gif',
			'https://nekos.best/api/v2/think/009.gif',
			'https://nekos.best/api/v2/think/010.gif',
			'https://nekos.best/api/v2/think/011.gif',
			'https://nekos.best/api/v2/think/012.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** о чем-то думает.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'tickle', description='Щекотать участника.')
	async def _tickle(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://cdn.nekos.life/tickle/tickle_001.gif',
			'https://cdn.nekos.life/tickle/tickle_002.gif',
			'https://cdn.nekos.life/tickle/tickle_003.gif',
			'https://cdn.nekos.life/tickle/tickle_004.gif',
			'https://cdn.nekos.life/tickle/tickle_005.gif',
			'https://cdn.nekos.life/tickle/tickle_006.gif',
			'https://cdn.nekos.life/tickle/tickle_007.gif',
			'https://cdn.nekos.life/tickle/tickle_008.gif',
			'https://cdn.nekos.life/tickle/tickle_009.gif',
			'https://cdn.nekos.life/tickle/tickle_010.gif',
			'https://cdn.nekos.life/tickle/tickle_011.gif',
			'https://cdn.nekos.life/tickle/tickle_012.gif',
			'https://cdn.nekos.life/tickle/tickle_013.gif',
			'https://cdn.nekos.life/tickle/tickle_014.gif',
			'https://cdn.nekos.life/tickle/tickle_015.gif',
			'https://cdn.nekos.life/tickle/tickle_016.gif',
			'https://cdn.nekos.life/tickle/tickle_017.gif',
			'https://cdn.nekos.life/tickle/tickle_018.gif',
			'https://cdn.nekos.life/tickle/tickle_019.gif',
			'https://cdn.nekos.life/tickle/tickle_020.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** щекочет **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)		

	@bridge.bridge_command(name = 'tie', description='Связать участника.')
	async def _tie(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://c.tenor.com/uYnS4Id7KmQAAAAC/haibara-ai-ai-struggles-tied-down.gif',
			'https://c.tenor.com/IKKTWinKUuwAAAAC/kishirika-kishirisu-kishirika.gif',
			'https://c.tenor.com/EawRHVGUtkkAAAAC/makenki-anime.gif',
			'https://c.tenor.com/CD8gvywKExQAAAAC/stocking-tied-up.gif',
			'https://c.tenor.com/RYo1Fdpb6aIAAAAC/girly-air-force-anime.gif',
			'https://c.tenor.com/4E1cWfNnwwgAAAAC/littlebitofab-bondage.gif',
			'https://c.tenor.com/F24yKxQOwEsAAAAC/cowboy-bebop-anime.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** связал(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'wave', description='Поприветствовать участника.')
	async def _wave(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://nekos.best/api/v2/wave/001.gif',
			'https://nekos.best/api/v2/wave/002.gif',
			'https://nekos.best/api/v2/wave/003.gif',
			'https://nekos.best/api/v2/wave/004.gif',
			'https://nekos.best/api/v2/wave/005.gif',
			'https://nekos.best/api/v2/wave/006.gif',
			'https://nekos.best/api/v2/wave/007.gif',
			'https://nekos.best/api/v2/wave/008.gif',
			'https://nekos.best/api/v2/wave/009.gif',
			'https://nekos.best/api/v2/wave/010.gif',
			'https://nekos.best/api/v2/wave/011.gif',
			'https://nekos.best/api/v2/wave/012.gif',
			'https://nekos.best/api/v2/wave/013.gif',
			'https://nekos.best/api/v2/wave/014.gif',
			'https://nekos.best/api/v2/wave/015.gif',
			'https://nekos.best/api/v2/wave/016.gif',
			'https://nekos.best/api/v2/wave/017.gif',
			'https://nekos.best/api/v2/wave/018.gif',
			'https://nekos.best/api/v2/wave/019.gif',
			'https://nekos.best/api/v2/wave/020.gif',
			'https://nekos.best/api/v2/wave/021.gif',
			'https://nekos.best/api/v2/wave/022.gif',
			'https://nekos.best/api/v2/wave/023.gif',
			'https://nekos.best/api/v2/wave/024.gif',
			'https://nekos.best/api/v2/wave/025.gif',
			'https://nekos.best/api/v2/wave/026.gif',
			'https://nekos.best/api/v2/wave/027.gif',
			'https://nekos.best/api/v2/wave/028.gif',
			'https://i.waifu.pics/HeeBaFc.gif',
			'https://i.waifu.pics/s3G5xJ0.gif',
			'https://i.waifu.pics/x3CjjOx.gif',
			'https://i.waifu.pics/SNR4nf5.gif',
			'https://i.waifu.pics/gwNlL3Q.gif',
			'https://i.waifu.pics/iC7niFP.gif',
			'https://i.waifu.pics/Jvi3~TN.gif',
			'https://i.waifu.pics/l3_ObDa.gif',
			'https://i.waifu.pics/aFDHylw.gif',
			'https://i.waifu.pics/aSLVz3i.gif',
			'https://i.waifu.pics/42DWO_8.gif',
			'https://i.waifu.pics/8npsaf-.gif',
			'https://i.waifu.pics/T0gfAdU.gif',
			'https://i.waifu.pics/jFOkv3O.gif',
			'https://i.waifu.pics/hjxDDMl.gif',
			'https://i.waifu.pics/ZOkB2_x.gif',
			'https://i.waifu.pics/546M14t.gif',
			'https://i.waifu.pics/0omhd79.gif',
			'https://i.waifu.pics/wyVFEi7.gif',
			'https://i.waifu.pics/iC7niFP.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** приветствует **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'wink', description='Подмигнуть участнику.')
	async def _wink(self, ctx, user: discord.Member):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		if user.bot:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать с ботами!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed=emb)

		elif user == ctx.author:
			emb = discord.Embed(description = f'**{ctx.author.name}**, нельзя взаимодействовать самому с собой!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			return await ctx.respond(embed = emb)

		responses = [
			'https://nekos.best/api/v2/wink/001.gif',
			'https://nekos.best/api/v2/wink/002.gif',
			'https://nekos.best/api/v2/wink/003.gif',
			'https://nekos.best/api/v2/wink/004.gif',
			'https://nekos.best/api/v2/wink/005.gif',
			'https://nekos.best/api/v2/wink/006.gif',
			'https://nekos.best/api/v2/wink/007.gif',
			'https://nekos.best/api/v2/wink/008.gif',
			'https://nekos.best/api/v2/wink/009.gif',
			'https://nekos.best/api/v2/wink/010.gif',
			'https://nekos.best/api/v2/wink/011.gif',
			'https://nekos.best/api/v2/wink/012.gif',
			'https://nekos.best/api/v2/wink/013.gif',
			'https://nekos.best/api/v2/wink/014.gif',
			'https://nekos.best/api/v2/wink/015.gif',
			'https://i.waifu.pics/VubRXkz.gif',
			'https://i.waifu.pics/y1E0H4g.gif',
			'https://i.waifu.pics/nzANAzh.gif',
			'https://i.waifu.pics/89e5HJK.gif',
			'https://i.waifu.pics/Tuh4Z2Q.gif',
			'https://i.waifu.pics/AS1~o21.gif',
			'https://i.waifu.pics/QmF2rf1.gif',
			'https://i.waifu.pics/yhPnXdH.gif',
			'https://i.waifu.pics/z2njfIf.gif',
			'https://i.waifu.pics/B9UEKY0.gif',
			'https://i.waifu.pics/iUewj~j.gif',
			'https://i.waifu.pics/s9KFBG~.gif',
			'https://i.waifu.pics/u9JAhmm.gif',
			'https://i.waifu.pics/t2IcbQK.gif',
			'https://i.waifu.pics/YVzEB_9.gif',
			'https://i.waifu.pics/qkceCJZ.gif',
			'https://i.waifu.pics/87KteDJ.gif',
			'https://i.waifu.pics/zFUMzUA.gif',
			'https://i.waifu.pics/ydw2e2U.gif',
			'https://i.waifu.pics/gHupS2L.gif',
			'https://i.waifu.pics/B9UEKY0.gif',
			'https://i.waifu.pics/seTjpRc.gif',
			'https://i.waifu.pics/Ah627bv.gif',
			'https://i.waifu.pics/q_eUlBV.gif',
			'https://i.waifu.pics/RP~1Qta.gif',
			'https://i.waifu.pics/tJGXND7.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** подмигнул(а) **{user.name}**.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)

	@bridge.bridge_command(name = 'yawn', description='Зевать.')
	async def _yawn(self, ctx):

		error = bot.get_emoji(ERROR_EMOJI)

		await ctx.trigger_typing()

		responses = [
			'https://media.tenor.com/images/0806130ea6389b76a397655d30833777/tenor.gif',
			'https://media.tenor.com/images/5af92174cdea45848e23841a4c297d7f/tenor.gif',
			'https://media.tenor.com/images/1df48a2d012ca195de0db0e0c2568d0b/tenor.gif',
			'https://media.tenor.com/images/9cef52ce27ab97e0fa9cfac1cdc1007f/tenor.gif',
			'https://media.tenor.com/images/2aa5ab79e635a1d22411e8313096908f/tenor.gif',
			'https://media.tenor.com/images/31e1a6251f50be85aa44057381866dee/tenor.gif',
			'https://media.tenor.com/images/17103fcd5c57229a7d944ada98bf7f45/tenor.gif',
			'https://media.tenor.com/images/f6183a194fbc50f157a4bece416168bc/tenor.gif',
			'https://media.tenor.com/images/530f7c16095c75b1ff045bec52c741e0/tenor.gif',
			'https://media.tenor.com/images/635652899cdf482a20b3bfe76c6810f3/tenor.gif',
			'https://media.tenor.com/images/d7176899990b3be56b89cbd76d4f6b49/tenor.gif'
		]

		response = random.choice(responses)

		embed = discord.Embed(description=f"**{ctx.author.name}** зевает.", colour=EMBED_COLOUR_SUCCESS)
		embed.set_image(url=response)
		await ctx.respond(embed=embed)		

	@_bite.error
	async def bite_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`bite [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`bite @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_cuddle.error
	async def cuddle_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`cuddle [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`cuddle @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_feed.error
	async def feed_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`feed [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`feed @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_fight.error
	async def fight_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`fight [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`fight @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_highfive.error
	async def highfive_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`highfive [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`highfive @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_hit.error
	async def hit_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`hit [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`hit @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_hug.error
	async def hug_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`hug [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`hug @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_kill.error
	async def kill_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`kill [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`kill @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_kiss.error
	async def kiss_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`kiss [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`kiss @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_kisscheek.error
	async def kisscheek_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`kisscheek [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`kisscheek @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_knees.error
	async def knees_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`knees [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`knees @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_lick.error
	async def lick_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`lick [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`lick @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_love.error
	async def love_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`love [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`love @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_pat.error
	async def pat_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`pat [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`pat @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_poke.error
	async def poke_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`poke [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`poke @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_pout.error
	async def pout_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`pout [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`pout @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_raise.error
	async def raise_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`raise [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`raise @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_scare.error
	async def scare_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`scare [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`scare @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_shoot.error
	async def shoot_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`shoot [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`shoot @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_slap.error
	async def slap_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`slap [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`slap @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_takehand.error
	async def takehand_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`takehand [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`takehand @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_tickle.error
	async def tickle_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`tickle [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`tickle @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_tie.error
	async def tie_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`tie [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`tie @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_wave.error
	async def wave_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`wave [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`wave @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

	@_wink.error
	async def wink_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument): # can't ban

			await ctx.trigger_typing()

			emb = discord.Embed(description = f'**{ctx.author.name}**, укажи пользователя!', color=EMBED_COLOUR_SUCCESS)
			emb.set_author(name='Ошибка', icon_url='https://i.imgur.com/OK6csvQ.png')
			emb.add_field(name = '>>> Пример №1:', value = f'`wink [@участник]`', inline = True)
			emb.add_field(name = '>>> Пример №2:', value = f'`wink @vollar#0074`', inline = True)
			await ctx.send(embed = emb)

def setup(bot):
	bot.add_cog(interaction(bot))