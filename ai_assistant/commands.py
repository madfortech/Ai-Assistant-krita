from krita import Krita
from PyQt5.QtWidgets import QMessageBox
from krita import ManagedColor
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QRectF
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPointF

class Commands:

    def create_layer(self, cmd):

        app = Krita.instance()

        QMessageBox.information(None, "Debug", "Krita instance OK")

        doc = app.activeDocument()

        if doc is None:
            QMessageBox.critical(None, "Debug", "No Active Document")
            return

        QMessageBox.information(
            None,
            "Debug",
            "Document: " + doc.name()
        )

        try:
            layer = doc.createNode(
                cmd.get("name", "AI Layer"),
                "paintlayer"
            )

            QMessageBox.information(None, "Debug", "createNode OK")

            doc.rootNode().addChildNode(layer, None)

            QMessageBox.information(None, "Debug", "addChildNode OK")

            doc.setActiveNode(layer)

            doc.refreshProjection()

            QMessageBox.information(None, "Debug", "Layer Created")

        except Exception as e:
            QMessageBox.critical(None, "Exception", str(e))

    
    def set_color(self, cmd):
        QMessageBox.information(
            None,
            "Debug",
            "set_color() called"
        )


        color = cmd.get("color") or cmd.get("value") or "#000000"

        window = Krita.instance().activeWindow()

        if window is None:
            print("No active window")
            return

        view = window.activeView()

        if view is None:
            print("No active view")
            return

        qcolor = QColor(color)

        QMessageBox.information(
            None,
            "Debug",
            f"Color = {color}"
        )

        try:
            managed = ManagedColor.fromQColor(
                qcolor,
                view.canvas()
            )

            view.setForeGroundColor(managed)

            QMessageBox.information(
                None,
                "Success",
                f"Foreground color set: {color}"
            )

        except Exception as e:
            QMessageBox.critical(
                None,
                "set_color Error",
                str(e)
            )
    
    
    def set_brush(self, cmd):

        preset_name = cmd.get("preset")

        app = Krita.instance()

        presets = app.resources("preset")

    

        brush = presets.get(preset_name)

        if brush is None:
            search = preset_name.lower()

            for name, resource in presets.items():
                if search in name.lower():
                    brush = resource
                    preset_name = name
                    break

        if brush is None:
            QMessageBox.critical(
                None,
                "Brush Error",
                f"Brush not found:\n{preset_name}"
            )
            return

        window = app.activeWindow()

        if window is None:
            return

        view = window.activeView()

        if view is None:
            return

        view.setCurrentBrushPreset(brush)

        QMessageBox.information(
            None,
            "Success",
            f"Brush changed to:\n{preset_name}"
        )
    
    def set_size(self, cmd):

        print(cmd)

        size = float(cmd.get("size", 10))

        print("Requested Size:", size)

        window = Krita.instance().activeWindow()

        if window is None:
            return

        view = window.activeView()

        if view is None:
            return

        print("Before:", view.brushSize())

        view.setBrushSize(size)

        print("After:", view.brushSize())


    def draw_line(self, cmd):

        doc = Krita.instance().activeDocument()
        if doc is None:
            return

        node = doc.activeNode()
        if node is None:
            return

        start = cmd.get("from", [0, 0])
        end = cmd.get("to", [100, 100])

        x1, y1 = start
        x2, y2 = end

        node.paintLine(
            QPoint(x1, y1),
            QPoint(x2, y2)
        )

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            f"Line: ({x1},{y1}) → ({x2},{y2})"
        )

    
    def draw_rectangle(self, cmd):

        doc = Krita.instance().activeDocument()

        if doc is None:
            return

        node = doc.activeNode()

        if node is None:
            return

        start = cmd.get("from", [0, 0])
        end = cmd.get("to", [100, 100])

        x1, y1 = start
        x2, y2 = end

        rect = QRectF(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )

        node.paintRectangle(rect)

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            f"Rectangle: ({x1},{y1}) → ({x2},{y2})"
        )
    def draw_circle(self, cmd):

        doc = Krita.instance().activeDocument()

        if doc is None:
            return

        node = doc.activeNode()

        if node is None:
            return

        start = cmd.get("from", [0, 0])
        end = cmd.get("to", [100, 100])

        x1, y1 = start
        x2, y2 = end

        rect = QRectF(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )

        node.paintEllipse(rect)

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            f"Circle: ({x1},{y1}) → ({x2},{y2})"
        )
    
    
    def draw_ellipse(self, cmd):

        doc = Krita.instance().activeDocument()

        if doc is None:
            return

        node = doc.activeNode()

        if node is None:
            return

        start = cmd.get("from", [0, 0])
        end = cmd.get("to", [100, 100])

        x1, y1 = start
        x2, y2 = end

        rect = QRectF(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )

        node.paintEllipse(rect)

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            f"Ellipse: ({x1},{y1}) → ({x2},{y2})"
        )
    

    def draw_bezier(self, cmd):

        doc = Krita.instance().activeDocument()

        if doc is None:
            return

        node = doc.activeNode()

        if node is None:
            return

        start = cmd.get("start", [0, 0])
        control1 = cmd.get("control1", [100, 0])
        control2 = cmd.get("control2", [200, 0])
        end = cmd.get("end", [300, 0])

        path = QPainterPath()

        path.moveTo(QPointF(start[0], start[1]))

        path.cubicTo(
            QPointF(control1[0], control1[1]),
            QPointF(control2[0], control2[1]),
            QPointF(end[0], end[1])
        )

        node.paintPath(path)

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            "Bezier curve drawn."
        )
    

    def draw_polygon(self, cmd):

        doc = Krita.instance().activeDocument()

        if doc is None:
            return

        node = doc.activeNode()

        if node is None:
            return

        points_data = cmd.get("points", [])

        if len(points_data) < 3:
            QMessageBox.warning(
                None,
                "Polygon",
                "Polygon requires at least 3 points."
            )
            return

        points = []

        for p in points_data:
            points.append(QPointF(p[0], p[1]))

        node.paintPolygon(points)

        doc.refreshProjection()

        QMessageBox.information(
            None,
            "Success",
            f"Polygon with {len(points)} points drawn."
        )
    

     