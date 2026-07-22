#from .commands import Commands
from .commands.layers import Layers
from .commands.drawing import Commands
from .commands.brushes import Brushes
from .commands.selection import Selection
from .commands.tools import Tools
#from .commands.registry import COMMANDS

class Executor:

    def __init__(self):
        self.commands = Commands()
        self.brushes = Brushes()
        self.layers = Layers()
        self.selection = Selection()
        self.tools = Tools()
        
    def execute(self, commands):

        if not commands:
            return

        for cmd in commands:

            action = cmd.get("action")

            if not action:
                continue

            try:

                if action == "create_layer":
                    self.commands.create_layer(cmd)

                elif action == "set_color":
                    self.commands.set_color(cmd)

                elif action == "set_brush":
                    self.commands.set_brush(cmd)

                elif action == "set_size":
                    self.commands.set_size(cmd)

                elif action == "draw_line":
                    self.commands.draw_line(cmd)

                elif action == "draw_rectangle":
                    self.commands.draw_rectangle(cmd)

                elif action == "draw_circle":
                    self.commands.draw_circle(cmd)
                
                elif action == "draw_ellipse":
                    self.commands.draw_ellipse(cmd)

                elif action == "draw_bezier":
                    self.commands.draw_bezier(cmd)
                    
                elif action == "draw_polygon":
                    self.commands.draw_polygon(cmd)

                elif action == "increase_brush_size":
                    self.brushes.increase_size()

                elif action == "increase_opacity":
                    self.brushes.increase_opacity()
                
                # Create Layers
                elif action == "add_paint_layer":
                    self.layers.add_paint_layer()

                elif action == "add_group_layer":
                    self.layers.add_group_layer()

                elif action == "add_vector_layer":
                    self.layers.add_vector_layer()

                elif action == "add_fill_layer":
                    self.layers.add_fill_layer()

                elif action == "add_filter_layer":
                    self.layers.add_filter_layer()

                elif action == "add_clone_layer":
                    self.layers.add_clone_layer()

                # Layer Operations
                elif action == "duplicate_layer":
                    self.layers.duplicate()

                elif action == "merge_layer":
                    self.layers.merge()

                elif action == "flatten_layer":
                    self.layers.flatten()

                elif action == "remove_layer":
                    self.layers.remove()

                # Layer Order
                elif action == "move_layer_up":
                    self.layers.move_up()

                elif action == "move_layer_down":
                    self.layers.move_down()

                # Layer Visibility
                elif action == "toggle_layer_visibility":
                    self.layers.toggle_visibility()

                # Layer Lock
                elif action == "toggle_layer_lock":
                    self.layers.toggle_lock()

                # Alpha Lock
                elif action == "toggle_layer_alpha_lock":
                    self.layers.toggle_alpha_lock()

                # Alpha Inheritance
                elif action == "toggle_layer_inherit_alpha":
                    self.layers.toggle_alpha_inheritance()


                elif action == "select_rectangle":
                    self.selection.select_rectangle()

                elif action == "select_all":
                    self.selection.select_all()

                elif action == "deselect":
                    self.selection.deselect()

                elif action == "invert_selection":
                    self.selection.invert_selection()

                elif action == "select_ellipse":
                    self.selection.select_ellipse()

                elif action == "select_polygon":
                    self.selection.select_polygon()

                elif action == "select_freehand":
                    self.selection.select_freehand()

                elif action == "grow_selection":
                    self.selection.grow_selection()

                elif action == "shrink_selection":
                    self.selection.shrink_selection()

                elif action == "feather_selection":
                    self.selection.feather_selection()
                
                # Tools
                elif action == "activate_freehand_tool":
                    self.tools.activate_freehand_tool()

                elif action == "activate_line_tool":
                    self.tools.activate_line_tool()

                elif action == "activate_rectangle_tool":
                    self.tools.activate_rectangle_tool()

                elif action == "activate_ellipse_tool":
                    self.tools.activate_ellipse_tool()

                elif action == "activate_polygon_tool":
                    self.tools.activate_polygon_tool()

                elif action == "activate_bezier_tool":
                    self.tools.activate_bezier_tool()

                elif action == "activate_move_tool":
                    self.tools.activate_move_tool()

                elif action == "activate_transform_tool":
                    self.tools.activate_transform_tool()

                elif action == "activate_crop_tool":
                    self.tools.activate_crop_tool()

                elif action == "activate_fill_tool":
                    self.tools.activate_fill_tool()

                elif action == "activate_gradient_tool":
                    self.tools.activate_gradient_tool()

                elif action == "activate_color_picker":
                    self.tools.activate_color_picker()

                elif action == "activate_measure_tool":
                    self.tools.activate_measure_tool()

                elif action == "activate_multibrush_tool":
                    self.tools.activate_multibrush_tool()

                elif action == "activate_assistant_tool":
                    self.tools.activate_assistant_tool()

                elif action == "activate_reference_tool":
                    self.tools.activate_reference_tool()

            except Exception as e:
                import traceback
                print(e)
                traceback.print_exc()
