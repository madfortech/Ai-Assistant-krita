from krita import Krita

class BrushEngine:

    def __init__(self):
        self.app = Krita.instance()

    def stroke(self, cmd):

        view = self.app.activeWindow().activeView()

        if not view:
            return

        x1 = cmd.get("x1", 100)
        y1 = cmd.get("y1", 100)

        x2 = cmd.get("x2", 400)
        y2 = cmd.get("y2", 300)

        size = cmd.get("size", 30)

        view.setBrushSize(size)

        view.freehandLine(
            x1,
            y1,
            x2,
            y2
        )