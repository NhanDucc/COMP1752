import tkinter as tk    # Import the Tkinter module for creating GUI applications
from tkinter import ttk # Import the ttk module for themed widgets
import tkinter.scrolledtext as tkst # Import the scrolledtext module for creating a scrolled text widget
import video_library as lib    # Import the video_library module
import font_manager as fonts    # Import the font_manager module for managing fonts

playlists = []  # Create an empty list to store the videos

def set_text(text_area, content):   # Function to set the text of a text area
    text_area.insert(tk.END, content)   # Insert the new text into the text area

class CreateVideos():   # Create the CreateVideos class
    def __init__(self, window): # Constructor method
        self.window = window    # Store the window in an instance variable
        # window.geometry("750x360")    # Set the window size
        window.title("Create Video List")   # Set the window title

        enter_number_lbl = tk.Label(window, text="Choose Video Name")   # Create a label widget
        enter_number_lbl.grid(row=0, column=0, padx=10, pady=10)    # Place the label widget in the window

        selected_option = tk.StringVar()    # Create a StringVar object to store the selected option    
        name = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=name)   # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=1, padx=10, pady=10)   # Place the Combobox widget in the window

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_video_clicked)   # Create "Add to Playlist" button and assign the add_video_clicked function to it
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)   # Place Add to Playlist button widget in the window

        self.list_txt = tk.Text(window, width=30, height=5)  # Create a text widget
        self.list_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   # Place the text widget in the window
        
        self.video_txt = tkst.ScrolledText(window, width=45, height=10)  # Create a scrolled text widget
        self.video_txt.grid(row=1, column=2, columnspan=2, padx=10, pady=10)    # Place the scrolled text widget in the window

        play_video_btn = tk.Button(window, text="Play", command=self.play_video_clicked)    # Create "Play" button and assign the play_video_clicked function to it
        play_video_btn.grid(row=2, column=0, padx=10, pady=10)  # Place Play button widget in the window

        clean_btn = tk.Button(window, text="Clean", command=self.clean_clicked)   # Create "Clean" button and assign the clean_clicked function to it
        clean_btn.grid(row=2, column=1, padx=10, pady=10)   # Place Clean button widget in the window
        
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)  # Create "Reset" button and assign the reset_clicked function to it
        reset_btn.grid(row=2, column=2, padx=10, pady=10)   # Place Reset button widget in the window
        
        back_btn = tk.Button(window, text="Back", command=self.back_clicked)    # Create "Back" button and assign the back_clicked function to it
        back_btn.grid(row=2, column=3, padx=10, pady=10)    # Place Back button widget in the window

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window
    
    def add_video_clicked(self):    # Method to handle the "Add to Playlist" button click event
        name = self.name_combo_box.get()    # Get the selected video name
        if name == "":  # If no video is selected
            set_text(self.video_txt, f"Please select a video!\n")   # Display a message in the scrolled text widget
            self.video_txt.see(tk.END)  # Scroll to the end
        else:   # If a video is selected
            if name in playlists:   # If the video is already in the playlist
                set_text(self.video_txt, f"Video already exists in the playlist!\n")    # Display a message in the scrolled text widget
                self.video_txt.see(tk.END)  # Scroll to the end
            else:   # If the video is not in the playlist
                playlists.append(name)  # Add the video to the playlist
                set_text(self.list_txt, f"{name}\n")    # Display the video name in the text widget
                self.video_txt.see(tk.END)  # Scroll to the end
                self.status_lbl.configure(text="Add to Playlist button was clicked!")   # Update status label text
               
    def play_video_clicked(self):   # Method to handle the "Play" button click event
        for name in playlists:  # For each video in the playlist
            key = lib.get_key(name) # Get the key of the video
            lib.increment_play_count(key)   # Increment the play count for each video
            play_count = lib.get_play_count(key)    # Get the play count for each video
        
        video_details = f"This playlist is played {play_count} time(s)\n"   # Create a string with the play count
        self.video_txt.see(tk.END)  # Scroll to the end
        set_text(self.video_txt, video_details)  # Set the text of the text widget
            
        self.status_lbl.configure(text="Play Playlist button was clicked!")  # Update status label text

    def clean_clicked(self):    # Method to handle the "Clean" button click event
        self.list_txt.delete(1.0, tk.END)   # Clear the text widget
        self.name_combo_box.delete(0, tk.END)   # Clear the Combobox widget
        self.video_txt.delete(1.0, tk.END)  # Clear the scrolled text widget
        
        self.status_lbl.configure(text="Clean button was clicked!")  # Update status label text
        
    def reset_clicked(self):    # Method to handle the "Reset" button click event
        for name in playlists:  # For each video in the playlist
            key = lib.get_key(name) # Get the key of the video
            lib.reset_play_count(key)  # Reset play count for each video
            set_text(self.video_txt, f"Play count for this playlist has been reset!\n")   # Display a message in the scrolled text widget
            self.video_txt.see(tk.END)  # Scroll to the end
        
        self.status_lbl.configure(text="Reset button was clicked!")     # Update status label text
    
    def back_clicked(self): # Method to handle the "Back" button click event
        self.window.destroy()   # Destroy the window
        import video_player as vp   # Import the video_player module
        vp.window.deiconify()   # Restore the main window
     
if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()        # Create a TK object
    # fonts.configure()       # Configure the fonts
    CreateVideos(window)     # Open the CreateVideos GUI
    window.mainloop()       # Run the window main loop, reacting to button presses, etc