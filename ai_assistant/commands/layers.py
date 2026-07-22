from .actions import ActionExecutor


class Layers:

    # Create Layers
    def add_paint_layer(self):
        return ActionExecutor.trigger("add_new_paint_layer")

    def add_group_layer(self):
        return ActionExecutor.trigger("add_new_group_layer")

    def add_vector_layer(self):
        return ActionExecutor.trigger("add_new_shape_layer")

    def add_fill_layer(self):
        return ActionExecutor.trigger("add_new_fill_layer")

    def add_filter_layer(self):
        return ActionExecutor.trigger("add_new_adjustment_layer")

    def add_clone_layer(self):
        return ActionExecutor.trigger("add_new_clone_layer")

    # Layer Operations
    def duplicate(self):
        return ActionExecutor.trigger("duplicatelayer")

    def merge(self):
        return ActionExecutor.trigger("merge_layer")

    def flatten(self):
        return ActionExecutor.trigger("flatten_layer")

    def remove(self):
        return ActionExecutor.trigger("remove_layer")

    # Layer Order
    def move_up(self):
        return ActionExecutor.trigger("move_layer_up")

    def move_down(self):
        return ActionExecutor.trigger("move_layer_down")

    # Layer Visibility
    def toggle_visibility(self):
        return ActionExecutor.trigger("toggle_layer_visibility")

    # Layer Lock
    def toggle_lock(self):
        return ActionExecutor.trigger("toggle_layer_lock")

    # Alpha Lock
    def toggle_alpha_lock(self):
        return ActionExecutor.trigger("toggle_layer_alpha_lock")

    # Alpha Inheritance
    def toggle_alpha_inheritance(self):
        return ActionExecutor.trigger("toggle_layer_inherit_alpha")