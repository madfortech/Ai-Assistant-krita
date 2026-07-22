from .actions import ActionExecutor


class Brushes:

    # Brush Size
    def increase_size(self):
        return ActionExecutor.trigger("increase_brush_size")

    def decrease_size(self):
        return ActionExecutor.trigger("decrease_brush_size")

    # Brush Opacity
    def increase_opacity(self):
        return ActionExecutor.trigger("increase_opacity")

    def decrease_opacity(self):
        return ActionExecutor.trigger("decrease_opacity")

    # Brush Flow
    def increase_flow(self):
        return ActionExecutor.trigger("increase_flow")

    def decrease_flow(self):
        return ActionExecutor.trigger("decrease_flow")

    # Brush Rotation
    def rotate_clockwise(self):
        return ActionExecutor.trigger("rotate_brush_tip_clockwise")

    def rotate_counter_clockwise(self):
        return ActionExecutor.trigger("rotate_brush_tip_counter_clockwise")

    # Brush Smoothing
    def smoothing_none(self):
        return ActionExecutor.trigger("set_no_brush_smoothing")

    def smoothing_basic(self):
        return ActionExecutor.trigger("set_simple_brush_smoothing")

    def smoothing_weighted(self):
        return ActionExecutor.trigger("set_weighted_brush_smoothing")

    def smoothing_stabilizer(self):
        return ActionExecutor.trigger("set_stabilizer_brush_smoothing")

    # Brush Presets
    def next_preset(self):
        return ActionExecutor.trigger("next_favorite_preset")

    def previous_preset(self):
        return ActionExecutor.trigger("previous_favorite_preset")

    def reload_preset(self):
        return ActionExecutor.trigger("reload_preset_action")

    # Brush Outline
    def toggle_outline(self):
        return ActionExecutor.trigger("toggle_brush_outline")