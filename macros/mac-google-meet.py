from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

PRESSED = 0xFFFFFF
WHITE = 0x404040
RED = 0x400000
GREEN = 0x004000
BLUE = 0x000040
YELLOW = 0x404000
MAGENTA = 0x400040
CYAN = 0x004040

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Meet', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (GREEN, 'Mute',  [Keycode.COMMAND, 'd']),
        (YELLOW, 'Video', [Keycode.COMMAND, 'e']),
        (RED, 'Close', [Keycode.COMMAND, 'w']),
        # 2nd row ----------
        (WHITE, '', 'v'),
        (WHITE, '', 'o'),
        (WHITE, '', 'm'),
        # 3rd row ----------
        (BLUE, 'Who', [Keycode.CONTROL, Keycode.COMMAND, 'p']),
        (WHITE, '', 'c'),
        (BLUE, 'Chat', [Keycode.CONTROL, Keycode.COMMAND, 'c']),
        # 4th row ----------
        (GREEN, '', [Keycode.COMMAND, 'd']),
        (GREEN, 'Mute', [Keycode.COMMAND, 'd']),
        (GREEN, '', [Keycode.COMMAND, 'd']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, Keycode.OPTION, 'S']) # Save for web
    ]
}
