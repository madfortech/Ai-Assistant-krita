from .actions import ActionExecutor


class Tools:

    def activate_freehand_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolBrush")

    def activate_line_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolLine")

    def activate_rectangle_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolRectangle")

    def activate_ellipse_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolEllipse")

    def activate_polygon_tool(self):
        return ActionExecutor.trigger("KisToolPolygon")

    def activate_bezier_tool(self):
        return ActionExecutor.trigger("KisToolPath")

    def activate_move_tool(self):
        return ActionExecutor.trigger("KritaTransform/KisToolMove")

    def activate_transform_tool(self):
        return ActionExecutor.trigger("KisToolTransform")

    def activate_crop_tool(self):
        return ActionExecutor.trigger("KisToolCrop")

    def activate_fill_tool(self):
        return ActionExecutor.trigger("KritaFill/KisToolFill")

    def activate_gradient_tool(self):
        return ActionExecutor.trigger("KritaFill/KisToolGradient")

    def activate_color_picker(self):
        return ActionExecutor.trigger("KritaSelected/KisToolColorSampler")

    def activate_measure_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolMeasure")

    def activate_multibrush_tool(self):
        return ActionExecutor.trigger("KritaShape/KisToolMultiBrush")

    def activate_assistant_tool(self):
        return ActionExecutor.trigger("KisAssistantTool")

    def activate_reference_tool(self):
        return ActionExecutor.trigger("ToolReferenceImages")