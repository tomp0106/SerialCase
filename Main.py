import os
from Utility import CMDlink
from SerialTest import SerialCtrl


ser=SerialCtrl()
CMDL=CMDlink()

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

            CmdLinkName=CMDL.GetCMDGroup()

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
a.	變更快捷群           :更換快捷指令檔案
b.	測試模式變更          :可自行輸入指令,輸入q離開
c.	顯示當前快捷指令列    
d.	變更傳輸資料保存與否     
e.	變更傳輸設定         :(1)COM (2)速率 (3)Hex or Text
dd. 關閉/顯示 菜單
h.  使用說明
v.  版本確認
    ''')
def DisplayCmdLinks(CmdlinksInfo):
    i=0
    for x in CmdlinksInfo.keys():
       i+=1
       print('{}.{}'.format(i,x))
def ChangeMode(ModeType):
    ModeList=['LinkTest','手動模式','腳本模式','假資料模式']
    Modeindex=ModeList.index(ModeType)
    #顯示模式
    for x in range(len(ModeList)):
        print('{}.{}'.format(x+1,ModeList[x]))

    UserAns=input('請輸入要變更的模式')
    if UserAns.isnumeric()&eval(UserAns)<=len(ModeList):
        ModeType=ModeList[eval(UserAns)]
    else:
        ModeType = ModeList[Modeindex]

    return ModeType
def TestMode(UserCmd,CmdlinksList,CmdlinksInfo,ModeType):
    if ModeType=='LinkTest':
        if UserCmd.isnumeric():
            CmdName = CmdlinksList[eval(UserCmd) - 1]
            cmd = CmdlinksInfo[CmdName]['commmand']

            if CmdlinksInfo[CmdName]['SendType'] == 'H':
                cmd = CMDL.GetHexCommand(cmd)
                print(cmd)
                ser.SerialWrite(cmd)
            else:
                ser.SerialWrite(cmd)
        else:
            print('系統設定變更')

        if CmdlinksInfo[CmdName]['ReciveType'] == 'H':
            ser.GetDebugHexInfo()
        else:
            ser.GetDebugTextInfo()
def SetChangeAction(cmd,ModeType):
    if cmd=='b':
        result=ChangeMode(ModeType)
        return result
    else:
        print('無效指令')

#操作開始
if __name__ == '__main__':
    #取得初始化設定
    SetInfo=GetInitialSet()
    ModeType='LinkTest'

    #連線流程
    try:
        ser.ConnectSerial(SetInfo[0],SetInfo[1])
    except:
        print('連接失敗')
    #取得快捷指令
    CmdlinksInfo=CMDL.CmdlinksInfo(SetInfo[4])
    DisplayCmdLinks(CmdlinksInfo)

    CmdlinksList=[]
    for x in CmdlinksInfo.keys():
        CmdlinksList.append(x)
    while(1):
        print()
        UserCmd=input('請輸入指令')

        # if UserCmd.isnumeric():
        #通訊測試流程
        TestMode(UserCmd,CmdlinksList,CmdlinksInfo,ModeType)
    # else:
    #     #使用設定流程
    #     SetChangeAction(UserCmd,ModeType)

    ser.SerialClose()