import os
import disnake
import keep_alive

client = disnake.Client()


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


my_secret = os.environ['TOKEN']
keep_alive.keep_alive()
client.run(my_secret)
