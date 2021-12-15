from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

PRESSED = 0xFFFFFF
WHITE = 0x606060
RED = 0x600000
GREEN = 0x006000
BLUE = 0x000060
YELLOW = 0x606000
MAGENTA = 0x600060
CYAN = 0x006060

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'WWW', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (GREEN, '< Back', [Keycode.COMMAND, '[']),
        (GREEN, 'Fwd >', [Keycode.COMMAND, ']']),
        (RED, 'Digi', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new tab
        # 2nd row ----------
        (YELLOW, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (YELLOW, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (BLUE, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 3rd row ----------
        (MAGENTA, 'Reload', [Keycode.COMMAND, 'r']),
        (MAGENTA, 'Hide', [Keycode.COMMAND, 'H']),
        (BLUE, 'Down', ' '),                     # Scroll down
        # 4th row ----------
        (GREEN, '< Back', [Keycode.COMMAND, '[']),
        (BLUE, '+Tab', [Keycode.COMMAND, 't']),
        (GREEN, 'Fwd >', [Keycode.COMMAND, ']']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
