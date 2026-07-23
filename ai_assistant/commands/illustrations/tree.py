import math
import random
from krita import Krita  # For any future extensions


class TreeIllustration:
    """
    Procedural realistic tree generator.
    Uses layered primitives for trunk, branches, and organic canopy.
    """

    def __init__(self):
        self.commands = None  # Will be set by parent Illustration class

    def _set_color(self, color: str):
        """Helper to set foreground color."""
        self.commands.set_color({"color": color})

    def draw_tree(self, cmd: dict):
        """
        Draw a realistic tree with configurable position and size.
        
        Args in cmd:
            x, y: base position (trunk center)
            trunk_width, trunk_height: trunk dimensions
            crown_radius: overall canopy size multiplier
        """
        x = cmd.get("x", 300)
        y = cmd.get("y", 150)
        trunk_width = cmd.get("trunk_width", 42)
        trunk_height = cmd.get("trunk_height", 165)
        crown_scale = cmd.get("crown_radius", 34) / 34.0  # Normalize

        center_x = x + trunk_width // 2
        trunk_top = y + 95
        trunk_bottom = trunk_top + trunk_height

        # Color palettes
        bark_colors = ["#5B3A1D", "#6B4423", "#7A4E2C", "#8B5A2B"]
        leaf_colors = {
            "top": ["#66BB6A", "#81C784", "#4CAF50"],
            "middle": ["#388E3C", "#43A047", "#4CAF50"],
            "dark": ["#1B5E20", "#2E7D32", "#33691E"]
        }
        grass_color = "#2E7D32"
        shadow_color = "#1B5E20"

        # ========================= TRUNK =========================
        self._set_color(bark_colors[1])
        self.commands.draw_rectangle({
            "from": [x, trunk_top],
            "to": [x + trunk_width, trunk_bottom]
        })

        # Inner bark layer
        self._set_color(bark_colors[2])
        self.commands.draw_rectangle({
            "from": [x + 8, trunk_top + 15],
            "to": [x + trunk_width - 8, trunk_bottom]
        })

        # Bark texture
        self._set_color(bark_colors[0])
        for yy in range(trunk_top + 8, trunk_bottom - 8, 12):
            xx = center_x + random.randint(-10, 10)
            self.commands.draw_line({
                "from": [xx, yy],
                "to": [xx + random.randint(-3, 3), yy + random.randint(6, 12)]
            })

        # ========================= ROOTS =========================
        self._set_color(bark_colors[0])
        roots = [(-32, 18), (-20, 12), (20, 12), (32, 18), (0, 22)]
        for dx, dy in roots:
            self.commands.draw_line({
                "from": [center_x, trunk_bottom],
                "to": [center_x + dx, trunk_bottom + dy]
            })

        # ========================= BRANCHES =========================
        branch_start_y = trunk_top + 25
        main_branches = [
            (-90, -70), (90, -70),
            (-75, -35), (75, -35),
            (-55, 0),   (55, 0),
            (-40, 25),  (40, 25),
            (-25, 45),  (25, 45)
        ]

        self._set_color(bark_colors[1])
        for dx, dy in main_branches:
            self.commands.draw_line({
                "from": [center_x, branch_start_y],
                "to": [center_x + dx, branch_start_y + dy]
            })

        # Secondary branches
        for dx, dy in main_branches:
            bx = center_x + dx
            by = branch_start_y + dy
            for _ in range(4):
                ex = bx + random.randint(-35, 35)
                ey = by + random.randint(-35, 20)
                self.commands.draw_line({
                    "from": [bx, by],
                    "to": [ex, ey]
                })

        # ========================= CANOPY =========================
        canopy_cx = center_x
        canopy_cy = y + 35
        canopy_rx = int(95 * crown_scale)
        canopy_ry = int(85 * crown_scale)

        for _ in range(380):  # More leaves for density
            angle = random.uniform(0, 2 * math.pi)
            radius_factor = random.random() ** 0.55

            px = canopy_cx + int(canopy_rx * radius_factor * math.cos(angle))
            py = canopy_cy + int(canopy_ry * radius_factor * math.sin(angle))

            if random.random() < 0.11:  # Natural gaps
                continue

            leaf_size = random.randint(13, 29)

            # Color variation by height
            if py < canopy_cy - 10:
                color = random.choice(leaf_colors["top"])
            elif py > canopy_cy + 25:
                color = random.choice(leaf_colors["dark"])
            else:
                color = random.choice(leaf_colors["middle"])

            self._set_color(color)
            self.commands.draw_circle({
                "from": [px, py],
                "to": [px + leaf_size, py + leaf_size]
            })

        # Top highlights
        self._set_color("#A5D6A7")
        for _ in range(50):
            px = center_x + random.randint(-70, 70)
            py = y + random.randint(-25, 35)
            self.commands.draw_circle({
                "from": [px, py],
                "to": [px + 13, py + 13]
            })

        # ========================= GROUND DETAILS =========================
        # Grass
        self._set_color(grass_color)
        for i in range(95):
            gx = x - 75 + i * 2
            height = random.randint(8, 22)
            self.commands.draw_line({
                "from": [gx, trunk_bottom],
                "to": [gx + random.randint(-3, 3), trunk_bottom - height]
            })

        # Ground shadow
        self._set_color(shadow_color)
        for i in range(40):
            self.commands.draw_line({
                "from": [center_x - 48 + i, trunk_bottom + 6],
                "to": [center_x - 22 + i, trunk_bottom + 18]
            })

        return True