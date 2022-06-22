import discord
from gpiozero import CPUTemperature

bot = discord.Client()

class cpu_class:
	temperature = "I am running locally"

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    message_content = message.content
    if "temperature" in message_content:
        await message.channel.send(getTemperatureRaspberrypi())


def getTemperatureRaspberrypi():
    cpu = "null"
    # cpu = CPUTemperature()
    if cpu != "null":
        cpu_class.temperature = cpu.temerature
    return cpu_class.temperature


bot.run("Change this")
