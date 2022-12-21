import pygame as pg

class Rectangle:
    def __init__(self, display, position, size, color = (255, 255, 255), outline_color=(0, 0, 0)) -> None:
        self.display = display
        self.checkbox_obj = pg.Rect(position[0], position[1], size[0], size[1])
        self.checkbox_outline = self.checkbox_obj.copy()
        self.active = False
        self.color = color
        self.outline_color=outline_color

    def render(self):
        pg.draw.rect(self.display, self.color, self.checkbox_obj)
        pg.draw.rect(self.display, self.outline_color, self.checkbox_outline, 1)

    def update(self, event):
        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
            # self.x, self.y, 12, 12
            px, py, w, h = self.checkbox_obj  # getting check box dimensions
            if px < x < px + w and py < y < py + h:
                self.active = True
            else:
                self.active = False