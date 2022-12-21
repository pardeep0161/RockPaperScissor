import pygame as pg
from app.rps_object_checkboxes import RPSObjectCheckboxes
from app.rps_battle_area import RPSBattleArea
from app.rps_play_button import RPSPlayButton

pg.init()
pg.font.init()

class Game:
    def __init__(self):
        self.WIDTH = 700
        self.HEIGHT = 600
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.object_chkboxes = RPSObjectCheckboxes(self.display, (self.WIDTH-100, 100))
        self.battle_area = RPSBattleArea(self.display, (50, 50), (self.WIDTH - 200, self.HEIGHT - 200))
        self.play_button = RPSPlayButton(self.display, (150, self.HEIGHT - 100), (self.WIDTH/2 -50, 50))

        self.running = True

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    quit()
                if not self.play_button.clicked:
                    self.object_chkboxes.update_checkboxes(event)
                    self.battle_area.update(event, self.object_chkboxes.selected_object())
                    self.play_button.update(event)
                if self.play_button.clicked:
                    self.battle_area.start_battle()

            self.display.fill((200, 200, 200))
            self.object_chkboxes.render()
            self.battle_area.render()
            self.play_button.render()
            pg.display.flip()