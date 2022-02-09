# MACROPAD Hotkeys example: AAutodesk Fusion 360 for Mac OS

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Mac Fusion Modeling', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'Undo',      [Keycode.COMMAND, 'z']),   #Undo
        (0x101010, 'Redo',      [Keycode.COMMAND, 'Z']),   #Redo
        (0x101010, 'Shortcut', 's'),   # shortcuts pallet
        # 2nd row ----------

        (0x004000, 'Window',    '1'),   # Select by window
        (0x004000, 'Lasso',     '2'),   # Select by Lasso
        (0x004000, 'Paint',     '3'),   # Select by paint
        # 3rd row ----------
        (0x101010, '< WS',      [Keycode.COMMAND, '[']),                    # Previous Workspace
        (0x000040, 'Data',      [Keycode.COMMAND, Keycode.OPTION, 'p']),    # Data Pane
        (0x101010, 'WS >',      [Keycode.COMMAND, ']']),                    # Next Workspace
        # 4th row ----------
        (0x303000, 'Shaded',    [Keycode.CONTROL, '4']),   # Shaded no edges visual style
        (0x303000, 'Edges',     [Keycode.CONTROL, '6']),   # Shaded with edges
        (0x303000, 'Wire',      [Keycode.CONTROL, '8']),   # Wireframe with hidden edges
        # Encoder button ---
        (0x000000, '',          [Keycode.COMMAND, 's'])   # Save
    ]
}
