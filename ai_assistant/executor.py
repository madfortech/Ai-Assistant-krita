from .commands import Commands

class Executor:

    def __init__(self):
        self.commands = Commands()

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

            except Exception as e:
                print(f"Executor Error ({action}): {e}")
                print(f"Executor Error ({action}): {e}")