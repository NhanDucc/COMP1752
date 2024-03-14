import tkinter.font as tkfont   # Import the font module from the Tkinter library

current_font = None # Create a variable to store the current font

def configure():                                        # Function to configure the fonts
    global current_font                                 # Use the global variable
    # family = "Segoe UI"
    family = "Helvetica"                                # Set the font famil    
    default_font = tkfont.nametofont("TkDefaultFont")   # Get the default font
    default_font.configure(size=15, family=family)      # Configure the default font
    text_font = tkfont.nametofont("TkTextFont")         # Get the text font
    text_font.configure(size=12, family=family)         # Configure the text font
    fixed_font = tkfont.nametofont("TkFixedFont")       # Get the fixed font
    fixed_font.configure(size=12, family=family)        # Configure the fixed font
    current_font = family                               # Store the current font family
