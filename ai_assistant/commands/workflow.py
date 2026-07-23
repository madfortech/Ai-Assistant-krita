from .drawing import Commands
from .layers import Layers
from .brushes import Brushes
from .selection import Selection
from .tools import Tools
from .illustration import Illustration
import random

class Workflow:

    def __init__(self):

        self.commands = Commands()
        self.layers = Layers()
        self.brushes = Brushes()
        self.selection = Selection()
        self.tools = Tools()
        self.illustration = Illustration()

    def run(self, workflow, params=None):

        if params is None:
            params = {}

        workflows = {
            "character": self.character,
            "landscape": self.landscape,
            "tree": self.tree,
            "building": self.building,
            "icon": self.icon,
            "sprite": self.sprite,
            "weapon": self.weapon,
            "npc": self.npc,
            "create_forest": self.create_forest,
        }

        action = workflows.get(workflow)

        if action:
            return action(params)

        return False

    def character(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def landscape(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def tree(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def building(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def icon(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def sprite(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def weapon(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True

    def npc(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        return True
    
    # Forest
    def create_forest(self, params):

        self.layers.add_paint_layer()
        self.tools.activate_freehand_tool()

        trees = [
            {
                "x": 300,
                "y": 170
            }
        ]

        for tree in trees:
            self.illustration.draw_tree(tree)

        self.illustration.draw_cloud({
            "x": 120,
            "y": 40
        })

        self.illustration.draw_cloud({
            "x": 420,
            "y": 60
        })

        self.illustration.draw_sun({
            "x": 700,
            "y": 70
        })

        return True