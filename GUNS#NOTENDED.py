import SETTINGS
import SOUND
import pygame as pg
import random
import math
import os

class Gun:

    def __init(self, txr, stats, snd, aim):
        seff_spr_sht = pg.image.load(txr['spr_sht'])
        self.itm_txr = txr['item']
        self.sub_itm_txr = pygame.transform.scale(
            pygame.image.load(self.itemtexture
                              ).subsurface(0,112,64,16
                                           ).convert_alpha(),
                                                     (256, 64))
        self.rect = self.spr_sht.get_rect()
        self.spr_sht = pygame.transform.scale(self.spr_sht,
                                                  (int(self.rect.width * 6),
                                                   int(self.rect.height * 6)))
        self.aim =     [self.spr_sht.subsurface(0,0,420,360).convert_alpha(),
                        self.spr_sht.subsurface(0,360,420,360).convert_alpha(),
                        self.spr_sht.subsurface(0  ,720,420,360).convert_alpha()]
        self.hipfire = [self.spr_sht.subsurface(420,0,420,360).convert_alpha(),
                        self.spr_sht.subsurface(420,360,420,360).convert_alpha(),
                        self.spr_sht.subsurface(420,720,420,360).convert_alpha()]
        self.aimdown = [self.spr_sht.subsurface(840,0,420,360).convert_alpha(),
                        self.spr_sht.subsurface(840,360,420,360).convert_alpha(),
                        self.spr_sht.subsurface(840,720,420,360).convert_alpha()]
        self.reload =  [self.spr_sht.subsurface(0,0,420,360).convert_alpha(),
                        self.spr_sht.subsurface(1260,0,420,360).convert_alpha(),
                        self.spr_sht.subsurface(1260,360,420,360).convert_alpha(),
                        self.spr_sht.subsurface(1260,720,420,360).convert_alpha(),
                        self.spr_sht.subsurface(1260,1080,420,360).convert_alpha(),
                        self.spr_sht.subsurface(1260,1440,420,360).convert_alpha()]
        self.sounds = sounds
        self.hit_marker = pygame.mixer.Sound(os.path.join(
            'sounds',
            'other',
            'hitmarker.ogg'))
        self.dmg = stats['dmg']
        self.accuracy = stats['spread']*2
        self.firerate = stats['firerate']
