from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'MIDI', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, '',  [Keycode.COMMAND, Keycode.SHIFT, 'A']),
        (0x404000, '', [Keycode.COMMAND, Keycode.SHIFT, 'V']),
        (0x400000, '', [Keycode.COMMAND, 'W']),
        # 2nd row ----------
        (0x101010, '', 'v'),  # Select (path)
        (0x101010, '', 'o'), # Reflect selection
        (0x101010, '', 'm'),    # Draw rectangle
        # 3rd row ----------
        (0x101010, '', 'a'),  # Direct (point) selection
        (0x101010, '', 'r'),  # Rotate selection
        (0x101010, '', 'l'),    # Draw ellipse
        # 4th row ----------
        (0x000040, '1', [1]),
        (0x000040, '2', [2]),
        (0x000040, '3', [3]),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, Keycode.OPTION, 'S']) # Save for web
    ]
}
