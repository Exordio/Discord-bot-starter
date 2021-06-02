from config import permissionAccessChannelList, permissionAccessUserList
from functions.test.sendTestMsg import sendTestMsg


class CommandRunner:
    def __init__(self, message, client):
        self.message = message
        self.client = client

        async def tst():
            return await sendTestMsg(self.message)

        # Публичные словари кортежей команд
        tTest = {('!test',): tst}
        self.commandsList = [tTest]

    async def runCommand(self):
        findCommand = False
        for command in self.commandsList:
            if not findCommand:
                for key in command:
                    if self.message.content.startswith(key):
                        try:
                            await command[key]()
                        except:
                            pass
                        finally:
                            findCommand = True
                            break
            else:
                break

        return findCommand


async def commandController(message, client):
    commandSuccess = False

    if message.author == client.user:
        return

    if str(message.channel) in permissionAccessChannelList and \
            str(message.author) in permissionAccessUserList:
        cRunner = CommandRunner(message, client)
        await cRunner.runCommand()

    if (str(message.channel) in permissionAccessChannelList and
        str(message.channel) in permissionAccessUserList) and \
            not commandSuccess and message.content.startswith('!'):
        await message.channel.send('The command was not found. You can type! Help to display a list of commands.')
