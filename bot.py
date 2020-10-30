import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random
from ruamel.yaml import YAML
import os
import requests
from discord import Spotify


yaml = YAML()
with open("./config.yml", "r", encoding = "utf-8") as file:
    config = yaml.load(file)




bot = commands.Bot(command_prefix =config['Prefix'] , description = "speedy paw bot created by speediest paws")
bot.startTime = datetime.datetime.now(datetime.timezone.utc)
tChannelID = config['test Channel ID']

bot.embed_color = discord.Color.from_rgb(
    config['Embed Settings']['Color']['r'],
    config['Embed Settings']['Color']['g'],
    config['Embed Settings']['Color']['b']
)


emoji = config['Emojis']['pucca']
moosmile = config['Emojis']['moosmile']
moofrown = config['Emojis']['moofrown']

bot.footer = config['Embed Settings']['Footer']['Text']
bot.footer_image = config['Embed Settings']['Footer']['Icon URL']

bot.TOKEN = os.getenv(config['Bot Token Variable Name'])

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}. and connected to server! (ID: {bot.user.id} )")
    #pucca = '<:pucca:768598768726966282>'
    status = config['Playing Status']
    game = discord.Game(name = status)
    await bot.change_presence(activity = game)

    embed = discord.Embed(
        title = f"{bot.user.name} is here!",
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image

    )
    
    bot.tchannel = bot.get_channel(tChannelID)
    await bot.tchannel.send(embed = embed)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if message.author.id == 573247938747170836 or message.author.id == 395616177386422285:
            await message.channel.send("hi speedy paws")
        elif message.author.id == 376673538414739458:
            await message.channel.send("hi lil speedy paws")
        elif message.author.id == 358744905796943883:
            await message.channel.send('hi medium paws')
        elif message.author.id == 699403795876282398:
            await message.channel.send("hi rusty paws")
        else:
            await message.channel.send("hi slow paws")
   
    
    
    
    
    await bot.process_commands(message)

@bot.command(name = "restart", aliases = ["r"], help = "restart botpaws.")
@commands.is_owner()
async def restart(ctx):
    embedclose = discord.Embed(
        title = f'{bot.user.name} restarting!',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedclose.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url

    )
    embedclose.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    await bot.tchannel.send(embed= embedclose)
    
    await ctx.message.add_reaction(emoji)
    
    await bot.close()


@bot.command(help ="shows bot latency")
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command(name ="8ball", aliases= ["8b"],help = "8 ball command duh")
async def _8ball(ctx, *, question):

    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    embed8ball = discord.Embed(
        title = f'Question: {question}\nAnswer: {random.choice(responses)}',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)

    )
    embed8ball.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url

    )
    embed8ball.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    
    await ctx.channel.send(embed = embed8ball)




@bot.command(aliases=['live'], help="displays how long botpaws has been running")
async def uptime(ctx):
    delta_uptime =  datetime.datetime.now(datetime.timezone.utc) - bot.startTime
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f'botpaws has been up for {days}d, {hours}h, {minutes}m and {seconds}s')

@bot.command(help="boo!")
async def boo(ctx, *, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    
    

    await ctx.channel.send(f'boo! {member.mention}')

@bot.command(help= "hug another member duh")
async def hug(ctx, member: discord.Member):
    request_url ="http://api.nekos.fun:8080/api/hug"
    response = requests.get(request_url)
    responseJSON = response.json()
    imgURL = responseJSON.get('image')

    embedHug = discord.Embed(
        title = f'{ctx.author.display_name} **hugs** {member.display_name}',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedHug.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    embedHug.set_image(url= imgURL)
    await ctx.channel.send(embed= embedHug)

@bot.command(help= "slap another member duh")
async def slap(ctx, member: discord.Member):
    request_url ="http://api.nekos.fun:8080/api/slap"
    response = requests.get(request_url)
    responseJSON = response.json()
    imgURL = responseJSON.get('image')

    embedSlap = discord.Embed(
        title = f'{ctx.author.display_name} **slaps** {member.display_name}',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedSlap.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    embedSlap.set_image(url= imgURL)
    await ctx.channel.send(embed= embedSlap)

@bot.command(help="kiss another member, **haram command**")
async def kiss(ctx, member: discord.Member):
    request_url ="http://api.nekos.fun:8080/api/kiss"
    response = requests.get(request_url)
    responseJSON = response.json()
    imgURL = responseJSON.get('image')

    embedKiss = discord.Embed(
        title = f'{ctx.author.display_name} **Kisses** {member.display_name}',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedKiss.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    embedKiss.set_image(url= imgURL)
    await ctx.channel.send(embed= embedKiss)

@bot.command(help="cry command for sad paws")
async def cry(ctx, member: discord.Member=None):
    request_url ="http://api.nekos.fun:8080/api/cry"
    response = requests.get(request_url)
    responseJSON = response.json()
    imgURL = responseJSON.get('image')

    embedCry = discord.Embed(
        title = f'{ctx.author.display_name} is sad paws',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedCry.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    embedCry.set_image(url= imgURL)
    await ctx.channel.send(embed= embedCry)


@bot.command(aliases=['av'], help="display avatar of member, if no argument given display your avatar")
async def avatar(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    
    
    embedAV = discord.Embed(
        title = f'{member}',
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)

    )
    embedAV.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url

    )
    embedAV.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    embedAV.set_image(url='{}'.format(member.avatar_url))
    await ctx.channel.send(embed= embedAV)

@bot.command(help="makes a quick yes/no poll")
async def poll(ctx, *, question):
    await ctx.channel.purge(limit=1)
    embedPoll = discord.Embed(
        title = "new poll",
        description = question,
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embedPoll.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url

    )
    embedPoll.set_footer(
        text = bot.footer,
        icon_url= bot.footer_image
    )
    sentPoll = await ctx.channel.send(embed = embedPoll)
    await sentPoll.add_reaction(emoji= moosmile)
    await sentPoll.add_reaction(emoji= moofrown)



@bot.command()
@commands.guild_only() # We can only access activities from a guild
async def spotify(ctx, user: discord.Member = None):
    user = user or ctx.author  # default to the caller
    spot = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
    if spot is None:
        await ctx.send(f"{user.name} is not listening to Spotify")
        return
    embedspotify = discord.Embed(title=f"{user.name}'s Spotify", color=0x1eba10)
    embedspotify.add_field(name="Song", value=spot.title)
    embedspotify.add_field(name="Artist", value=spot.artist)
    embedspotify.add_field(name="Album", value=spot.album)
    embedspotify.set_thumbnail(url=spot.album_cover_url)
    await ctx.send(embed=embedspotify)

    






            

bot.run(bot.TOKEN, bot=True, reconnect=True)