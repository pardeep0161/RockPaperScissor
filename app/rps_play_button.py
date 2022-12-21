from app.rectangle import Rectangle
import pygame as pg


class RPSPlayButton(Rectangle):
    def __init__(self, display, position, size, color=(96,96,96), text="Start Battle", font_color=(255,10,10)) -> None:
        super().__init__(display, position, size, color)
        self.font_size = size[1] - 5
        self.font_color = font_color
        self.text=text
        self.position = position
        self.size = size
        self.clicked = False

    def _draw_button_text(self):
        self.font = pg.font.Font(None, self.font_size)
        self.font_surf = self.font.render(self.text, True, self.font_color)
        w, h = self.font.size(self.text)
        self.font_pos = (self.position[0] + (self.size[0]-w)/2, self.position[1] + (self.size[1]-h)/2)
        self.display.blit(self.font_surf, self.font_pos)

    def render(self):
        super().render()
        self._draw_button_text()

    def update(self, event):
        super().update(event)
        if self.active:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.clicked=True