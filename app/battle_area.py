from app.rectangle import Rectangle

class BattleArea(Rectangle):
    def __init__(self, display, position, size) -> None:
        super().__init__(display, position, size)
        