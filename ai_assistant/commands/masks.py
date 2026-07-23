from krita import Krita


class Masks:

    def __init__(self):
        self.app = Krita.instance()

    def _document(self):
        return self.app.activeDocument()

    def _node(self):
        doc = self._document()

        if doc is None:
            return None

        return doc.activeNode()

    # Create Transparency Mask
    def create_transparency_mask(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        name = cmd.get("name", "Transparency Mask")

        mask = doc.createTransparencyMask(name)

        if mask is None:
            return

        node.addChildNode(mask, None)

        doc.refreshProjection()
    

    # Create Selection Mask
    def create_selection_mask(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        name = cmd.get("name", "Selection Mask")

        mask = doc.createSelectionMask(name)

        if mask is None:
            return

        node.addChildNode(mask, None)

        doc.refreshProjection()
    

    # Create Colorize Mask
    def create_colorize_mask(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        name = cmd.get("name", "Colorize Mask")

        mask = doc.createColorizeMask(name)

        if mask is None:
            return

        node.addChildNode(mask, None)

        doc.refreshProjection()
    

    # Create Transform Mask
    def create_transform_mask(self, cmd):

        doc = self._document()
        node = self._node()

        if doc is None or node is None:
            return

        name = cmd.get("name", "Transform Mask")

        mask = doc.createTransformMask(name)

        if mask is None:
            return

        node.addChildNode(mask, None)

        doc.refreshProjection()
    

    # Rename Mask
    def rename_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        name = cmd.get("name", "Mask")

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setName(name)

                doc = self._document()

                if doc:
                    doc.refreshProjection()

                return
    

    # Remove Mask
    def remove_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.remove()

                if doc:
                    doc.refreshProjection()

                return

    # Duplicate Mask
    def duplicate_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                duplicate = child.duplicate()

                if duplicate is None:
                    return

                node.addChildNode(duplicate, None)

                if doc:
                    doc.refreshProjection()

                return


    # Lock Mask
    def lock_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setLocked(True)

                if doc:
                    doc.refreshProjection()

                return
    
    # Unlock Mask
    def unlock_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setLocked(False)

                if doc:
                    doc.refreshProjection()

                return
    

    # Hide Mask
    def hide_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setVisible(False)

                if doc:
                    doc.refreshProjection()

                return
    
    # Show Mask
    def show_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setVisible(True)

                if doc:
                    doc.refreshProjection()

                return
    

    # Set Mask Opacity
    def set_mask_opacity(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        opacity = int(cmd.get("opacity", 255))

        opacity = max(0, min(255, opacity))

        for child in node.childNodes():

            if "mask" in child.type().lower():

                child.setOpacity(opacity)

                if doc:
                    doc.refreshProjection()

                return
    
    # Move Mask
    def move_mask(self, cmd):

        node = self._node()

        if node is None:
            return

        doc = self._document()

        direction = cmd.get("direction", "up").lower()

        masks = []

        for child in node.childNodes():

            if "mask" in child.type().lower():
                masks.append(child)

        if len(masks) < 2:
            return

        target = masks[0]

        index = masks.index(target)

        if direction == "up":

            if index == 0:
                return

            target.move(masks[index - 1], False)

        elif direction == "down":

            if index >= len(masks) - 1:
                return

            target.move(masks[index + 1], True)

        if doc:
            doc.refreshProjection()