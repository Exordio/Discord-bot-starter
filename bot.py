import logging
import discord
import asyncio
import time

from datetime import datetime
from config import token

from controllers.commandController import commandController

client = discord.Client()
logging.basicConfig(filename='bot.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')


@client.event
async def on_ready():
    print(f'|| {datetime.now()} || We logged in as {client.user}')
    logging.warning(f'|| {datetime.now()} || We logged in as {client.user}')
    client.loop.create_task()


@client.event
async def on_message(message):
    await commandController(message, client)


def runClient():
    loop = asyncio.get_event_loop()
    while True:
        try:
            loop.run_until_complete(client.run(token, reconnect=True))
        except Exception as e:
            print("Error", e)
            logging.error(e)
        print("Waiting until restart 10 sec")
        time.sleep(10)


if __name__ == '__main__':
    runClient()