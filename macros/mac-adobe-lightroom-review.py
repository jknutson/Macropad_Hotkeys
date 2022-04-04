# MACROPAD Hotkeys example: Adobe Photoshop for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

PRESSED = 0xFFFFFF
WHITE = 0x404040
RED = 0x400000
GREEN = 0x004000
BLUE = 0x000040

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Lightroom Review', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (BLUE, 'Grid', 'g'),
        (BLUE, 'Detail', 'd'),
        (GREEN, 'Full', 'f'),
        # 2nd row ----------
        (BLUE, '<', [Keycode.COMMAND, '[']),
        (WHITE,   'Rotate', [Keycode.SPACEBAR]),
        (BLUE, '>', [Keycode.COMMAND, ']']),
        # 3rd row ----------
        (GREEN, 'Pick', 'z'),
        (BLUE, 'Unpick', 'u'),
        (RED, 'Reject', 'x'),
        # 4th row ----------
        (BLUE,  '<-', [Keycode.LEFT_ARROW]),
        (WHITE, '+',  [Keycode.SPACEBAR]),
        (BLUE,  '->', [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.SHIFT, Keycode.COMMAND, 'I']) # Import Photos
    ]
}
