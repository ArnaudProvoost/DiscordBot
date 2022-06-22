import json

import discord
import json
from gpiozero import CPUTemperature

f = open('env.json')
data = json.load(f)

bot = discord.Client()

class cpu_class:
	temperature = "0"

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("DiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    message_content = message.content
    if "temperature" in message_content:
        await message.channel.send("My cpu is at "+getTemperatureRaspberrypi()+"°c")


def getTemperatureRaspberrypi():
    cpu = "null"
    # cpu = CPUTemperature()
    if cpu != "null":
        cpu_class.temperature = round(cpu.temerature)
    return cpu_class.temperature


bot.run(data["token"])
