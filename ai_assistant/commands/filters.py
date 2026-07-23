from krita import Krita

class Filters:

    def __init__(self):
        self.app = Krita.instance()

    def _document(self):
        return self.app.activeDocument()


    def _node(self):
        doc = self._document()

        if not doc:
            return None

        return doc.activeNode()
    
    # Filters  gaussian blur
    def apply_gaussian_blur(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        radius = int(cmd.get("radius", 5))

        blur = self.app.filter("gaussian blur")

        if blur is None:
            return

        cfg = blur.configuration()

        cfg.setProperty("horizRadius", radius)
        cfg.setProperty("vertRadius", radius)
        cfg.setProperty("lockAspect", True)

        blur.setConfiguration(cfg)

        bounds = node.bounds()

        blur.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()

    
    # Filters  motion blur
    def apply_motion_blur(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        angle = float(cmd.get("angle", 0))
        length = int(cmd.get("length", 5))

        blur = self.app.filter("motion blur")

        if blur is None:
            return

        cfg = blur.configuration()

        cfg.setProperty("blurAngle", angle)
        cfg.setProperty("blurLength", length)

        blur.setConfiguration(cfg)

        bounds = node.bounds()

        blur.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()

    # Filters  sharpen
    def apply_sharpen(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        sharpen = self.app.filter("sharpen")

        if sharpen is None:
            return

        bounds = node.bounds()

        sharpen.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters  unsharp
    def apply_unsharp(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        amount = float(cmd.get("amount", 0.5))
        half_size = int(cmd.get("half_size", 1))
        threshold = int(cmd.get("threshold", 0))
        lightness_only = bool(cmd.get("lightness_only", True))

        unsharp = self.app.filter("unsharp")

        if unsharp is None:
            return

        cfg = unsharp.configuration()

        cfg.setProperty("amount", amount)
        cfg.setProperty("halfSize", half_size)
        cfg.setProperty("threshold", threshold)
        cfg.setProperty("lightnessOnly", lightness_only)

        unsharp.setConfiguration(cfg)

        bounds = node.bounds()

        unsharp.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters  hsv adjustment
    def apply_hsv_adjustment(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        hue = int(cmd.get("h", 0))
        saturation = int(cmd.get("s", 0))
        value = int(cmd.get("v", 0))
        colorize = bool(cmd.get("colorize", False))
        compatibility = bool(cmd.get("compatibility_mode", False))
        adjustment_type = int(cmd.get("type", 1))

        hsv = self.app.filter("hsvadjustment")

        if hsv is None:
            return

        cfg = hsv.configuration()

        cfg.setProperty("colorize", colorize)
        cfg.setProperty("compatibilityMode", compatibility)
        cfg.setProperty("h", hue)
        cfg.setProperty("s", saturation)
        cfg.setProperty("type", adjustment_type)
        cfg.setProperty("v", value)

        hsv.setConfiguration(cfg)

        bounds = node.bounds()

        hsv.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters  levels
    def apply_levels(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        levels = self.app.filter("levels")

        if levels is None:
            return

        cfg = levels.configuration()

        cfg.setProperty("blackvalue", int(cmd.get("blackvalue", 0)))
        cfg.setProperty("whitevalue", int(cmd.get("whitevalue", 255)))
        cfg.setProperty("gammavalue", float(cmd.get("gammavalue", 1.0)))
        cfg.setProperty("outblackvalue", int(cmd.get("outblackvalue", 0)))
        cfg.setProperty("outwhitevalue", int(cmd.get("outwhitevalue", 255)))

        cfg.setProperty("histogram_mode", cmd.get("histogram_mode", "linear"))
        cfg.setProperty("mode", cmd.get("mode", "lightness"))
        cfg.setProperty("lightness", cmd.get("lightness", "0;1;1;0;1"))
        cfg.setProperty("number_of_channels", int(cmd.get("number_of_channels", 0)))

        levels.setConfiguration(cfg)

        bounds = node.bounds()

        levels.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters color balance
    def apply_color_balance(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        color_balance = self.app.filter("colorbalance")

        if color_balance is None:
            return

        cfg = color_balance.configuration()

        cfg.setProperty(
            "cyan_red_highlights",
            int(cmd.get("cyan_red_highlights", 0))
        )

        cfg.setProperty(
            "cyan_red_midtones",
            int(cmd.get("cyan_red_midtones", 0))
        )

        cfg.setProperty(
            "cyan_red_shadows",
            int(cmd.get("cyan_red_shadows", 0))
        )

        cfg.setProperty(
            "magenta_blue_highlights",
            int(cmd.get("magenta_blue_highlights", 0))
        )

        cfg.setProperty(
            "magenta_blue_midtones",
            int(cmd.get("magenta_blue_midtones", 0))
        )

        cfg.setProperty(
            "magenta_blue_shadows",
            int(cmd.get("magenta_blue_shadows", 0))
        )

        cfg.setProperty(
            "yellow_green_highlights",
            int(cmd.get("yellow_green_highlights", 0))
        )

        cfg.setProperty(
            "yellow_green_midtones",
            int(cmd.get("yellow_green_midtones", 0))
        )

        cfg.setProperty(
            "yellow_green_shadows",
            int(cmd.get("yellow_green_shadows", 0))
        )

        cfg.setProperty(
            "preserve_luminosity",
            bool(cmd.get("preserve_luminosity", True))
        )

        color_balance.setConfiguration(cfg)

        bounds = node.bounds()

        color_balance.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters invert
    def apply_invert(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        invert = self.app.filter("invert")

        if invert is None:
            return

        bounds = node.bounds()

        invert.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters posterize
    def apply_posterize(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        posterize = self.app.filter("posterize")

        if posterize is None:
            return

        cfg = posterize.configuration()

        cfg.setProperty(
            "steps",
            int(cmd.get("steps", 16))
        )

        posterize.setConfiguration(cfg)

        bounds = node.bounds()

        posterize.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()
    
    # Filters pixelize
    def apply_pixelize(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        pixelize = self.app.filter("pixelize")

        if pixelize is None:
            return

        width = int(cmd.get("pixel_width", 10))
        height = int(cmd.get("pixel_height", 10))
        keep_aspect = bool(cmd.get("keep_aspect", True))

        cfg = pixelize.configuration()

        cfg.setProperty("pixelWidth", width)
        cfg.setProperty("pixelHeight", height)
        cfg.setProperty("keepAspect", keep_aspect)

        pixelize.setConfiguration(cfg)

        bounds = node.bounds()

        pixelize.apply(
            node,
            bounds.x(),
            bounds.y(),
            bounds.width(),
            bounds.height()
        )

        doc.refreshProjection()