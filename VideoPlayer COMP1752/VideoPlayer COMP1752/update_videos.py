import tkinter as tk    # Import the Tkinter module for creating GUI applications
import video_library as lib   # Import the video_library module
import font_manager as fonts    # Import the font_manager module for managing fonts
from tkinter import ttk # Import the ttk module for themed widgets

def set_text(text_area, content):   # Function to set the text of a text area
    text_area.delete("1.0", tk.END) # Delete the current text in the text area
    text_area.insert(1.0, content)  # Insert the new text into the text area

class UpdateVideos():   # Create the UpdateVideos class
    def __init__(self, window): # Constructor method
        self.window = window    # Store the window in an instance variable
        # window.geometry("550x270")    # Set the window size
        window.title("Update Videos")   # Set the window title
        
        enter_number_lbl = tk.Label(window, text="Choose Video Name")   # Create a label widget
        enter_number_lbl.grid(row=0, column=0, padx=10, pady=10)    # Place the label widget in the window
        
        selected_option = tk.StringVar()    # Create a StringVar object to store the selected option
        names = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=names)  # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=1, padx=10, pady=10)  # Place the Combobox widget in the window

        search_video_btn = tk.Button(window, text="Search", command=self.search_video_clicked)  # Create "Search" button and assign the search_video_clicked function to it
        search_video_btn.grid(row=0, column=2, padx=10, pady=10)    # Place Search button widget in the window
        
        self.video_txt = tk.Text(window, width=25, height=5)    # Create a text widget
        self.video_txt.grid(row=1, column=2, padx=10, pady=10)  # Place the text widget in the window
        
        new_rating_lbl = tk.Label(window, text="Chosse New Rating")   # Create a label widget
        new_rating_lbl.grid(row=1, column=0, padx=10, pady=10)  # Place the label widget in the window
        
        self.new_rating_combo_box = ttk.Combobox(window, values=[1, 2, 3, 4, 5])    # Create a Combobox widget with the list of ratings
        self.new_rating_combo_box.grid(row=1, column=1, padx=10, pady=10)   # Place the Combobox widget in the window
        
        update_btn = tk.Button(window, text="Update", command=self.update_video_clicked)    # Create "Update" button and assign the update_video_clicked function to it
        update_btn.grid(row=2, column=0, padx=10, pady=10)  # Place Update button widget in the window
        
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked) # Create "Reset" button and assign the reset_clicked function to it
        reset_btn.grid(row=2, column=1, padx=10, pady=10)   # Place Reset button widget in the window
        
        back_btn = tk.Button(window, text="Back", command=self.back_clicked)    # Create "Back" button and assign the back_clicked function to it
        back_btn.grid(row=2, column=2, padx=10, pady=10)    # Place Back button widget in the window
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window

    def search_video_clicked(self): # Method to handle the "Search" button click event
        name = self.name_combo_box.get()    # Get the selected video name
        key = lib.get_key(name) # Get the key of the selected video
        
        if name != "":  # If a video is selected
            director = lib.get_director(key)    # Get the director of the selected video
            rating = lib.get_rating(key)    # Get the rating of the selected video
            self.original_rating = rating   # Store the original rating
            play_count = lib.get_play_count(key)    # Get the play count of the selected video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    # Create a string with the video details    
            set_text(self.video_txt, video_details)  # Display the video details in the text widget
        else:   # If no video is selected
            set_text(self.video_txt, f"Please select a video!\n")   # Display a message in the text widget
        
        self.status_lbl.configure(text="Search button was clicked!")    # Update status label text

    def update_video_clicked(self): # Method to handle the "Update" button click event
        name = self.name_combo_box.get()    # Get the selected video name
        key = lib.get_key(name) # Get the key of the selected video
        rating = self.new_rating_combo_box.get()    # Get the selected rating

        if rating == "":    # If no rating is selected
            set_text(self.video_txt, f"Please select a rating!\n")  # Display a message in the text widget
        else:   # If a rating is selected
            rating = int(rating)    # Convert the rating to an integer
            lib.set_rating(key, rating) # Set the rating of the selected video
            
            new_rating = lib.get_rating(key)    # Get the new rating of the selected video
            video_details = f"{lib.get_name(key)}\n{lib.get_director(key)}\nrating: {new_rating}\nplays: {lib.get_play_count(key)}"   # Create a string with the video details
            set_text(self.video_txt, video_details)     # Display the video details in the text widget
        
        self.status_lbl.configure(text="Update button was clicked!")    # Update status label text
    
    def back_clicked(self): # Method to handle the "Back" button click event
        self.window.destroy()   # Destroy the window
        import video_player as vp   # Import the video_player module
        vp.window.deiconify()   # Restore the main window
     
    def reset_clicked(self):    # Method to handle the "Reset" button click event
        name = self.name_combo_box.get()    # Get the selected video name
        key = lib.get_key(name) # Get the key of the selected video
        lib.set_rating(key, self.original_rating)  # Reset the rating to the original rating
        video_details = f"{lib.get_name(key)}\n{lib.get_director(key)}\nrating: {self.original_rating}\nplays: {lib.get_play_count(key)}"   # Create a string with the video details
        set_text(self.video_txt, video_details)    # Display the video details in the text widget
        
        self.status_lbl.configure(text="Reset button was clicked!")   # Update status label text
        
if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()        # Create a TK object
    # fonts.configure()       # Configure the fonts
    UpdateVideos(window)     # Open the UpdateVideos GUI
    window.mainloop()       # Run the window main loop, reacting to button presses, etc