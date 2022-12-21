from app.rectangle import Rectangle
import pygame as pg
from app.rps_object import RPSObject
pg.init()

class RPSBattleArea(Rectangle):
    def __init__(self, display, position, size) -> None:
        super().__init__(display, position, size)
        self.rps_object_types = {}
        self.display = display
        self.clicked = False


    def update(self, event, selected_object_type):
        
        if not selected_object_type or selected_object_type.isspace():
            return
            
        super().update(event)
        if self.active:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.clicked=True
            
            if self.clicked and event.type == pg.MOUSEBUTTONUP:
                x_pos, y_pos = pg.mouse.get_pos()
                self.rps_object_types.setdefault(selected_object_type,[]).append(RPSObject(self.display, selected_object_type, (x_pos, y_pos)))

    def render(self):
        super().render()
        for rps_objects in self.rps_object_types.values():
            for rps_object in rps_objects:
                rps_object.render()

    

    def start_battle(self):
        pass

    