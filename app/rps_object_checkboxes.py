from app.checkbox import Checkbox
from app.rps_object import RPSObject
import pygame as pg


class RPSObjectCheckboxes:
    def __init__(self, display, position) -> None:
        self.rps_checkboxes = []
        for i, rps_object_type in enumerate(RPSObject.TYPES):
            self.rps_checkboxes.append(Checkbox(display, (position[0], position[1] + (i*20)), rps_type=rps_object_type))

    def render(self):
        for rps_check_box in self.rps_checkboxes:
            rps_check_box.render()

    
    def update_checkboxes(self, event):
        active_rps_object_chk_box_type = ''
        for rps_check_box in self.rps_checkboxes:
            rps_check_box.update(event)
            if rps_check_box.active:
                active_rps_object_chk_box_type = rps_check_box.rps_type

        if active_rps_object_chk_box_type and not active_rps_object_chk_box_type.isspace():
            for rps_check_box in self.rps_checkboxes:
                rps_check_box.update_checkbox(event)

    def selected_object(self):
        for rps_check_box in self.rps_checkboxes:
            if rps_check_box.checked:
                return rps_check_box.rps_type