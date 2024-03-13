import tkinter.font as tkfont   # Import the font module from the Tkinter library


def configure():    # Function to configure the fonts
    # family = "Segoe UI"
    family = "Helvetica"    # Set the font family
    default_font = tkfont.nametofont("TkDefaultFont")   # Get the default font
    default_font.configure(size=15, family=family)  # Configure the default font
    text_font = tkfont.nametofont("TkTextFont")  # Get the text font
    text_font.configure(size=12, family=family)  # Configure the text font
    fixed_font = tkfont.nametofont("TkFixedFont")   # Get the fixed font
    fixed_font.configure(size=12, family=family)    # Configure the fixed font
