
class Set():
    def __init__(self):
        self.ModeType='快捷模式'


    def SetChangeAction(cmd, ModeType):
        if cmd == 'b':
            result = ChangeMode(ModeType)
            return result
        else:
            print('無效指令')