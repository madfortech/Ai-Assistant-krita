from .drawing import Commands
from .illustrations import TreeIllustration

class Illustration(TreeIllustration):
    """
    High-level illustration helper.

    This class builds complex illustrations by combining
    primitive drawing commands from drawing.py.

    Example:
        House
            -> draw_rectangle()
            -> draw_triangle()
            -> draw_rectangle()

        Tree
            -> draw_rectangle()
            -> draw_circle()
            -> draw_circle()

        Car
            -> draw_rectangle()
            -> draw_circle()
            -> draw_polygon()
    """

    
    def __init__(self):
        self.commands = Commands()

    # -------------------------------------------------
    # Buildings
    # -------------------------------------------------

    def draw_house(self, cmd):

        body = {
            "from": [180, 220],
            "to": [420, 420]
        }

        roof = {
            "points": [
                [300, 100],
                [450, 220],
                [150, 220]
            ]
        }

        door = {
            "from": [270, 320],
            "to": [330, 420]
        }

        left_window = {
            "from": [210, 260],
            "to": [260, 310]
        }

        right_window = {
            "from": [340, 260],
            "to": [390, 310]
        }

        self.commands.draw_rectangle(body)
        self.commands.draw_triangle(roof)
        self.commands.draw_rectangle(door)
        self.commands.draw_rectangle(left_window)
        self.commands.draw_rectangle(right_window)

    
    # draw castle with towers and walls
    def draw_castle(self, cmd):

        x = cmd.get("x", 250)
        y = cmd.get("y", 180)

        width = cmd.get("width", 260)
        height = cmd.get("height", 180)

        tower_width = cmd.get("tower_width", 50)
        tower_height = cmd.get("tower_height", 220)

        gate_width = cmd.get("gate_width", 60)
        gate_height = cmd.get("gate_height", 90)

        # Left Tower
        left_tower = {
            "from": [x, y],
            "to": [x + tower_width, y + tower_height]
        }

        # Right Tower
        right_tower = {
            "from": [x + width - tower_width, y],
            "to": [x + width, y + tower_height]
        }

        # Main Building
        center = {
            "from": [
                x + tower_width,
                y + 40
            ],
            "to": [
                x + width - tower_width,
                y + height
            ]
        }

        # Left Tower Roof
        left_roof = {
            "points": [
                [x, y],
                [x + tower_width // 2, y - 40],
                [x + tower_width, y]
            ]
        }

        # Right Tower Roof
        right_roof = {
            "points": [
                [x + width - tower_width, y],
                [x + width - tower_width // 2, y - 40],
                [x + width, y]
            ]
        }

        # Castle Gate
        gate = {
            "from": [
                x + width // 2 - gate_width // 2,
                y + height - gate_height
            ],
            "to": [
                x + width // 2 + gate_width // 2,
                y + height
            ]
        }

        # Left Window
        left_window = {
            "from": [
                x + 20,
                y + 70
            ],
            "to": [
                x + 35,
                y + 90
            ]
        }

        # Right Window
        right_window = {
            "from": [
                x + width - 35,
                y + 70
            ],
            "to": [
                x + width - 20,
                y + 90
            ]
        }

        # Center Window
        center_window = {
            "from": [
                x + width // 2 - 10,
                y + 70
            ],
            "to": [
                x + width // 2 + 10,
                y + 90
            ]
        }

        self.commands.draw_rectangle(left_tower)
        self.commands.draw_rectangle(right_tower)
        self.commands.draw_rectangle(center)

        self.commands.draw_triangle(left_roof)
        self.commands.draw_triangle(right_roof)

        self.commands.draw_rectangle(gate)

        self.commands.draw_rectangle(left_window)
        self.commands.draw_rectangle(right_window)
        self.commands.draw_rectangle(center_window)

    # draw bridge with arches and railing
    def draw_bridge(self, cmd):

        x = cmd.get("x", 200)
        y = cmd.get("y", 250)

        width = cmd.get("width", 300)
        deck_height = cmd.get("deck_height", 20)

        tower_height = cmd.get("tower_height", 120)
        tower_width = cmd.get("tower_width", 20)

        # Bridge Deck
        deck = {
            "from": [x, y],
            "to": [x + width, y + deck_height]
        }

        # Left Tower
        left_tower = {
            "from": [
                x + width // 4 - tower_width // 2,
                y - tower_height
            ],
            "to": [
                x + width // 4 + tower_width // 2,
                y
            ]
        }

        # Right Tower
        right_tower = {
            "from": [
                x + (3 * width) // 4 - tower_width // 2,
                y - tower_height
            ],
            "to": [
                x + (3 * width) // 4 + tower_width // 2,
                y
            ]
        }

        self.commands.draw_rectangle(deck)
        self.commands.draw_rectangle(left_tower)
        self.commands.draw_rectangle(right_tower)

        # Suspension Cables
        self.commands.draw_line({
            "from": [x, y],
            "to": [x + width // 4, y - tower_height]
        })

        self.commands.draw_line({
            "from": [x + width // 4, y - tower_height],
            "to": [x + width // 2, y]
        })

        self.commands.draw_line({
            "from": [x + width // 2, y],
            "to": [x + (3 * width) // 4, y - tower_height]
        })

        self.commands.draw_line({
            "from": [x + (3 * width) // 4, y - tower_height],
            "to": [x + width, y]
        })

        # Vertical Suspension Cables
        for i in range(6):
            px = x + (i * width // 5)

            self.commands.draw_line({
                "from": [px, y],
                "to": [px, y - 40]
            })

     
   
   
    # draw sun with rays
    def draw_sun(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 150)

        radius = cmd.get("radius", 40)
        ray_length = cmd.get("ray_length", 30)

        # Sun Body
        sun = {
            "from": [
                x - radius,
                y - radius
            ],
            "to": [
                x + radius,
                y + radius
            ]
        }

        self.commands.draw_circle(sun)

        # Rays
        rays = [
            ([x, y - radius], [x, y - radius - ray_length]),                 # Top
            ([x, y + radius], [x, y + radius + ray_length]),                 # Bottom
            ([x - radius, y], [x - radius - ray_length, y]),                 # Left
            ([x + radius, y], [x + radius + ray_length, y]),                 # Right
            ([x - radius, y - radius], [x - radius - 20, y - radius - 20]), # Top Left
            ([x + radius, y - radius], [x + radius + 20, y - radius - 20]), # Top Right
            ([x - radius, y + radius], [x - radius - 20, y + radius + 20]), # Bottom Left
            ([x + radius, y + radius], [x + radius + 20, y + radius + 20])  # Bottom Right
        ]

        for start, end in rays:
            self.commands.draw_line({
                "from": start,
                "to": end
            })
    

    # draw cloud
    def draw_cloud(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 150)

        width = cmd.get("width", 180)
        height = cmd.get("height", 80)

        # Left Cloud
        left = {
            "from": [
                x,
                y + height // 4
            ],
            "to": [
                x + width // 3,
                y + height
            ]
        }

        # Center Cloud
        center = {
            "from": [
                x + width // 4,
                y
            ],
            "to": [
                x + width // 4 + width // 3,
                y + height
            ]
        }

        # Right Cloud
        right = {
            "from": [
                x + width // 2,
                y + height // 4
            ],
            "to": [
                x + width // 2 + width // 3,
                y + height
            ]
        }

        # Bottom Cloud
        bottom = {
            "from": [
                x + width // 6,
                y + height // 2
            ],
            "to": [
                x + width // 6 + width // 2,
                y + height + height // 3
            ]
        }

        self.commands.draw_circle(left)
        self.commands.draw_circle(center)
        self.commands.draw_circle(right)
        self.commands.draw_circle(bottom)

    # draw flower with petals and stem
    def draw_flower(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 200)

        petal_radius = cmd.get("petal_radius", 25)
        center_radius = cmd.get("center_radius", 18)

        stem_height = cmd.get("stem_height", 120)

        # Flower Center
        center = {
            "from": [
                x - center_radius,
                y - center_radius
            ],
            "to": [
                x + center_radius,
                y + center_radius
            ]
        }

        # Petals
        top = {
            "from": [x - petal_radius, y - 2 * petal_radius],
            "to": [x + petal_radius, y]
        }

        bottom = {
            "from": [x - petal_radius, y],
            "to": [x + petal_radius, y + 2 * petal_radius]
        }

        left = {
            "from": [x - 2 * petal_radius, y - petal_radius],
            "to": [x, y + petal_radius]
        }

        right = {
            "from": [x, y - petal_radius],
            "to": [x + 2 * petal_radius, y + petal_radius]
        }

        top_left = {
            "from": [x - int(1.5 * petal_radius), y - int(1.5 * petal_radius)],
            "to": [x, y]
        }

        top_right = {
            "from": [x, y - int(1.5 * petal_radius)],
            "to": [x + int(1.5 * petal_radius), y]
        }

        # Stem
        stem = {
            "from": [x, y + center_radius],
            "to": [x, y + stem_height]
        }

        # Leaves
        left_leaf = {
            "points": [
                [x, y + 60],
                [x - 30, y + 80],
                [x, y + 90]
            ]
        }

        right_leaf = {
            "points": [
                [x, y + 80],
                [x + 30, y + 60],
                [x, y + 100]
            ]
        }

        self.commands.draw_circle(top)
        self.commands.draw_circle(bottom)
        self.commands.draw_circle(left)
        self.commands.draw_circle(right)
        self.commands.draw_circle(top_left)
        self.commands.draw_circle(top_right)
        self.commands.draw_circle(center)

        self.commands.draw_line(stem)

        self.commands.draw_triangle(left_leaf)
        self.commands.draw_triangle(right_leaf) 


    # -------------------------------------------------
    # Nature
    # -------------------------------------------------

    # draw moon with crescent effect
    def draw_moon(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 180)

        radius = cmd.get("radius", 50)
        offset = cmd.get("offset", 20)

        # Outer Moon
        outer = {
            "from": [
                x - radius,
                y - radius
            ],
            "to": [
                x + radius,
                y + radius
            ]
        }

        # Inner Cut (creates crescent effect)
        inner = {
            "from": [
                x - radius + offset,
                y - radius
            ],
            "to": [
                x + radius + offset,
                y + radius
            ]
        }

        self.commands.draw_circle(outer)
        self.commands.draw_circle(inner)

    # draw mountain with peak
    def draw_mountain(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 350)

        width = cmd.get("width", 220)
        height = cmd.get("height", 180)

        peak_count = cmd.get("peak_count", 3)

        if peak_count < 1:
            peak_count = 1

        peak_width = width // peak_count

        for i in range(peak_count):

            px = x + i * peak_width

            mountain = {
                "points": [
                    [px, y],
                    [px + peak_width // 2, y - height],
                    [px + peak_width, y]
                ]
            }

            self.commands.draw_triangle(mountain)

    # -------------------------------------------------
    # Characters
    # -------------------------------------------------

    # draw eye
    def draw_eye(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 200)

        width = cmd.get("width", 50)
        height = cmd.get("height", 25)

        pupil_radius = cmd.get("pupil_radius", 6)

        # Eye Outline
        eye = {
            "from": [
                x - width // 2,
                y - height // 2
            ],
            "to": [
                x + width // 2,
                y + height // 2
            ]
        }

        # Iris
        iris = {
            "from": [
                x - pupil_radius * 2,
                y - pupil_radius * 2
            ],
            "to": [
                x + pupil_radius * 2,
                y + pupil_radius * 2
            ]
        }

        # Pupil
        pupil = {
            "from": [
                x - pupil_radius,
                y - pupil_radius
            ],
            "to": [
                x + pupil_radius,
                y + pupil_radius
            ]
        }

        # Upper Eyelid
        upper_lid = {
            "from": [
                x - width // 2,
                y
            ],
            "to": [
                x + width // 2,
                y
            ]
        }

        # Eyebrow
        eyebrow = {
            "from": [
                x - width // 2,
                y - height - 10
            ],
            "to": [
                x + width // 2,
                y - height - 15
            ]
        }

        self.commands.draw_ellipse(eye)
        self.commands.draw_circle(iris)
        self.commands.draw_circle(pupil)
        self.commands.draw_line(upper_lid)
        self.commands.draw_line(eyebrow)

    # draw nose
    def draw_nose(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 220)

        width = cmd.get("width", 20)
        height = cmd.get("height", 35)

        nostril_size = cmd.get("nostril_size", 4)

        # Nose Bridge
        self.commands.draw_line({
            "from": [x, y - height // 2],
            "to": [x, y + height // 2]
        })

        # Nose Tip
        tip = {
            "points": [
                [x - width // 2, y + height // 2],
                [x + width // 2, y + height // 2],
                [x, y + height // 2 + 10]
            ]
        }

        # Left Nostril
        left_nostril = {
            "from": [
                x - width // 3 - nostril_size,
                y + height // 2 + 8 - nostril_size
            ],
            "to": [
                x - width // 3 + nostril_size,
                y + height // 2 + 8 + nostril_size
            ]
        }

        # Right Nostril
        right_nostril = {
            "from": [
                x + width // 3 - nostril_size,
                y + height // 2 + 8 - nostril_size
            ],
            "to": [
                x + width // 3 + nostril_size,
                y + height // 2 + 8 + nostril_size
            ]
        }

        self.commands.draw_triangle(tip)
        self.commands.draw_circle(left_nostril)
        self.commands.draw_circle(right_nostril)

    # draw mouth
    def draw_mouth(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 300)

        width = cmd.get("width", 50)
        height = cmd.get("height", 20)

        smile = cmd.get("smile", True)
        teeth = cmd.get("teeth", False)

        # Mouth Outline
        if smile:
            mouth = {
                "points": [
                    [x - width // 2, y],
                    [x, y + height],
                    [x + width // 2, y]
                ]
            }
        else:
            mouth = {
                "points": [
                    [x - width // 2, y],
                    [x, y - height],
                    [x + width // 2, y]
                ]
            }

        self.commands.draw_bezier(mouth)

        # Teeth
        if teeth:

            self.commands.draw_line({
                "from": [x - width // 2 + 5, y],
                "to": [x + width // 2 - 5, y]
            })

            self.commands.draw_line({
                "from": [x, y - 2],
                "to": [x, y + 8]
            })

    # draw person
    def draw_person(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 200)

        head_radius = cmd.get("head_radius", 25)
        body_height = cmd.get("body_height", 80)
        arm_length = cmd.get("arm_length", 40)
        leg_length = cmd.get("leg_length", 50)

        # Head
        self.commands.draw_circle({
            "from": [
                x - head_radius,
                y - head_radius
            ],
            "to": [
                x + head_radius,
                y + head_radius
            ]
        })

        body_top = y + head_radius
        body_bottom = body_top + body_height

        # Body
        self.commands.draw_line({
            "from": [x, body_top],
            "to": [x, body_bottom]
        })

        # Left Arm
        self.commands.draw_line({
            "from": [x, body_top + 20],
            "to": [x - arm_length, body_top + 45]
        })

        # Right Arm
        self.commands.draw_line({
            "from": [x, body_top + 20],
            "to": [x + arm_length, body_top + 45]
        })

        # Left Leg
        self.commands.draw_line({
            "from": [x, body_bottom],
            "to": [x - 20, body_bottom + leg_length]
        })

        # Right Leg
        self.commands.draw_line({
            "from": [x, body_bottom],
            "to": [x + 20, body_bottom + leg_length]
        })

        # Left Eye
        self.commands.draw_circle({
            "from": [x - 10, y - 8],
            "to": [x - 4, y - 2]
        })

        # Right Eye
        self.commands.draw_circle({
            "from": [x + 4, y - 8],
            "to": [x + 10, y - 2]
        })

        # Mouth
        self.commands.draw_line({
            "from": [x - 8, y + 10],
            "to": [x + 8, y + 10]
        })

    # -------------------------------------------------
    # Animals
    # -------------------------------------------------

    # draw cat
    def draw_cat(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        head_radius = cmd.get("head_radius", 30)
        body_width = cmd.get("body_width", 60)
        body_height = cmd.get("body_height", 80)
        tail_length = cmd.get("tail_length", 50)

        # Head
        self.commands.draw_circle({
            "from": [x - head_radius, y - head_radius],
            "to": [x + head_radius, y + head_radius]
        })

        # Left Ear
        self.commands.draw_triangle({
            "points": [
                [x - 22, y - head_radius],
                [x - 8, y - head_radius - 28],
                [x + 2, y - head_radius]
            ]
        })

        # Right Ear
        self.commands.draw_triangle({
            "points": [
                [x - 2, y - head_radius],
                [x + 8, y - head_radius - 28],
                [x + 22, y - head_radius]
            ]
        })

        # Body
        self.commands.draw_ellipse({
            "from": [
                x - body_width // 2,
                y + head_radius - 5
            ],
            "to": [
                x + body_width // 2,
                y + head_radius + body_height
            ]
        })

        # Eyes
        self.commands.draw_circle({
            "from": [x - 14, y - 10],
            "to": [x - 8, y - 4]
        })

        self.commands.draw_circle({
            "from": [x + 8, y - 10],
            "to": [x + 14, y - 4]
        })

        # Nose
        self.commands.draw_triangle({
            "points": [
                [x - 3, y + 5],
                [x + 3, y + 5],
                [x, y + 10]
            ]
        })

        # Mouth
        self.commands.draw_line({
            "from": [x, y + 10],
            "to": [x, y + 18]
        })

        self.commands.draw_line({
            "from": [x, y + 18],
            "to": [x - 8, y + 22]
        })

        self.commands.draw_line({
            "from": [x, y + 18],
            "to": [x + 8, y + 22]
        })

        # Whiskers
        self.commands.draw_line({
            "from": [x - 6, y + 10],
            "to": [x - 28, y + 6]
        })

        self.commands.draw_line({
            "from": [x - 6, y + 14],
            "to": [x - 28, y + 16]
        })

        self.commands.draw_line({
            "from": [x + 6, y + 10],
            "to": [x + 28, y + 6]
        })

        self.commands.draw_line({
            "from": [x + 6, y + 14],
            "to": [x + 28, y + 16]
        })

        # Legs
        self.commands.draw_line({
            "from": [x - 18, y + head_radius + body_height],
            "to": [x - 18, y + head_radius + body_height + 30]
        })

        self.commands.draw_line({
            "from": [x + 18, y + head_radius + body_height],
            "to": [x + 18, y + head_radius + body_height + 30]
        })

        # Tail
        self.commands.draw_bezier({
            "points": [
                [x + body_width // 2, y + head_radius + 25],
                [x + body_width // 2 + 30, y + head_radius - 20],
                [x + body_width // 2 + tail_length, y + head_radius + 30]
            ]
        })

    # draw dog
    def draw_dog(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        head_radius = cmd.get("head_radius", 28)
        body_width = cmd.get("body_width", 70)
        body_height = cmd.get("body_height", 85)
        tail_length = cmd.get("tail_length", 45)

        # Head
        self.commands.draw_circle({
            "from": [x - head_radius, y - head_radius],
            "to": [x + head_radius, y + head_radius]
        })

        # Left Ear
        self.commands.draw_ellipse({
            "from": [x - head_radius - 12, y - head_radius + 5],
            "to": [x - head_radius + 8, y + 12]
        })

        # Right Ear
        self.commands.draw_ellipse({
            "from": [x + head_radius - 8, y - head_radius + 5],
            "to": [x + head_radius + 12, y + 12]
        })

        # Body
        self.commands.draw_ellipse({
            "from": [
                x - body_width // 2,
                y + head_radius - 5
            ],
            "to": [
                x + body_width // 2,
                y + head_radius + body_height
            ]
        })

        # Eyes
        self.commands.draw_circle({
            "from": [x - 12, y - 10],
            "to": [x - 6, y - 4]
        })

        self.commands.draw_circle({
            "from": [x + 6, y - 10],
            "to": [x + 12, y - 4]
        })

        # Nose
        self.commands.draw_circle({
            "from": [x - 4, y + 4],
            "to": [x + 4, y + 12]
        })

        # Mouth
        self.commands.draw_line({
            "from": [x, y + 12],
            "to": [x, y + 20]
        })

        self.commands.draw_line({
            "from": [x, y + 20],
            "to": [x - 8, y + 24]
        })

        self.commands.draw_line({
            "from": [x, y + 20],
            "to": [x + 8, y + 24]
        })

        # Collar
        self.commands.draw_line({
            "from": [x - 18, y + head_radius - 2],
            "to": [x + 18, y + head_radius - 2]
        })

        # Legs
        leg_top = y + head_radius + body_height

        self.commands.draw_line({
            "from": [x - 22, leg_top],
            "to": [x - 22, leg_top + 30]
        })

        self.commands.draw_line({
            "from": [x - 8, leg_top],
            "to": [x - 8, leg_top + 30]
        })

        self.commands.draw_line({
            "from": [x + 8, leg_top],
            "to": [x + 8, leg_top + 30]
        })

        self.commands.draw_line({
            "from": [x + 22, leg_top],
            "to": [x + 22, leg_top + 30]
        })

        # Tail
        self.commands.draw_bezier({
            "points": [
                [x + body_width // 2, y + head_radius + 20],
                [x + body_width // 2 + 20, y + head_radius - 10],
                [x + body_width // 2 + tail_length, y + head_radius + 15]
            ]
        })

    # draw bird
    def draw_bird(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 220)

        body_width = cmd.get("body_width", 70)
        body_height = cmd.get("body_height", 45)

        head_radius = cmd.get("head_radius", 18)
        wing_height = cmd.get("wing_height", 35)
        tail_length = cmd.get("tail_length", 30)

        # Body
        self.commands.draw_ellipse({
            "from": [
                x - body_width // 2,
                y - body_height // 2
            ],
            "to": [
                x + body_width // 2,
                y + body_height // 2
            ]
        })

        # Head
        self.commands.draw_circle({
            "from": [
                x - body_width // 2 - head_radius,
                y - head_radius
            ],
            "to": [
                x - body_width // 2 + head_radius,
                y + head_radius
            ]
        })

        # Beak
        self.commands.draw_triangle({
            "points": [
                [x - body_width // 2 - head_radius, y],
                [x - body_width // 2 - head_radius - 18, y - 6],
                [x - body_width // 2 - head_radius - 18, y + 6]
            ]
        })

        # Eye
        self.commands.draw_circle({
            "from": [
                x - body_width // 2 - 8,
                y - 6
            ],
            "to": [
                x - body_width // 2 - 2,
                y
            ]
        })

        # Wing
        self.commands.draw_ellipse({
            "from": [
                x - 10,
                y - wing_height // 2
            ],
            "to": [
                x + 25,
                y + wing_height // 2
            ]
        })

        # Tail
        self.commands.draw_triangle({
            "points": [
                [x + body_width // 2, y],
                [x + body_width // 2 + tail_length, y - 15],
                [x + body_width // 2 + tail_length, y + 15]
            ]
        })

        # Left Leg
        self.commands.draw_line({
            "from": [x - 10, y + body_height // 2],
            "to": [x - 15, y + body_height // 2 + 20]
        })

        # Right Leg
        self.commands.draw_line({
            "from": [x + 10, y + body_height // 2],
            "to": [x + 15, y + body_height // 2 + 20]
        })

        # Left Foot
        self.commands.draw_line({
            "from": [x - 15, y + body_height // 2 + 20],
            "to": [x - 20, y + body_height // 2 + 25]
        })

        self.commands.draw_line({
            "from": [x - 15, y + body_height // 2 + 20],
            "to": [x - 10, y + body_height // 2 + 25]
        })

        # Right Foot
        self.commands.draw_line({
            "from": [x + 15, y + body_height // 2 + 20],
            "to": [x + 10, y + body_height // 2 + 25]
        })

        self.commands.draw_line({
            "from": [x + 15, y + body_height // 2 + 20],
            "to": [x + 20, y + body_height // 2 + 25]
        })
        
    # draw fish
    def draw_fish(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        body_width = cmd.get("body_width", 90)
        body_height = cmd.get("body_height", 50)

        tail_width = cmd.get("tail_width", 35)
        fin_height = cmd.get("fin_height", 20)

        # Body
        self.commands.draw_ellipse({
            "from": [
                x - body_width // 2,
                y - body_height // 2
            ],
            "to": [
                x + body_width // 2,
                y + body_height // 2
            ]
        })

        # Tail
        self.commands.draw_triangle({
            "points": [
                [x + body_width // 2, y],
                [x + body_width // 2 + tail_width, y - body_height // 2],
                [x + body_width // 2 + tail_width, y + body_height // 2]
            ]
        })

        # Top Fin
        self.commands.draw_triangle({
            "points": [
                [x - 10, y - body_height // 2],
                [x + 10, y - body_height // 2 - fin_height],
                [x + 30, y - body_height // 2]
            ]
        })

        # Bottom Fin
        self.commands.draw_triangle({
            "points": [
                [x - 10, y + body_height // 2],
                [x + 10, y + body_height // 2 + fin_height],
                [x + 30, y + body_height // 2]
            ]
        })

        # Eye
        self.commands.draw_circle({
            "from": [
                x - body_width // 3 - 4,
                y - 4
            ],
            "to": [
                x - body_width // 3 + 4,
                y + 4
            ]
        })

        # Mouth
        self.commands.draw_line({
            "from": [
                x - body_width // 2,
                y
            ],
            "to": [
                x - body_width // 2 - 10,
                y + 4
            ]
        })

        # Gill
        self.commands.draw_line({
            "from": [
                x - body_width // 4,
                y - 15
            ],
            "to": [
                x - body_width // 4,
                y + 15
            ]
        })

        # Decorative Scales
        for i in range(3):
            self.commands.draw_circle({
                "from": [
                    x - 5 + i * 15,
                    y - 8
                ],
                "to": [
                    x + 3 + i * 15,
                    y
                ]
            })

            self.commands.draw_circle({
                "from": [
                    x - 5 + i * 15,
                    y + 4
                ],
                "to": [
                    x + 3 + i * 15,
                    y + 12
                ]
            })

    # -------------------------------------------------
    # Vehicles
    # -------------------------------------------------

    # draw car with body, roof, wheels, and windows
    def draw_car(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        width = cmd.get("width", 220)
        height = cmd.get("height", 70)

        wheel_radius = cmd.get("wheel_radius", 22)

        roof_height = cmd.get("roof_height", 50)

        # Car Body
        body = {
            "from": [x, y],
            "to": [x + width, y + height]
        }

        # Car Roof
        roof = {
            "points": [
                [x + 50, y],
                [x + 80, y - roof_height],
                [x + width - 80, y - roof_height],
                [x + width - 50, y]
            ]
        }

        # Left Wheel
        left_wheel = {
            "from": [
                x + 25,
                y + height - wheel_radius
            ],
            "to": [
                x + 25 + wheel_radius * 2,
                y + height + wheel_radius
            ]
        }

        # Right Wheel
        right_wheel = {
            "from": [
                x + width - 25 - wheel_radius * 2,
                y + height - wheel_radius
            ],
            "to": [
                x + width - 25,
                y + height + wheel_radius
            ]
        }

        # Window
        window = {
            "from": [
                x + 75,
                y - roof_height + 10
            ],
            "to": [
                x + width - 75,
                y - 10
            ]
        }

        self.commands.draw_rectangle(body)
        self.commands.draw_polygon(roof)
        self.commands.draw_rectangle(window)
        self.commands.draw_circle(left_wheel)
        self.commands.draw_circle(right_wheel)

    # draw bike with body, wheels, and handlebars
    def draw_bike(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 300)

        wheel_radius = cmd.get("wheel_radius", 35)
        frame_length = cmd.get("frame_length", 120)
        seat_height = cmd.get("seat_height", 40)
        handle_height = cmd.get("handle_height", 45)

        # Wheels
        left_wheel = {
            "from": [x - wheel_radius, y - wheel_radius],
            "to": [x + wheel_radius, y + wheel_radius]
        }

        right_wheel = {
            "from": [x + frame_length - wheel_radius, y - wheel_radius],
            "to": [x + frame_length + wheel_radius, y + wheel_radius]
        }

        self.commands.draw_circle(left_wheel)
        self.commands.draw_circle(right_wheel)

        # Frame
        self.commands.draw_line({
            "from": [x, y],
            "to": [x + frame_length // 2, y - seat_height]
        })

        self.commands.draw_line({
            "from": [x + frame_length // 2, y - seat_height],
            "to": [x + frame_length, y]
        })

        self.commands.draw_line({
            "from": [x, y],
            "to": [x + frame_length, y]
        })

        self.commands.draw_line({
            "from": [x + frame_length // 2, y - seat_height],
            "to": [x + frame_length // 2 - 15, y]
        })

        # Seat
        self.commands.draw_line({
            "from": [x + frame_length // 2 - 15, y - seat_height],
            "to": [x + frame_length // 2 + 15, y - seat_height]
        })

        # Seat Post
        self.commands.draw_line({
            "from": [x + frame_length // 2, y - seat_height],
            "to": [x + frame_length // 2 - 15, y]
        })

        # Handle Bar
        self.commands.draw_line({
            "from": [x + frame_length, y],
            "to": [x + frame_length, y - handle_height]
        })

        self.commands.draw_line({
            "from": [x + frame_length - 15, y - handle_height],
            "to": [x + frame_length + 15, y - handle_height]
        })

        # Front Fork
        self.commands.draw_line({
            "from": [x + frame_length, y - handle_height],
            "to": [x + frame_length, y]
        })

        # Pedal Crank
        self.commands.draw_circle({
            "from": [
                x + frame_length // 2 - 8,
                y - 8
            ],
            "to": [
                x + frame_length // 2 + 8,
                y + 8
            ]
        })

        # Pedals
        self.commands.draw_line({
            "from": [x + frame_length // 2, y],
            "to": [x + frame_length // 2 - 15, y + 15]
        })

        self.commands.draw_line({
            "from": [x + frame_length // 2, y],
            "to": [x + frame_length // 2 + 15, y - 15]
        })

    # draw boat with hull, sail, and mast
    def draw_boat(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 300)

        width = cmd.get("width", 220)
        hull_height = cmd.get("hull_height", 45)
        mast_height = cmd.get("mast_height", 140)
        sail_width = cmd.get("sail_width", 90)

        # Hull
        hull = {
            "points": [
                [x, y],
                [x + width, y],
                [x + width - 35, y + hull_height],
                [x + 35, y + hull_height]
            ]
        }

        # Mast
        mast = {
            "from": [x + width // 2, y],
            "to": [x + width // 2, y - mast_height]
        }

        # Main Sail
        main_sail = {
            "points": [
                [x + width // 2, y - mast_height],
                [x + width // 2, y],
                [x + width // 2 + sail_width, y - mast_height // 2]
            ]
        }

        # Front Sail
        front_sail = {
            "points": [
                [x + width // 2, y - mast_height + 20],
                [x + width // 2, y],
                [x + width // 2 - sail_width + 20, y - mast_height // 2]
            ]
        }

        # Flag Pole
        flag_pole = {
            "from": [x + width // 2, y - mast_height],
            "to": [x + width // 2, y - mast_height - 20]
        }

        # Flag
        flag = {
            "points": [
                [x + width // 2, y - mast_height - 20],
                [x + width // 2 + 25, y - mast_height - 12],
                [x + width // 2, y - mast_height - 4]
            ]
        }

        self.commands.draw_polygon(hull)
        self.commands.draw_line(mast)
        self.commands.draw_triangle(main_sail)
        self.commands.draw_triangle(front_sail)
        self.commands.draw_line(flag_pole)
        self.commands.draw_triangle(flag)


    # draw airplane with fuselage, wings, and tail
    def draw_airplane(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        body_length = cmd.get("body_length", 220)
        body_height = cmd.get("body_height", 35)

        wing_span = cmd.get("wing_span", 80)
        tail_height = cmd.get("tail_height", 45)
        nose_length = cmd.get("nose_length", 30)

        # Fuselage
        body = {
            "from": [x, y],
            "to": [x + body_length, y + body_height]
        }

        # Nose
        nose = {
            "points": [
                [x + body_length, y],
                [x + body_length + nose_length, y + body_height // 2],
                [x + body_length, y + body_height]
            ]
        }

        # Main Wing
        main_wing = {
            "points": [
                [x + body_length // 2 - 20, y + body_height // 2],
                [x + body_length // 2 + 30, y - wing_span],
                [x + body_length // 2 + 80, y + body_height // 2]
            ]
        }

        # Rear Wing
        rear_wing = {
            "points": [
                [x + body_length // 2 - 20, y + body_height // 2],
                [x + body_length // 2 + 30, y + body_height + wing_span],
                [x + body_length // 2 + 80, y + body_height // 2]
            ]
        }

        # Tail Fin
        tail_fin = {
            "points": [
                [x + 20, y],
                [x + 20, y - tail_height],
                [x + 60, y]
            ]
        }

        # Tail Wing
        tail_wing = {
            "points": [
                [x + 20, y + body_height // 2],
                [x - 20, y + body_height // 2 + 20],
                [x + 60, y + body_height // 2]
            ]
        }

        # Cockpit Window
        cockpit = {
            "from": [
                x + body_length - 50,
                y + 6
            ],
            "to": [
                x + body_length - 20,
                y + 22
            ]
        }

        self.commands.draw_rectangle(body)
        self.commands.draw_triangle(nose)
        self.commands.draw_triangle(main_wing)
        self.commands.draw_triangle(rear_wing)
        self.commands.draw_triangle(tail_fin)
        self.commands.draw_triangle(tail_wing)
        self.commands.draw_rectangle(cockpit)

    # -------------------------------------------------
    # Game Assets
    # -------------------------------------------------

    # draw coin with outer circle, inner circle, and vertical and horizontal lines
    def draw_coin(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 300)

        radius = cmd.get("radius", 40)
        inner_radius = cmd.get("inner_radius", 30)

        # Outer Coin
        outer = {
            "from": [
                x - radius,
                y - radius
            ],
            "to": [
                x + radius,
                y + radius
            ]
        }

        # Inner Ring
        inner = {
            "from": [
                x - inner_radius,
                y - inner_radius
            ],
            "to": [
                x + inner_radius,
                y + inner_radius
            ]
        }

        # Vertical Line
        vertical = {
            "from": [x, y - inner_radius + 5],
            "to": [x, y + inner_radius - 5]
        }

        # Horizontal Line
        horizontal = {
            "from": [x - inner_radius + 5, y],
            "to": [x + inner_radius - 5, y]
        }

        self.commands.draw_circle(outer)
        self.commands.draw_circle(inner)
        self.commands.draw_line(vertical)
        self.commands.draw_line(horizontal)

    # draw heart with two circles and a triangle
    def draw_heart(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        size = cmd.get("size", 60)

        # Left Heart Circle
        left = {
            "from": [
                x - size,
                y - size
            ],
            "to": [
                x,
                y
            ]
        }

        # Right Heart Circle
        right = {
            "from": [
                x,
                y - size
            ],
            "to": [
                x + size,
                y
            ]
        }

        # Bottom Heart
        bottom = {
            "points": [
                [x - size, y - size // 2],
                [x + size, y - size // 2],
                [x, y + size + 20]
            ]
        }

        self.commands.draw_circle(left)
        self.commands.draw_circle(right)
        self.commands.draw_triangle(bottom)
    

    # draw star with five points
    def draw_star(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        size = cmd.get("size", 60)

        points = {
            "points": [
                [x, y - size],
                [x + size // 4, y - size // 4],
                [x + size, y - size // 4],
                [x + size // 2, y + size // 6],
                [x + (3 * size) // 4, y + size],
                [x, y + size // 2],
                [x - (3 * size) // 4, y + size],
                [x - size // 2, y + size // 6],
                [x - size, y - size // 4],
                [x - size // 4, y - size // 4]
            ]
        }

        self.commands.draw_polygon(points)

    # draw sword with blade and handle
    def draw_sword(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 120)

        blade_length = cmd.get("blade_length", 180)
        blade_width = cmd.get("blade_width", 20)

        guard_width = cmd.get("guard_width", 80)
        guard_height = cmd.get("guard_height", 12)

        handle_length = cmd.get("handle_length", 60)
        handle_width = cmd.get("handle_width", 14)

        pommel_radius = cmd.get("pommel_radius", 10)

        # Blade
        blade = {
            "from": [
                x - blade_width // 2,
                y
            ],
            "to": [
                x + blade_width // 2,
                y + blade_length
            ]
        }

        # Blade Tip
        tip = {
            "points": [
                [x - blade_width // 2, y],
                [x + blade_width // 2, y],
                [x, y - 30]
            ]
        }

        # Cross Guard
        guard = {
            "from": [
                x - guard_width // 2,
                y + blade_length
            ],
            "to": [
                x + guard_width // 2,
                y + blade_length + guard_height
            ]
        }

        # Handle
        handle = {
            "from": [
                x - handle_width // 2,
                y + blade_length + guard_height
            ],
            "to": [
                x + handle_width // 2,
                y + blade_length + guard_height + handle_length
            ]
        }

        # Pommel
        pommel = {
            "from": [
                x - pommel_radius,
                y + blade_length + guard_height + handle_length
            ],
            "to": [
                x + pommel_radius,
                y + blade_length + guard_height + handle_length + pommel_radius * 2
            ]
        }

        self.commands.draw_rectangle(blade)
        self.commands.draw_triangle(tip)
        self.commands.draw_rectangle(guard)
        self.commands.draw_rectangle(handle)
        self.commands.draw_circle(pommel)


    # draw shield with border and center
    def draw_shield(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 150)

        width = cmd.get("width", 120)
        height = cmd.get("height", 180)

        emblem_size = cmd.get("emblem_size", 20)

        # Shield Outline
        shield = {
            "points": [
                [x, y],
                [x + width, y],
                [x + width, y + height // 2],
                [x + width // 2, y + height],
                [x, y + height // 2]
            ]
        }

        # Center Emblem
        emblem = {
            "from": [
                x + width // 2 - emblem_size,
                y + height // 3 - emblem_size
            ],
            "to": [
                x + width // 2 + emblem_size,
                y + height // 3 + emblem_size
            ]
        }

        # Vertical Line
        vertical = {
            "from": [
                x + width // 2,
                y + height // 3 - emblem_size
            ],
            "to": [
                x + width // 2,
                y + height // 3 + emblem_size
            ]
        }

        # Horizontal Line
        horizontal = {
            "from": [
                x + width // 2 - emblem_size,
                y + height // 3
            ],
            "to": [
                x + width // 2 + emblem_size,
                y + height // 3
            ]
        }

        self.commands.draw_polygon(shield)
        self.commands.draw_circle(emblem)
        self.commands.draw_line(vertical)
        self.commands.draw_line(horizontal)

    # draw chest with lid and lock
    def draw_chest(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        width = cmd.get("width", 140)
        height = cmd.get("height", 100)

        lid_height = cmd.get("lid_height", 40)
        lock_size = cmd.get("lock_size", 18)

        # Chest Base
        base = {
            "from": [
                x,
                y
            ],
            "to": [
                x + width,
                y + height
            ]
        }

        # Chest Lid
        lid = {
            "points": [
                [x, y],
                [x + width, y],
                [x + width - 15, y - lid_height],
                [x + 15, y - lid_height]
            ]
        }

        # Lock
        lock = {
            "from": [
                x + width // 2 - lock_size // 2,
                y + height // 3
            ],
            "to": [
                x + width // 2 + lock_size // 2,
                y + height // 3 + lock_size
            ]
        }

        # Left Metal Band
        left_band = {
            "from": [
                x + 25,
                y
            ],
            "to": [
                x + 35,
                y + height
            ]
        }

        # Right Metal Band
        right_band = {
            "from": [
                x + width - 35,
                y
            ],
            "to": [
                x + width - 25,
                y + height
            ]
        }

        self.commands.draw_polygon(lid)
        self.commands.draw_rectangle(base)
        self.commands.draw_rectangle(left_band)
        self.commands.draw_rectangle(right_band)
        self.commands.draw_rectangle(lock)
    

    # draw hut with roof, door, and windows
    def draw_hut(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 220)

        width = cmd.get("width", 180)
        height = cmd.get("height", 120)

        roof_height = cmd.get("roof_height", 70)

        door_width = cmd.get("door_width", 40)
        door_height = cmd.get("door_height", 70)

        window_size = cmd.get("window_size", 30)

        # Hut Body
        body = {
            "from": [x, y],
            "to": [x + width, y + height]
        }

        # Roof
        roof = {
            "points": [
                [x + width // 2, y - roof_height],
                [x + width + 20, y],
                [x - 20, y]
            ]
        }

        # Door
        door = {
            "from": [
                x + width // 2 - door_width // 2,
                y + height - door_height
            ],
            "to": [
                x + width // 2 + door_width // 2,
                y + height
            ]
        }

        # Left Window
        left_window = {
            "from": [
                x + 25,
                y + 30
            ],
            "to": [
                x + 25 + window_size,
                y + 30 + window_size
            ]
        }

        # Right Window
        right_window = {
            "from": [
                x + width - 25 - window_size,
                y + 30
            ],
            "to": [
                x + width - 25,
                y + 30 + window_size
            ]
        }

        self.commands.draw_rectangle(body)
        self.commands.draw_triangle(roof)
        self.commands.draw_rectangle(door)
        self.commands.draw_rectangle(left_window)
        self.commands.draw_rectangle(right_window)
    
    # draw face with eyes, nose, mouth, ears
    def draw_face(self, cmd):

        x = cmd.get("x", 300)
        y = cmd.get("y", 250)

        radius = cmd.get("radius", 60)

        eye_radius = cmd.get("eye_radius", 6)

        # Face
        face = {
            "from": [
                x - radius,
                y - radius
            ],
            "to": [
                x + radius,
                y + radius
            ]
        }

        self.commands.draw_circle(face)

        # Left Eye
        left_eye = {
            "from": [
                x - 25 - eye_radius,
                y - 15 - eye_radius
            ],
            "to": [
                x - 25 + eye_radius,
                y - 15 + eye_radius
            ]
        }

        # Right Eye
        right_eye = {
            "from": [
                x + 25 - eye_radius,
                y - 15 - eye_radius
            ],
            "to": [
                x + 25 + eye_radius,
                y - 15 + eye_radius
            ]
        }

        self.commands.draw_circle(left_eye)
        self.commands.draw_circle(right_eye)

        # Nose
        self.commands.draw_line({
            "from": [x, y - 5],
            "to": [x, y + 20]
        })

        # Mouth
        self.commands.draw_line({
            "from": [x - 20, y + 35],
            "to": [x + 20, y + 35]
        })

        # Left Ear
        self.commands.draw_circle({
            "from": [
                x - radius - 8,
                y - 10
            ],
            "to": [
                x - radius + 8,
                y + 10
            ]
        })

        # Right Ear
        self.commands.draw_circle({
            "from": [
                x + radius - 8,
                y - 10
            ],
            "to": [
                x + radius + 8,
                y + 10
            ]
        })
    

    # 