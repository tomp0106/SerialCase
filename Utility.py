import os
import csv

#快捷指令
class CMDlink():
    def GetCMDGroup(self):
        a=os.listdir('./Commands')
        return a
    def GetCommands(self,FileName):
        with open(FileName, newline='') as csvfile:
            # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile, delimiter=' ')
            # 以迴圈輸出每一列
            for row in rows:
                print(row)

    def GetHexCommand(self,CommandWords):

        HexCMD = bytearray()
        for x in CommandWords:
            base16INT = int(x, 16)
            HexCMD.append(base16INT)
        return HexCMD


if __name__ == '__main__':
    #取得指令群
    CMDL=CMDlink()
    x=CMDL.GetCMDGroup()

