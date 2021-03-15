import pygame

pygame.font.init()

class Text:
    def __init__(self, x, y, string, clr, size):
        self.x = x
        self.y = y
        self.str = string
        self.clr = clr
        self.sz = size
        self.fnt = pygame.font.Font("DUGAFONT.ttf", self.sz)
        self.rslt = self.fnt.render(self.str, True, self.clr)
        pass
    def draw(self, cnvs):
        cnvs.blit(self.rslt, (self.x, self.y))
        pass
    def text(self, txt):
        self.rslt = self.fnt.render(txt, True, self.clr)
        self.str = txt
        pass
    def pos(self, x, y):
        self.x = x
        self.y = y
        pass
    pass
###
