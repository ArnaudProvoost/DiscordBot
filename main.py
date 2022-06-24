import json
import sys
import urllib.request
import discord
import json
from gpiozero import CPUTemperature

f = open('env.json')
data = json.load(f)

bot = discord.Client()

website_link_local = "http://192.168.0.152:8080/"
website_link_outside = "arnaud.sinners.be"

commands = ["!temperatuur", "!stop", "!checkwebsite", "!info"]


class cpu_class:
    temperature = "0"


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("DiscordBot is in " + str(guild_count) + " server.")


@bot.event
async def on_message(message):
    message_content = message.content

    if message.author == bot.user:
        return

    if "!temperature" in message_content.lower() or "!temperatuur" in message_content.lower():
        await message.reply("My cpu is at " + getTemperatureRaspberrypi() + "°c")

    if "!stop" in message_content:
        await message.reply("I will stop myself")
        sys.exit()

    if "!checkwebsite" in message_content.lower():
        returnWaarde, responsecode = getCheckwebsiteOnline()
        if returnWaarde == "true":
            await message.reply(":white_check_mark: De website staat goed online. \n Je kan deze terugvinden "
                                       "op deze lokale link " + website_link_local)
        else:
            await message.reply(":negative_squared_cross_mark: Pas op de website is down. \n Kijk dit na op "
                                       "deze lokale link " + website_link_local + ". \n De errorcode is " + str(
                responsecode))

    if "!info" in message_content.lower():
        await message.reply(getInformationBot())


def getTemperatureRaspberrypi():
    cpu = "null"
    # cpu = CPUTemperature()
    if cpu != "null":
        cpu_class.temperature = str(round(cpu.temperature))
    return cpu_class.temperature


def getCheckwebsiteOnline():
    response_code = urllib.request.urlopen(website_link_local).getcode()
    if response_code == 200:
        return "true", response_code
    else:
        return "false", response_code


def getInformationBot():
    str = ""
    for command in commands:
        str += "- " + command + "\n"

    return "Ik ben een bot geschreven door Arnaud Provoost. Als je meer informatie wilt over Arnaud volg dan volgende " \
           "link " + website_link_outside + ".\n Dit zijn de verschillende commands die je kan gebruiken \n" + str

bot.run(data["token"])
