from library_item import LibraryItem    # Import the LibraryItem class from the library_item module

library = {}    # Create an empty dictionary to store the library items
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, "VideoPlayer COMP1752\Image\Tom and Jerry.jpg")  # Add a new library item to the dictionary
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, "VideoPlayer COMP1752\Image\Breakfast at Tiffany's.jpg")  # Add a new library item to the dictionary
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, "VideoPlayer COMP1752\Image\Casablanca.jpg") # Add a new library item to the dictionary
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, "VideoPlayer COMP1752\Image\The Sound of Music.jpg")    # Add a new library item to the dictionary
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, "VideoPlayer COMP1752\Image\Gone with the Wind.jpg")   # Add a new library item to the dictionary

def list_all(): # Function to list all library items
    output = "" # Create an empty string
    for key in library: # Iterate through the library items
        item = library[key] # Get the library item
        output += f"{key} {item.info()}\n"  # Add the library item details to the output string
    return output   # Return the output string

def get_name(key):  # Function to get the name of a library item
    try:    # Try to get the name of the library item
        item = library[key] # Get the library item
        return item.name    # Return the name of the library item
    except KeyError:    # If the key does not exist
        return None # Return None

def get_director(key):  # Function to get the director of a library item
    try:    # Try to get the director of the library item
        item = library[key] # Get the library item
        return item.director    # Return the director of the library item
    except KeyError:    # If the key does not exist
        return None # Return None

def get_rating(key):    # Function to get the rating of a library item
    try:    # Try to get the rating of the library item
        item = library[key] # Get the library item
        return item.rating  # Return the rating of the library item
    except KeyError:    # If the key does not exist
        return -1   # Return -1

def set_rating(key, rating):    # Function to set the rating of a library item
    try:    # Try to set the rating of the library item
        item = library[key] # Get the library item
        item.rating = rating    # Set the rating of the library item
    except KeyError:    # If the key does not exist
        return  # Return

def get_play_count(key):    # Function to get the play count of a library item
    try:    # Try to get the play count of the library item
        item = library[key] # Get the library item
        return item.play_count  # Return the play count of the library item
    except KeyError:    # If the key does not exist
        return -1   # Return -1

def reset_play_count(key):  # Function to reset the play count of a library item
    try:    # Try to reset the play count of the library item
        item = library[key] # Get the library item
        item.play_count = 0 # Reset the play count of the library item
    except KeyError:    # If the key does not exist
        return  # Return

def increment_play_count(key):  # Function to increment the play count of a library item
    try:    # Try to increment the play count of the library item
        item = library[key] # Get the library item
        item.play_count += 1    # Increment the play count of the library item
    except KeyError:    # If the key does not exist
        return  # Return

def get_image_path(key):    # Function to get the image path of a library item
    try:    # Try to get the image path of the library item
        item = library[key] # Get the library item
        return item.image_path  # Return the image path of the library item
    except KeyError:    # If the key does not exist
        return  # Return
    
def get_key(name):  # Function to get the key of a library item
    for key, item in library.items():   # Iterate through the library items
        if item.name == name:   # If the name of the library item matches the given name
            return key  # Return the key of the library item
    return None # Return None