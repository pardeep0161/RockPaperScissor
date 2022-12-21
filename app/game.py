import pygame as pg
from app.object_checkboxes import ObjectCheckboxes
from app.battle_area import BattleArea
from app.play_button import PlayButton

pg.init()
pg.font.init()

class Game:
    def __init__(self):
        self.WIDTH = 700
        self.HEIGHT = 600
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.object_chkboxes = ObjectCheckboxes(self.display, (self.WIDTH-100, 100))
        self.battle_area = BattleArea(self.display, (50, 50), (self.WIDTH - 200, self.HEIGHT - 200))
        self.play_button = PlayButton(self.display, (150, self.HEIGHT - 100), (self.WIDTH/2 -50, 50))

        self.running = True
        self.battle_started=False

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    quit()
                if not self.battle_started:
                    self.object_chkboxes.update_checkboxes(event)

            self.display.fill((200, 200, 200))
            self.object_chkboxes.render()
            self.battle_area.render()
            self.play_button.render()
            pg.display.flip()