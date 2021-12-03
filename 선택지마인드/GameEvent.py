# -*- coding: cp949 -*-
import pygame.event as getEvent
import pygame.mouse as mouse
import pygame.mixer as mixer
import Ending

mixer.init()

ClickBtnBgm = mixer.Sound('./resource/chatNext.wav')
onOff = False
onRoot = True

def onClickEvent(addFunc0, addFunc1, addFunc2, addFunc3, sOn):
    global sound, onOff, onRoot
    for event in getEvent.get():
        if event.type == 1025: #1025 is mouse button Click event
            if event.button == 1: # 1 is left click
                if not sOn:
                    x, y = event.pos
                        

                    if x >=408 and y >= 296 and x <= 662 and y <= 361: #button 1 click
                        if onRoot:
                            addFunc3(1)
                            onRoot = False
                        else:
                            if not onOff:
                                ClickBtnBgm.play()
                                addFunc0(1)
                                addFunc2()
                                onOff = True
                            else:
                                addFunc1()
                                addFunc2()
                                onOff = False
                                
                            
                    elif x >= 707 and y <= 361 and x <= 964 and y >= 297: # button 2 click
                        if onRoot:
                            addFunc3(-1)
                            onRoot = False
                        else:
                            if not onOff:
                                ClickBtnBgm.play()
                                addFunc0(2)
                                addFunc2()
                                onOff = True
                            else:
                                addFunc1()
                                addFunc2()
                                onOff = False
                
                    else:
                        if onOff:
                            addFunc1()
                            addFunc2()
                            onOff = False
                

def onQuitEvent():
    for event in getEvent.get():
        if event.type == 256: #256 is quit event
            break
