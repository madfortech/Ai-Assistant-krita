from .actions import ActionExecutor


class Selection:

    # Rectangle Selection
    def select_rectangle(self):
        return ActionExecutor.trigger("select_rectangle")

    # Ellipse Selection
    def select_ellipse(self):
        return ActionExecutor.trigger("select_ellipse")

    # Polygon Selection
    def select_polygon(self):
        return ActionExecutor.trigger("select_polygon")

    # Freehand Selection
    def select_freehand(self):
        return ActionExecutor.trigger("select_freehand")

    # Select All
    def select_all(self):
        return ActionExecutor.trigger("select_all")

    # Deselect
    def deselect(self):
        return ActionExecutor.trigger("deselect")

    # Invert Selection
    def invert_selection(self):
        return ActionExecutor.trigger("invert_selection")

    # Feather Selection
    def feather_selection(self):
        return ActionExecutor.trigger("feather_selection")

    # Grow Selection
    def grow_selection(self):
        return ActionExecutor.trigger("grow_selection")

    # Shrink Selection
    def shrink_selection(self):
        return ActionExecutor.trigger("shrink_selection")