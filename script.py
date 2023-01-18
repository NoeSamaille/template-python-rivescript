from rivescript import RiveScript
import requests
import discord
import os

# Function to get weather forecast 
def get_weather(lat, lon, endpoint):
    url = f"https://api.openweathermap.org/data/2.5/{endpoint}?lat={lat}&lon={lon}&appid={os.environ['WEATHER_API_KEY']}&lang=fr&units=Metric"
    response = requests.request('GET', url, headers={}, data={})
    return response.json()

# Function to get current time of selected timezone 
def get_time(timezone):
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
    response = requests.request('GET', url, headers={}, data={})
    return response.json()

# Inits Rivescript bot
bot = RiveScript()
bot.load_directory('./eg/brain')
bot.sort_replies()

# Inits Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Handles Discord login event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Handles Discord message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    reply = bot.reply('localuser', message.content)
    if reply.startswith('!!'):
        action = reply.replace('!!', '').split('$$')[0]
        if action == 'weather':
            weather = get_weather(43.607, 3.877, 'weather')
            reply = f"Actuellement, le temps est: {weather['weather'][0]['description']}, la temperature ressentie est de {weather['main']['feels_like']} °c"
        elif action == 'weather_forcast':
            weather = get_weather(43.607, 3.877, 'forecast')
            cur_day = ''
            reply = 'Voici la prevision meteo pour les 5 prochains jours à Montpellier:\n'
            for prev in weather['list']:
                day = prev['dt_txt'][:10]
                if day != cur_day:
                    cur_day = day
                    reply += f"  - {day}: {prev['weather'][0]['description']}, temperature {prev['main']['temp']} °c\n"
        elif action == 'time':
            location = reply.replace('!!', '').split('$$')[1]
            timezone = 'Europe/Paris'
            if location == 'londres':
                timezone = 'Europe/London'
            elif location == 'new york':
                timezone = 'America/New_York'
            elif location == 'tokyo':
                timezone = 'Asia/Tokyo'
            time = get_time(timezone)
            reply = f'A {location}, il est {time["time"]}'
    await message.channel.send(reply)

# Run discord client using bot token
client.run(os.environ['DISCORD_TOKEN'])
