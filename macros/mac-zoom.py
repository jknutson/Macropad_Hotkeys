# MACROPAD Hotkeys example: Adobe Illustrator for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'Mute',  [Keycode.COMMAND, Keycode.SHIFT, 'A']),
        (0x000040, 'Video', [Keycode.COMMAND, Keycode.SHIFT, 'V']),
        (0x004000, 'Leave', [Keycode.Command, 'W'),
        # 2nd row ----------
        (0x101010, 'Select', 'v'),  # Select (path)
        (0x101010, 'Reflect', 'o'), # Reflect selection
        (0x101010, 'Rect', 'm'),    # Draw rectangle
        # 3rd row ----------
        (0x101010, 'Direct', 'a'),  # Direct (point) selection
        (0x101010, 'Rotate', 'r'),  # Rotate selection
        (0x101010, 'Oval', 'l'),    # Draw ellipse
        # 4th row ----------
        (0x000040, '', Keycode.SPACEBAR),
        (0x000040, 'Toggle Mute', Keycode.SPACEBAR),
        (0x000040, '', Keycode.SPACEBAR),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, Keycode.OPTION, 'S']) # Save for web
    ]
}
