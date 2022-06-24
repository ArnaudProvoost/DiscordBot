import json
import sys
from http.client import HTTPConnection
import discord
import json
from gpiozero import CPUTemperature

f = open('env.json')
data = json.load(f)

bot = discord.Client()

website_link_local = "192.168.0.152"
website_link_local_port = 8080
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
        returnWaarde, errormessage = getCheckwebsiteOnline()
        website_link_answer = "http://"+website_link_local+":"+str(website_link_local_port)+"/"
        if returnWaarde == "true":
            await message.reply(":white_check_mark: De website staat goed online. \n Je kan deze terugvinden "
                                       "op deze lokale link " + website_link_answer)
        else:
            await message.reply(":negative_squared_cross_mark: Pas op de website is down. \n Kijk dit na op "
                                       "deze lokale link " + website_link_answer + "."+ "\n Met deze errormessage: "+errormessage)

    if "!info" in message_content.lower():
        await message.reply(getInformationBot())


def getTemperatureRaspberrypi():
    cpu = "null"
    # cpu = CPUTemperature()
    if cpu != "null":
        cpu_class.temperature = str(round(cpu.temperature))
    return cpu_class.temperature


def getCheckwebsiteOnline():
    connection = HTTPConnection(website_link_local, port=website_link_local_port, timeout=10)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return "true","none"
    except Exception as e:
        error = e
        return "false", str(error)



def getInformationBot():
    str = ""
    for command in commands:
        str += "- " + command + "\n"

    return "Ik ben een bot geschreven door Arnaud Provoost. Als je meer informatie wilt over Arnaud volg dan volgende " \
           "link " + website_link_outside + ".\n Dit zijn de verschillende commands die je kan gebruiken \n" + str

bot.run(data["token"])
