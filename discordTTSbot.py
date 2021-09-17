import discord
from discord.ext import commands
import discord.voice_client
from gtts import gTTS
from discord import FFmpegPCMAudio


last = ""
channelId = 12345678910
TOKEN = "xxxxxxxxxxxxxxx"


def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    return filename


def speakchoi(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    return filename

client = commands.Bot(command_prefix=["tts", "TTS", "Tts"], help_command=None)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.command(pass_context=True)
async def p(ctx):
    global last
    global channelId
    last = str(ctx.message.author) + ": " + str(ctx.message.content[5:])
    print(last)
    if discord.utils.get(client.voice_clients, guild=ctx.guild) == None:
        channel = client.get_channel(channelId)
        voice = await channel.connect()
        source = FFmpegPCMAudio(executable="C:\FFmpeg\\bin\\ffmpeg.exe", source=speak(ctx.message.content[5:]))
        player = voice.play(source)
    else:
        voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
        source = FFmpegPCMAudio(executable="C:\FFmpeg\\bin\\ffmpeg.exe", source=speak(ctx.message.content[5:]))
        voice_client.play(source)


@client.command(pass_context=True)
async def c(ctx):
    global last
    global channelId
    last = str(ctx.message.author) + ": " + str(ctx.message.content[7:])
    print(last)
    if discord.utils.get(client.voice_clients, guild=ctx.guild) == None:
        channel = client.get_channel(channelId)
        voice = await channel.connect()
        source = FFmpegPCMAudio(executable="C:\FFmpeg\\bin\\ffmpeg.exe", source=speakchoi(ctx.message.content[7:],ctx.message.content[5:7]))
        voice.play(source)
    else:
        voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
        source = FFmpegPCMAudio(executable="C:\FFmpeg\\bin\\ffmpeg.exe", source=speakchoi(ctx.message.content[7:],ctx.message.content[5:7]))
        voice_client.play(source)



@client.command(pass_context=True)
async def l(ctx):
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def help(ctx):
    text = """p/P: Play default langugage
    c/C: Play with chosen language
    l/L: Leave
    h/H: Show last message sent"""

    embed = discord.Embed(title="Commands", color=0xffffff)
    embed.add_field(name="Description", value=text)
    await ctx.channel.send(embed=embed)


@client.command(pass_context=True)
async def P(ctx):
    await p(ctx)


@client.command(pass_context=True)
async def C(ctx):
    await c(ctx)

@client.command(pass_context=True)
async def L(ctx):
    await l(ctx)

@client.command(pass_context=True)
async def h(ctx):
    print(last)
    await ctx.channel.send(last)

client.run(TOKEN)
