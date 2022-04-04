# MACROPAD Hotkeys example: Adobe Illustrator for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Teams', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'Mute',  [Keycode.COMMAND, Keycode.SHIFT, 'M']),
        (0x404000, 'Video', [Keycode.COMMAND, Keycode.SHIFT, 'O']),
        (0x400000, 'Leave', [Keycode.COMMAND, Keycode.SHIFT, 'H']),
        # 2nd row ----------
        (0x101010, '', 'v'),  # Select (path)
        (0x101010, '', 'o'), # Reflect selection
        (0x101010, '', 'm'),    # Draw rectangle
        # 3rd row ----------
        (0x101010, '', 'a'),  # Direct (point) selection
        (0x101010, '', 'r'),  # Rotate selection
        (0x101010, '', 'l'),    # Draw ellipse
        # 4th row ----------
        (0x000040, '', [Keycode.COMMAND, Keycode.SHIFT, 'M']),
        (0x000040, 'Toggle Mute', [Keycode.COMMAND, Keycode.SHIFT, 'M']),
        (0x000040, '', [Keycode.COMMAND, Keycode.SHIFT, 'M']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, Keycode.OPTION, 'S']) # Save for web
    ]
}
