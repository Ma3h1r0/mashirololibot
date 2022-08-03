def get_command_text(textlt): #指令提取
    try:
        textcomm = textlt
        if ' ' in textlt:
            char_1=' '
            commkgkg=textcomm.find(char_1)
            outip = textcomm[commkgkg+1:len(textcomm)]
            if outip == None:
                return False
            else:
                return outip
        else:
            return False
    except:
        return False
