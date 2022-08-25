import os
from SerialTest import SerialCtrl

ser=SerialCtrl()

#初始設定
def GetInitialSet():
    InitialSetArray=[]
    #無初始化檔案流程
    if not os.path.exists("SerialSet.ini"):
        #顯示目前可用連接埠
        AvailblePort=ser.serial_ports()
        if len(AvailblePort)!=0:
            print('目前可使用連接埠:',AvailblePort)
            COMPortNumber=input('輸入連接號')
            BaudRate=input('輸入速率')
            SendMod=input('輸出模式')
            RecieveMod=input('接收模式')

            if len(os.listdir('./Commands'))!=0:
                CommandGroupList = os.listdir('./Commands')
                for x in range(1, len(CommandGroupList) + 1):
                    print('{}.{}'.format(x, CommandGroupList[x - 1]))
                CmdLinkNumber=eval(input('選擇指令群組:'))
                CmdLinkName=CommandGroupList[CmdLinkNumber-1]

            f=open("SerialSet.ini",'w+')
            content='{},{},{},{},{}'.format('COM'+COMPortNumber,BaudRate,SendMod,RecieveMod,CmdLinkName)
            f.write(content)

            InitialSetArray.append(COMPortNumber)
            InitialSetArray.append(BaudRate)
            InitialSetArray.append(SendMod)
            InitialSetArray.append(RecieveMod)
            InitialSetArray.append(CmdLinkName)

        else:
            print("無可使用連接埠")
    else:
        SerialSet=open("SerialSet.ini")
        SetInfo=SerialSet.readline()
        InitialSetArray=SetInfo.split(',')
    return InitialSetArray

def PrintMenu():
    print(
    '''
    
    ''')

#操作開始
if __name__ == '__main__':
    SetInfo=GetInitialSet()
    PrintMenu()

    # ser.ConnectSerial(SetInfo[0],SetInfo[1])
    # ser.SerialClose()