# MACROPAD Hotkeys example: Adobe Illustrator for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Mac Fusion Modeling', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'Undo', [Keycode.COMMAND, 'z']),   #Undo
        (0x101010, 'Redo', [Keycode.COMMAND, 'Z']),   #Redo
        (0x101010, 'Shortcut', 's'),     # shortcuts pallet
        # 2nd row ----------

        (0x004000, 'Window', '1'),  # Select by window
        (0x004000, 'Freefrom', '2'), # Select by Lasso
        (0x004000, 'Paint', '3'),    # Select by paint
        # 3rd row ----------
        (0x101010, '<Space', [Keycode.COMMAND, '[']),  # Direct (point) selection
        (0x000040, 'Data', [Keycode.COMMAND, Keycode.OPTION, 'p']),  # Rotate selection
        (0x101010, 'Space>', [Keycode.COMMAND, ']']),    # Draw ellipse
        # 4th row ----------
        (0x303000, 'Shaded', [Keycode.CONTROL, '4']), # Cycle eyedropper/measure modes
        (0x303000, 'Edges', [Keycode.CONTROL, '6']),   # Scale selection
        (0x303000, 'Wire', [Keycode.CONTROL, '8']),    # Type tool
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 's']) # Save
    ]
}
