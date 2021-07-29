# MACROPAD Hotkeys example: Adobe Photoshop for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

PRESSED = 0xFFFFFF
WHITE = 0x404040
RED = 0x400000
GREEN = 0x004000
BLUE = 0x000040

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Lightroom CC', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (BLUE, 'Undo', [Keycode.COMMAND, 'Z']),
        (BLUE, 'Redo', [Keycode.SHIFT, Keycode.COMMAND, 'Z']),
        (GREEN, 'OG', '/'),
        # 2nd row ----------
        (BLUE,  'Esc', [Keycode.ESCAPE]),
        (RED,   'Del', [Keycode.DELETE]),
        (GREEN, 'Ent', [Keycode.ENTER]),
        # 3rd row ----------
        (WHITE, 'Pics', 'P'),
        (WHITE, 'Edit', 'E'),
        (WHITE, 'Crop', 'C'),
        # 4th row ----------
        (BLUE,  '<-', [Keycode.LEFT_ARROW]),
        (WHITE, '+',  [Keycode.SPACEBAR]),
        (BLUE,  '->', [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.SHIFT, Keycode.COMMAND, 'I']) # Import Photos
    ]
}
