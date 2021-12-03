# -*- coding: cp949 -*-
import sys
import pygame
import pygame.display as display
import pygame.time as time
import pygame.mouse as mouse
import pygame.mixer as mixer
import Draw
import GameEvent
import Utils
import Ending

WHITE = (255, 255, 255)

pygame.init()
mixer.init()

mixer.music.load('./resource/bgm.wav')
mixer.music.play()

view = display.set_mode([1200, 600])

root = 0

index = 0
subIndex = 1

bgmTime = 0

onOff = True

onScreen = True

end = False

stime = 0
sOn = False

def setIndex():
    global index, subIndex
    index = subIndex * 3
    subIndex += 1
    print(index)

def onOffScreen():
    global onScreen
    onScreen = not onScreen

def addIndex(count):
    global index
    index += count

def reverseOnOff():
    global onOff
    onOff = not onOff

def setStory(number):
    global root, index
    if root == 0:
        index = 0
        root = number

def Story(storyRoot):
    global end, index, onScreen, stime, sOn, onOff
    if Utils.getFirstLen(storyRoot) + 1 > index:  
        Draw.addText(view, Utils.getFirst(storyRoot, index)[0], 20, (255,250,255), 120, 405)
        Draw.addText(view, Utils.getFirst(storyRoot, index)[1], 20, (255,250,255), 120, 430)

        if onOff:
            Draw.addImage(view, './resource/textBox.png', 400, 290, 270, 80)
            Draw.addImage(view, './resource/textBox.png', 700, 290, 270, 80)

            Draw.addText(view, Utils.getChoice(storyRoot, index)[0], 15, (255,250,255), 425, 322)
            Draw.addText(view, Utils.getChoice(storyRoot, index)[1], 15, (255,250,255), 725, 322)
    else:
        onOffScreen()
        end = True

    if Utils.isFinish(storyRoot, index):
            Ending.endOnOff()
            sOn = True
            onOff = False

    if sOn:
                
        onScreen = False


while True:
    time.Clock().tick(20)
    view.fill(WHITE)

    if root == 0:
        view.blit(pygame.image.load('./resource/House.jfif'), (-400, -250))
        Story('story')
    elif root == 1:
        view.blit(pygame.image.load('./resource/Forest.png'), (-80, -250))
        Story('first')
    elif root == -1:
        view.blit(pygame.image.load('./resource/Forest.png'), (-80, -250))
        Story('two')

    if onScreen:
        Draw.addImage(view, './resource/chatBox.png', -90, 30, 1300, 700)
        Draw.addText(view, '질문자', 30, (255,250,255), 180, 340)

            
    GameEvent.onClickEvent(addIndex, setIndex, reverseOnOff, setStory, sOn)
    GameEvent.onQuitEvent()


    if 20 * 110 == bgmTime:
        bgmTime = 0
        mixer.music.play()
    else:
        bgmTime += 1
        Ending.end(view)

    if end:
        Ending.endOnOff()
        onScreen = False
        
    
    display.update()

pygame.quit()
sys.exit(0)
