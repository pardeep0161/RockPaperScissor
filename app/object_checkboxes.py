from app.checkbox import Checkbox
from app.objects import ROCK,PAPER, Rock, Paper
import pygame as pg


class ObjectCheckboxes:
    def __init__(self, display, position) -> None:
        self.rock_chkbox = Checkbox(display, (position[0], position[1]), caption=ROCK.capitalize())
        self.paper_chkbox = Checkbox(display, (position[0], position[1]+25), caption=PAPER.capitalize())

    def render(self):
        self.rock_chkbox.render()
        self.paper_chkbox.render()

    
    def update_checkboxes(self, event):
        self.rock_chkbox.update(event)
        self.paper_chkbox.update(event)
        self.rock_chkbox.update_checkbox(event, other_checkbox_active= self.paper_chkbox.active)
        self.paper_chkbox.update_checkbox(event, other_checkbox_active= self.rock_chkbox.active)

    def selected_object(self):
        if self.rock_chkbox.checked:
            return ROCK
        if self.rock_chkbox.checked:
            return PAPER