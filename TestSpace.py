import os

if len(os.listdir('./Commands')) != 0:
    CommandGroupList = os.listdir('./Commands')
    for x in range(1, len(CommandGroupList) + 1):
        print('{}.{}'.format(x, CommandGroupList[x - 1]))
CmdLinkNumber = eval(input('選擇指令群組:'))
CmdLinkName = CommandGroupList[CmdLinkNumber - 1]

print(CmdLinkName)