from app.rectangle import Rectangle
import pygame as pg

class Checkbox(Rectangle):
    def __init__(self, display, position, color=(230, 230, 230), caption="",
                 check_color=(0, 0, 0), font_size=22, font_color=(0, 0, 0), text_offset=(15, 1)):
        super().__init__(display, position, (12,12))
        self.display = display
        self.position = position
        self.color = color
        self.caption = caption
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.checked = False
        self.click = False
        self.other_checkbox_active = False

    def _draw_button_text(self):
        self.font = pg.font.Font(None, 22)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.position[0] + self.to[0], self.position[1] + 12 / 2 - h / 2 + self.to[1])
        self.display.blit(self.font_surf, self.font_pos)

    def render(self):
        super().render()
        if self.checked:
            pg.draw.circle(self.display, self.cc, (self.position[0] + 6, self.position[1] + 6), 4)

        self._draw_button_text()

    def _mouse_up(self):
            if self.active and not self.checked and self.click:
                self.checked = True
            elif self.other_checkbox_active and self.checked:
                self.checked = False

    def update_checkbox(self, event, other_checkbox_active):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.click = True
            self.other_checkbox_active = other_checkbox_active
        if event.type == pg.MOUSEBUTTONUP:
            self._mouse_up()