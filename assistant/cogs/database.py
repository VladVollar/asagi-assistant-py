from main import bot
from global_sets import *

class database(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs

	db = sqlite3.connect('voice.db')
	sql = db.cursor()

	sql.execute("""CREATE TABLE IF NOT EXISTS voiceChannel (
		userID INTEGER,
		voiceID INTEGER,
		boolean BOOLEAN
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS guild (
		guildID INTEGER,
		ownerID INTEGER,
		voiceChannelID INTEGER,
		voiceCategoryID INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS userSettings (
		userID INTEGER,
		channelName TEXT,
		channelLimit INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS guildSettings (
		guildID INTEGER,
		channelName TEXT,
		channelLimit INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS main (
		prefix TEXT,
		guildID INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS bio (
		bio TEXT,
		userID INTEGER,
		guildID INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS levels (
		level INTEGER, 
		xp INTEGER, 
		user INTEGER, 
		guild INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS levelSettings (
		levelsys BOOL, 
		role INTEGER, 
		levelreq INTEGER, 
		guild INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS welcomeSettings (
		welcomesys BOOL, 
		channel INTEGER, 
		guild INTEGER
	)""")

	sql.execute("""CREATE TABLE IF NOT EXISTS automodSettings (
		automodsys BOOL,
		guild INTEGER
	)""")

	db.commit()

def setup(bot):
	bot.add_cog(database(bot))