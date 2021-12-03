import Draw

text = "게임이 끝났습니다"
index = 0
time = 0
onOff = False

def endOnOff():
    global onOff
    onOff = True

    
def end(view):
    global arr, time, text,index, onOff

    if onOff:
        
        if 19 > index:
            index +=1
        
        Draw.addText(view, text[:index], 40, (255,250,255), 440, 200)
            

