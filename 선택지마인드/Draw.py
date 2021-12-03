import pygame.draw as draw
import pygame.display as display
import pygame.font as font
import pygame.image as image
import pygame.transform as transform

def addRect(view, color, array, thick):
    return draw.rect(view, color, array, thick)

def addText(view, text, size, textColor, x, y, backColor=None):
    return view.blit((font.Font('./resource/PFStardust.ttf', size).render(text, True, textColor, backColor)), (x, y))
 
def addImage(view, path, x, y, sizeX, sizeY):
    view.blit(transform.scale(image.load(path).convert_alpha(), (sizeX, sizeY)), (x, y))
