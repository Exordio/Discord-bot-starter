async def sendTestMsg(message):
    await message.channel.send('Test OK!')
    await message.channel.send(f'{message.author}')
    await message.channel.send(f'{message.channel}')
    print(message.author)
