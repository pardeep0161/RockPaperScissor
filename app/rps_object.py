import pygame as pg

class RPSObject:
    TYPES = ['Rock', 'Paper', 'Scissor']
    ENEMY_TYPES = {
        'Rock': 'Scissor',
        'Paper': 'Rock',
        'Scissor': 'Paper'
    }

    TYPE_COLORS = {
        'Rock': (255,0,0),
        'Paper': (0,255,0),
        'Scissor': (0,0,255)
    }

    def __init__(self, display, rps_type, position) -> None:
        self.rps_type = rps_type
        self.position = position
        self.enemies_pos = []
        self.display = display
        
        # imp = pg.image.load("app\ObjectImages\paper.png").convert()
        # display.blit(imp, position)

    def render(self):
        pg.draw.circle(self.display, self.TYPE_COLORS[self.rps_type], (self.position[0] + 6, self.position[1] + 6), 6)


    # def add_enemy_pos(self, enemy_pos):
    #     self.enemies_pos.append(enemy_pos)