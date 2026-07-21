# AI Assistant for Krita

AI Assistant for Krita is an open-source plugin that allows you to create drawings in Krita using natural language. The plugin sends your prompt to an AI backend, receives drawing commands, and executes them directly on the Krita canvas.

> **Disclaimer:** This is an independent community project and is **not affiliated with, endorsed by, or an official plugin of the Krita Foundation.**

## Features

- AI-powered drawing generation
- Natural language prompts
- Automatic layer creation
- Brush selection
- Brush size control
- Color selection
- Draw lines
- Draw rectangles
- Draw circles
- Draw ellipses
- Draw Bezier curves
- Draw polygons
- JSON command execution
- Secure Unique Key authentication

## Supported Commands

- create_layer
- set_brush
- set_size
- set_color
- draw_line
- draw_rectangle
- draw_circle
- draw_ellipse
- draw_bezier
- draw_polygon

## Requirements

- Krita 5.x
- Internet connection

## Installation

1. Download or clone this repository.
2. Copy the `ai_assistant` folder into:

```text
%APPDATA%\krita\pykrita\
```

3. Restart Krita.
4. Enable the plugin from **Settings → Configure Krita → Python Plugin Manager**.
5. Open **Settings → Dockers → AI Assistant**.

> **Documentation:** Coming Soon  
> **Website:** Coming Soon

## Usage

1. Open or create a Krita document.
2. Open the **AI Assistant** docker.
3. Once available, obtain your **Server URL** and **Unique Key** from the AI Assistant website.
4. Enter them into the AI Assistant settings.
5. Enter a drawing prompt.
6. Click **Generate**.
7. The drawing will be created automatically on the active layer.

### Example Prompts

- Draw a house
- Create a car
- Draw a tree
- Draw a smiling face
- Draw a flower
- Draw a mountain
- Draw a bridge
- Draw a simple robot

## API Example

### Request

```json
{
  "prompt": "Create a car"
}
```

### Response

```json
{
  "commands": [
    {
      "action": "create_layer",
      "name": "Car"
    }
  ]
}
```

## Error Handling

The plugin provides user-friendly messages for:

- Network errors
- Authentication failures
- Invalid AI responses
- Missing Krita document
- Drawing execution failures

## License

GPL-3.0 License

## Author

**MadForTech**

GitHub: <https://github.com/madfortech/Ai-Assistant-krita>