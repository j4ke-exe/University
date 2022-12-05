import discord
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

# Set up the data source
yf.pdr_override()

# Create a client object
client = discord.Client()

# Define the bot's response
response = 'The current price of GameStop stock is: $%.2f'

# Define the channel the bot should listen to
channel_id = 1234567890

# Define the command the bot should listen for
command = '!gme'

# Event that triggers when the bot connects to Discord
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event that triggers when the bot receives a message in the specified channel
@client.event
async def on_message(message):
    if message.channel.id == channel_id and message.content.startswith(command):
        # Get the current price of GameStop's stock
        gamestop = pdr.get_data_yahoo('GME', start="2020-01-01")
        price = gamestop['Adj Close'][-1]

        # Send the current price in the pre-defined response
        await message.channel.send(response % price)

# Start the bot
client.run('bot_token')
