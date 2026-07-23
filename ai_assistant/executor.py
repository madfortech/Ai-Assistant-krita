#from .commands import Commands
from .commands.layers import Layers
from .commands.drawing import Commands
from .commands.brushes import Brushes
from .commands.selection import Selection
from .commands.tools import Tools
from .commands.illustration import Illustration
from .commands.workflow import Workflow
from .commands.assets import Assets
from .commands.brush_engine import BrushEngine
from .commands.filters import Filters
from .commands.masks import Masks
#from .commands.registry import COMMANDS

class Executor:

    def __init__(self):
        self.commands = Commands()
        self.brushes = Brushes()
        self.layers = Layers()
        self.selection = Selection()
        self.tools = Tools()
        self.illustration = Illustration()
        self.workflow = Workflow()
        self.assets = Assets()
        self.brush = BrushEngine()
        self.filters = Filters()
        self.masks = Masks()
    
    def execute(self, commands):

        if not commands:
            return

        for cmd in commands:

            action = cmd.get("action")

            if not action:
                continue

            try:

                if self.workflow.run(action, cmd):
                    continue

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

                # Selection Tools
                elif action == "select_rectangle":
                    self.selection.select_rectangle()
                
                # Select All
                elif action == "select_all":
                    self.selection.select_all()
                
                # Deselect
                elif action == "deselect":
                    self.selection.deselect()
                
                # Invert Selection
                elif action == "invert_selection":
                    self.selection.invert_selection()
                
                # Select Ellipse
                elif action == "select_ellipse":
                    self.selection.select_ellipse()
                
                # Select Polygon
                elif action == "select_polygon":
                    self.selection.select_polygon()
                
                # Select Freehand
                elif action == "select_freehand":
                    self.selection.select_freehand()
                
                # Grow Selection
                elif action == "grow_selection":
                    self.selection.grow_selection()
                
                # Shrink Selection
                elif action == "shrink_selection":
                    self.selection.shrink_selection()
                
                # Feather Selection
                elif action == "feather_selection":
                    self.selection.feather_selection()
                
                # Tools
                elif action == "activate_freehand_tool":
                    self.tools.activate_freehand_tool()

                # Line Tool
                elif action == "activate_line_tool":
                    self.tools.activate_line_tool()

                # Rectangle Tool
                elif action == "activate_rectangle_tool":
                    self.tools.activate_rectangle_tool()

                # Ellipse Tool
                elif action == "activate_ellipse_tool":
                    self.tools.activate_ellipse_tool()

                # Polygon Tool
                elif action == "activate_polygon_tool":
                    self.tools.activate_polygon_tool()

                # Bezier Tool
                elif action == "activate_bezier_tool":
                    self.tools.activate_bezier_tool()

                # Move Tool
                elif action == "activate_move_tool":
                    self.tools.activate_move_tool()

                # Transform Tool
                elif action == "activate_transform_tool":
                    self.tools.activate_transform_tool()

                # Crop Tool
                elif action == "activate_crop_tool":
                    self.tools.activate_crop_tool()

                # Fill Tool
                elif action == "activate_fill_tool":
                    self.tools.activate_fill_tool()

                # Gradient Tool
                elif action == "activate_gradient_tool":
                    self.tools.activate_gradient_tool()

                # Color Picker Tool
                elif action == "activate_color_picker":
                    self.tools.activate_color_picker()

                # Measure Tool
                elif action == "activate_measure_tool":
                    self.tools.activate_measure_tool()

                # Multibrush Tool
                elif action == "activate_multibrush_tool":
                    self.tools.activate_multibrush_tool()

                # Assistant Tool
                elif action == "activate_assistant_tool":
                    self.tools.activate_assistant_tool()

                # Reference Tool
                elif action == "activate_reference_tool":
                    self.tools.activate_reference_tool()

                # Drawing Commands
                elif action == "draw_triangle":
                    self.commands.draw_triangle(cmd)

                # Cross Drawing
                elif action == "draw_cross":
                    self.commands.draw_cross(cmd)

                # Arrow Drawing
                elif action == "draw_arrow":
                    self.commands.draw_arrow(cmd)

                # Grid Drawing
                elif action == "draw_grid":
                    self.commands.draw_grid(cmd)

                # Round Rectangle Drawing
                elif action == "draw_round_rectangle":
                    self.commands.draw_round_rectangle(cmd)

                # Freehand Drawing
                elif action == "draw_freehand":
                    self.commands.draw_freehand(cmd)

                # Brush Stroke Drawing
                elif action == "draw_brush_stroke":
                    self.brush.stroke(cmd)

                # Dashed Line Drawing
                elif action == "draw_dashed_line":
                    self.commands.draw_dashed_line(cmd)

                # Dotted Line Drawing
                elif action == "draw_dotted_line":
                    self.commands.draw_dotted_line(cmd)

                # Erase Area
                elif action == "erase_area":
                    self.commands.erase_area(cmd)

                # Fill Selection
                elif action == "fill_selection":
                    self.commands.fill_selection(cmd)

                # Filters

                elif action == "apply_gaussian_blur":
                    self.filters.apply_gaussian_blur(cmd)

                elif action == "apply_motion_blur":
                    self.filters.apply_motion_blur(cmd)

                elif action == "apply_sharpen":
                    self.filters.apply_sharpen(cmd)

                elif action == "apply_unsharp":
                    self.filters.apply_unsharp(cmd)

                elif action == "apply_hsv_adjustment":
                    self.filters.apply_hsv_adjustment(cmd)

                elif action == "apply_levels":
                    self.filters.apply_levels(cmd)

                elif action == "apply_color_balance":
                    self.filters.apply_color_balance(cmd)

                elif action == "apply_invert":
                    self.filters.apply_invert(cmd)

                elif action == "apply_posterize":
                    self.filters.apply_posterize(cmd)

                elif action == "apply_pixelize":
                    self.filters.apply_pixelize(cmd)

                # Masks

                elif action == "create_transparency_mask":
                    self.masks.create_transparency_mask(cmd)

                elif action == "create_selection_mask":
                    self.masks.create_selection_mask(cmd)
                
                elif action == "create_colorize_mask":
                    self.masks.create_colorize_mask(cmd)
                
                elif action == "create_transform_mask":
                    self.masks.create_transform_mask(cmd)
                
                elif action == "rename_mask":
                    self.masks.rename_mask(cmd)
                
                elif action == "remove_mask":
                    self.masks.remove_mask(cmd)

                elif action == "duplicate_mask":
                    self.masks.duplicate_mask(cmd)
                
                elif action == "lock_mask":
                    self.masks.lock_mask(cmd)
                
                elif action == "unlock_mask":
                    self.masks.unlock_mask(cmd)

                elif action == "hide_mask":
                    self.masks.hide_mask(cmd)

                elif action == "show_mask":
                    self.masks.show_mask(cmd)

                elif action == "set_mask_opacity":
                    self.masks.set_mask_opacity(cmd)
                
                elif action == "move_mask":
                    self.masks.move_mask(cmd)
    
                # Illustration Commands

                # Geometric Shapes
                elif action == "draw_house":
                    self.illustration.draw_house(cmd)

                # Buildings
                elif action == "draw_hut":
                    self.illustration.draw_hut(cmd)

                # Castles
                elif action == "draw_castle":
                    self.illustration.draw_castle(cmd)

                # Bridges
                elif action == "draw_bridge":
                    self.illustration.draw_bridge(cmd)

                # Trees
                elif action == "draw_tree":
                    self.illustration.draw_tree(cmd)

                # Clouds
                elif action == "draw_cloud":
                    self.illustration.draw_cloud(cmd)

                # Sun
                elif action == "draw_sun":
                    self.illustration.draw_sun(cmd)

                # Flowers
                elif action == "draw_flower":
                    self.illustration.draw_flower(cmd)

                # Moon
                elif action == "draw_moon":
                    self.illustration.draw_moon(cmd)

                # Mountains
                elif action == "draw_mountain":
                    self.illustration.draw_mountain(cmd)

                # Faces
                elif action == "draw_face":
                    self.illustration.draw_face(cmd)

                # Eyes
                elif action == "draw_eye":
                    self.illustration.draw_eye(cmd)

                # Nose
                elif action == "draw_nose":
                    self.illustration.draw_nose(cmd)

                # Mouth
                elif action == "draw_mouth":
                    self.illustration.draw_mouth(cmd)

                # People
                elif action == "draw_person":
                    self.illustration.draw_person(cmd)

                # Cats
                elif action == "draw_cat":
                    self.illustration.draw_cat(cmd)

                # Dogs
                elif action == "draw_dog":
                    self.illustration.draw_dog(cmd)

                # Fish
                elif action == "draw_fish":
                    self.illustration.draw_fish(cmd)

                # Birds
                elif action == "draw_bird":
                    self.illustration.draw_bird(cmd)

                # Cars
                elif action == "draw_car":
                    self.illustration.draw_car(cmd)

                # Bikes
                elif action == "draw_bike":
                    self.illustration.draw_bike(cmd)

                # Boats
                elif action == "draw_boat":
                    self.illustration.draw_boat(cmd)

                # Airplanes
                elif action == "draw_airplane":
                    self.illustration.draw_airplane(cmd)

                # Coins
                elif action == "draw_coin":
                    self.illustration.draw_coin(cmd)

                # Hearts
                elif action == "draw_heart":
                    self.illustration.draw_heart(cmd)

                # Stars
                elif action == "draw_star":
                    self.illustration.draw_star(cmd)

                # Swords
                elif action == "draw_sword":
                    self.illustration.draw_sword(cmd)

                # Shields
                elif action == "draw_shield":
                    self.illustration.draw_shield(cmd)

                # Chests
                elif action == "draw_chest":
                    self.illustration.draw_chest(cmd)


                # Unknown Action
                else:
                    print(f"Unknown action: {action}")

            except Exception as e:
                import traceback
                print(e)
                traceback.print_exc()
            

