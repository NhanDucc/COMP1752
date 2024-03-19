import tkinter as tk                    # Import the Tkinter module for creating GUI applications
from tkinter import ttk                 # Import the ttk module for themed widgets
import tkinter.scrolledtext as tkst     # Import the scrolledtext module for creating a scrolled text widget
import font_manager as fonts            # Import the font_manager module for managing fonts
from PIL import Image, ImageTk          # Import the Image and ImageTk modules from the Python Imaging Library (PIL)
import os                               # Import the os module for interacting with the operating system
import video_library as lib             # Import the video_library module

playlists = []  # Create an empty list to store the videos

def set_text(text_area, content):       # Function to set the text of a text area
    text_area.insert(1.0, content)      # Insert the new text into the text area

class CheckVideos():                    # Create the CheckVideos class
    def __init__(self, window):         # Constructor method
        self.window = window            # Store the window in an instance variable

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   # Create "List All Videos" button and assign the list_videos_clicked function to it
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                         # Place List All Videos button widget in the window

        enter_lbl = tk.Label(window, text="Choose Video Name")  # Create a label widget
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)       # Place the label widget in the window

        selected_option = tk.StringVar()                                                                                 # Create a StringVar object to store the selected option
        names = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=names)                           # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=2, padx=10, pady=10)                                                      # Place the Combobox widget in the window

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   # Create "Check Video" button and assign the check_video_clicked function to it
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)                                     # Place Check Video button widget in the window

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")      # Create a scrolled text widget
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place the scrolled text widget in the window

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")    # Create a text widget
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Place the text widget in the window
        
        clean_btn = tk.Button(window, text="Clean", command=self.clean_clicked) # Create "Clean" button and assign the clean_clicked function to it
        clean_btn.grid(row=2, column=3, padx=10, pady=10)                       # Place Clean button widget in the window
        
        self.image_label = tk.Label(window)                         # Create a label widget
        self.image_label.grid(row=1, column=4, padx=10, pady=10)    # Place the label widget in the window

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window
        
        self.list_videos_clicked()  # Call the list_videos_clicked method to list all videos

    def display_image(self, key):                                   # Method to display the image of a video
        image_path = lib.get_image_path(key)                        # Get the image path of the video
        if image_path is not None and os.path.isfile(image_path):   # If the image path is not None and the image file exists
            image = (Image.open(image_path)).resize((200, 200))     # Open the image and adjust the size as needed
            self.photo = ImageTk.PhotoImage(image)                  # Create a PhotoImage object from the image
            self.image_label.configure(image=self.photo)            # Configure the label to display the image
        else:                                                       # If the image path does not exist
            self.image_label.configure(image=None)                  # Clear the label widget

    def check_video_clicked(self):                                                          # Method to handle the "Check Video" button click event
        name = self.name_combo_box.get()                                                    # Get the selected video name
        if name == "":                                                                      # If no video is selected
            self.video_txt.delete(1.0, tk.END)                                               # Clear the text widget
            set_text(self.video_txt, f"Please select a video!\n")                           # Display a message in the text widget
        else:                                                                               # If a video is selected
            key = lib.get_key(name)                                                         # Get the key of the selected video
            director = lib.get_director(key)                                                # Get the director of the selected video
            rating = lib.get_rating(key)                                                    # Get the rating of the selected video
            play_count = lib.get_play_count(key)                                            # Get the play count of the selected video
            self.video_txt.delete(1.0, tk.END)                                               # Clear the text widget
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"    # Create a string with the video details
            set_text(self.video_txt, video_details)                                         # Set the text of the text widget
        self.status_lbl.configure(text="Check Video button was clicked!")                   # Update status label text
        self.display_image(key)                                                             # Call the display_image method to display the image of the selected video

    def clean_clicked(self):                                            # Method to handle the "Clean" button click event
        self.name_combo_box.delete(0, tk.END)                           # Clear the Combobox widget
        self.video_txt.delete(1.0, tk.END)                                   # Clear the text widget
        lib.remove_image                                                # Delete image
        self.image_label.configure(image="")                            # Clear the label widget
        self.status_lbl.configure(text="Clean button was clicked!")     # Update status label text

    def list_videos_clicked(self):                                          # Method to handle the "List All Videos" button click event
        self.list_txt.delete(1.0, tk.END)                                   # Clear the text widget
        video_list = lib.list_all()                                         # Get the list of all videos
        set_text(self.list_txt, video_list)                                 # Set the text of the scrolled text widget
        self.status_lbl.configure(text="List Videos button was clicked!")   # Update status label text

class CreateVideos():                       # Create the CreateVideos class
    def __init__(self, window):             # Constructor method
        self.window = window                # Store the window in an instance variable

        enter_name_lbl = tk.Label(window, text="Choose Video Name")   # Create a label widget
        enter_name_lbl.grid(row=0, column=0, padx=10, pady=10)        # Place the label widget in the window

        selected_option = tk.StringVar()                                                                                # Create a StringVar object to store the selected option    
        name = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=name)                           # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=1, padx=10, pady=10)                                                     # Place the Combobox widget in the window

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_video_clicked)   # Create "Add to Playlist" button and assign the add_video_clicked function to it
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)                                       # Place Add to Playlist button widget in the window

        self.list_txt = tk.Text(window, width=30, height=5)                   # Create a text widget
        self.list_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   # Place the text widget in the window
        
        self.video_txt = tk.Text(window, width=45, height=5)         # Create a scrolled text widget
        self.video_txt.grid(row=1, column=2, columnspan=2, padx=10, pady=10)    # Place the scrolled text widget in the window

        play_video_btn = tk.Button(window, text="Play", command=self.play_video_clicked)    # Create "Play" button and assign the play_video_clicked function to it
        play_video_btn.grid(row=2, column=0, padx=10, pady=10)                              # Place Play button widget in the window

        clean_btn = tk.Button(window, text="Clean", command=self.clean_clicked)   # Create "Clean" button and assign the clean_clicked function to it
        clean_btn.grid(row=2, column=1, padx=10, pady=10)                         # Place Clean button widget in the window
        
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)  # Create "Reset" button and assign the reset_clicked function to it
        reset_btn.grid(row=2, column=2, padx=10, pady=10)                        # Place Reset button widget in the window
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window
    
    def add_video_clicked(self):                                                        # Method to handle the "Add to Playlist" button click event
        name = self.name_combo_box.get()                                                # Get the selected video name
        if name == "":                                                                  # If no video is selected
            self.video_txt.delete(1.0, tk.END)                                   # Clear the text widget
            set_text(self.video_txt, f"Please select a video!\n")                       # Display a message in the scrolled text widget
        else:                                                                           # If a video is selected
            if name in playlists:                                                       # If the video is already in the playlist
                self.video_txt.delete(1.0, tk.END)
                set_text(self.video_txt, f"Video already exists in the playlist!\n")    # Display a message in the scrolled text widget
            else:                                                                       # If the video is not in the playlist
                playlists.append(name)                                                  # Add the video to the playlist
                self.video_txt.delete(1.0, tk.END)
                set_text(self.list_txt, f"{name}\n")                                    # Display the video name in the text widget
                set_text(self.video_txt, f"{name} has been added to the playlist!\n")   # Display a message in the scrolled text widget
                self.status_lbl.configure(text="Add to Playlist button was clicked!")   # Update status label text
               
    def play_video_clicked(self):                                               # Method to handle the "Play" button click event
        for name in playlists:                                                  # For each video in the playlist
            key = lib.get_key(name)                                             # Get the key of the video
            lib.increment_play_count(key)                                       # Increment the play count for each video
            play_count = lib.get_play_count(key)                                # Get the play count for each video
        self.video_txt.delete(1.0, tk.END)
        video_details = f"This playlist is played {play_count} time(s)\n"       # Create a string with the play count
        set_text(self.video_txt, video_details)                                 # Set the text of the text widget
        self.status_lbl.configure(text="Play Playlist button was clicked!")     # Update status label text

    def clean_clicked(self):                                            # Method to handle the "Clean" button click event
        self.list_txt.delete(1.0, tk.END)                               # Clear the text widget
        self.name_combo_box.delete(0, tk.END)                           # Clear the Combobox widget
        self.video_txt.delete(1.0, tk.END)                              # Clear the scrolled text widget
        self.status_lbl.configure(text="Clean button was clicked!")     # Update status label text
        
    def reset_clicked(self):                                                            # Method to handle the "Reset" button click event
        for name in playlists:                                                          # For each video in the playlist
            key = lib.get_key(name)                                                     # Get the key of the video
            lib.reset_play_count(key)                                                   # Reset play count for each video
        playlists.clear()                                                               # Clear the playlist
        self.list_txt.delete(1.0, tk.END)                                               # Clear the text widget
        self.name_combo_box.delete(0, tk.END)                                           # Clear the Combobox widget# Clear the playlist
        self.video_txt.delete(1.0, tk.END)
        set_text(self.video_txt, f"This playlist has been removed!\n")                  # Display a message in the scrolled text widget 
        set_text(self.video_txt, f"Play count for this playlist has been reset!\n")     # Display a message in the scrolled text widget
        self.status_lbl.configure(text="Reset button was clicked!")                     # Update status label text

class UpdateVideos():                   # Create the UpdateVideos class
    def __init__(self, window):         # Constructor method
        self.window = window            # Store the window in an instance variable
        
        enter_name_lbl = tk.Label(window, text="Choose Video Name")   # Create a label widget
        enter_name_lbl.grid(row=0, column=0, padx=10, pady=10)        # Place the label widget in the window
        
        selected_option = tk.StringVar()                                                                                 # Create a StringVar object to store the selected option
        names = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=names)                           # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=1, padx=10, pady=10)                                                      # Place the Combobox widget in the window

        search_video_btn = tk.Button(window, text="Search", command=self.search_video_clicked)  # Create "Search" button and assign the search_video_clicked function to it
        search_video_btn.grid(row=0, column=2, padx=10, pady=10)                                # Place Search button widget in the window
        
        self.video_txt = tk.Text(window, width=25, height=5)    # Create a text widget
        self.video_txt.grid(row=1, column=2, padx=10, pady=10)  # Place the text widget in the window
        
        new_rating_lbl = tk.Label(window, text="Chosse New Rating")   # Create a label widget
        new_rating_lbl.grid(row=1, column=0, padx=10, pady=10)        # Place the label widget in the window
        
        self.new_rating_combo_box = ttk.Combobox(window, values=[1, 2, 3, 4, 5])    # Create a Combobox widget with the list of ratings
        self.new_rating_combo_box.grid(row=1, column=1, padx=10, pady=10)           # Place the Combobox widget in the window
        
        update_btn = tk.Button(window, text="Update", command=self.update_video_clicked)    # Create "Update" button and assign the update_video_clicked function to it
        update_btn.grid(row=2, column=0, padx=10, pady=10)                                  # Place Update button widget in the window
        
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)     # Create "Reset" button and assign the reset_clicked function to it
        reset_btn.grid(row=2, column=1, padx=10, pady=10)                           # Place Reset button widget in the window
                
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window

    def get_key_by_name(self):                      # Method to get the key of the selected video
        name = self.name_combo_box.get()    # Get the selected video name
        key = self.lib.get_key(name)        # Get the key of the selected video
        return key                          # Return the key of the selected video

    def search_video_clicked(self):                                                         # Method to handle the "Search" button click event
        name = self.name_combo_box.get()                                                    # Get the selected video name
        key = lib.get_key(name)                                                        # Get the key of the selected video
        if name != "":                                                                      # If a video is selected
            director = lib.get_director(key)                                                # Get the director of the selected video
            rating = lib.get_rating(key)                                                    # Get the rating of the selected video
            self.original_rating = rating                                                   # Store the original rating
            play_count = lib.get_play_count(key)                                            # Get the play count of the selected video
            self.video_txt.delete(1.0, tk.END)                                   # Clear the text widget
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"    # Create a string with the video details    
            set_text(self.video_txt, video_details)                                         # Display the video details in the text widget
        else:                                                                               # If no video is selected
            set_text(self.video_txt, f"Please select a video!\n")                           # Display a message in the text widget
        self.status_lbl.configure(text="Search button was clicked!")                        # Update status label text

    def update_video_clicked(self):                                                                                                   # Method to handle the "Update" button click eventme
        key = lib.get_key(self.name_combo_box.get())                                                                                                  # Get the key of the selected video
        rating = self.new_rating_combo_box.get()                                                                                      # Get the selected rating
        if rating == "":                                                                                                              # If no rating is selected
            set_text(self.video_txt, f"Please select a rating!\n")                                                                    # Display a message in the text widget
        else:                                                                                                                         # If a rating is selected
            rating = int(rating)                                                                                                      # Convert the rating to an integer
            lib.set_rating(key, rating)                                                                                               # Set the rating of the selected video
            new_rating = lib.get_rating(key)                                                                                          # Get the new rating of the selected video
            self.video_txt.delete(1.0, tk.END)                                                                                        # Clear the text widget
            video_details = f"Name: {lib.get_name(key)}\nDirector: {lib.get_director(key)}\nRating: {new_rating}\nPlays: {lib.get_play_count(key)}"   # Create a string with the video details
            set_text(self.video_txt, video_details)                                                                                   # Display the video details in the text widget
        self.status_lbl.configure(text="Update button was clicked!")                                                                  # Update status label text
     
    def reset_clicked(self):                                                                                                                # Method to handle the "Reset" button click event
        key = lib.get_key(self.name_combo_box.get())                                                                                        # Get the key of the selected video
        lib.set_rating(key, self.original_rating)                                                                                           # Save the original rating
        self.video_txt.delete(1.0, tk.END)                                                                                                  # Reset the rating to the original rating
        video_details = f"Name: {lib.get_name(key)}\nDirector: {lib.get_director(key)}\nRating: {self.original_rating}\nPlays: {lib.get_play_count(key)}"   # Create a string with the video details
        set_text(self.video_txt, video_details)                                                                                             # Display the video details in the text widget
        self.status_lbl.configure(text="Reset button was clicked!")                                                                         # Update status label text

class FilterVideos():                    # Create the FilterVideos class
    def __init__(self, window):
        self.window = window
        
        enter_name_director_lbl = tk.Label(window, text="Choose Director Name")   # Create a label widget
        enter_name_director_lbl.grid(row=0, column=0, padx=10, pady=10)          # Place the label widget in the window
        
        selected_option = tk.StringVar()                                                                                     # Create a StringVar object to store the selected option
        directors = ["Fred Quimby", "Blake Edwards", "Michael Curtiz", "Robert Wise", "Victor Fleming"]                        # Create a list of director names
        self.director_combo_box = ttk.Combobox(window, textvariable=selected_option, values=directors)                           # Create a Combobox widget with the list of director names
        self.director_combo_box.grid(row=0, column=1, padx=10, pady=10)                                                        # Place the Combobox widget in the window
        
        filter_video_btn = tk.Button(window, text="Filter", command=self.filter_video_clicked)  # Create "Filter" button and assign the filter_video_clicked function to it
        filter_video_btn.grid(row=0, column=2, padx=10, pady=10)                                # Place Filter button widget in the window
        
        self.list_txt = tkst.ScrolledText(window, width=45, height=10)    # Create a scrolled text widget
        self.list_txt.grid(row=1, column=0, padx=10, pady=10)             # Place the scrolled text widget in the window
        
        self.video_txt = tk.Text(window, width=30, height=5)    # Create a text widget
        self.video_txt.grid(row=1, column=1, padx=10, pady=10)  # Place the text widget in the window
        
        clean_btn = tk.Button(window, text="Clean", command=self.clean_clicked)   # Create "Clean" button and assign the clean_clicked function to it
        clean_btn.grid(row=2, column=2, padx=10, pady=10)                         # Place Clean button widget in the window
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window
        
    def filter_video_clicked(self):                                                                 # Method to handle the "Filter" button click event
        director = self.director_combo_box.get()                                                       # Get the selected director name
        key = lib.get_key_by_director(director)
        if director != "":                                                                            # If no director is selected
            self.list_txt.delete(1.0, tk.END) 
            self.video_txt.delete(1.0, tk.END)
            video_details = f"Name: {lib.get_name(key)}\nDirector: {director}\nRating: {lib.get_rating(key)}\nPlays: {lib.get_play_count(key)}"   # Create a string with the video details
            set_text(self.list_txt, video_details)                                                   # Display the video details in the text widget
            set_text(self.video_txt, f"{lib.get_name(key)} has been filtered!\n")      # Display a message in the text widget
        else:
            self.video_txt.delete(1.0, tk.END)
            set_text(self.video_txt, f"Please select an director!\n")                                 # Display a message in the text widget 
        self.status_lbl.configure(text="Filter button was clicked!") 
    
    def clean_clicked(self):                                            # Method to handle the "Clean" button click event
        self.director_combo_box.delete(0, tk.END)                       # Clear the Combobox widget
        self.list_txt.delete(1.0, tk.END)                               # Clear the scrolled text widget
        self.video_txt.delete(1.0, tk.END)                              # Clear the text widget
        self.status_lbl.configure(text="Clean button was clicked!")     # Update status label text
        

window = tk.Tk()                        # Create a Tkinter window
window.title("Video Player App")        # Set the title of the window
tab_control = ttk.Notebook(window)      # Create a tab control widget
fonts.configure()                       # Call the configure method to configure the fonts

# First tab
tab_1 = ttk.Frame(tab_control)                      # Create a frame widget
tab_control.add(tab_1, text="Check Videos")         # Add the frame widget to the tab control
CheckVideos(tab_1)                                  # Create the CheckVideos object

# Create a spacer tab
spacer_1 = ttk.Frame(tab_control)
tab_control.add(spacer_1, text=" ")
tab_control.tab(spacer_1, state='disabled')

# Second tab
tab_2 = ttk.Frame(tab_control)                      # Create a frame widget
tab_control.add(tab_2, text="Create Videos")        # Add the frame widget to the tab control
CreateVideos(tab_2)                                 # Create the CreateVideos object

# Create a spacer tab
spacer_2 = ttk.Frame(tab_control)
tab_control.add(spacer_2, text=" ")
tab_control.tab(spacer_2, state='disabled')

# Third tab
tab_3 = ttk.Frame(tab_control)                      # Create a frame widget
tab_control.add(tab_3, text="Update Videos")        # Add the frame widget to the tab control
UpdateVideos(tab_3)                                 # Create the UpdateVideos object

# Create a spacer tab
spacer_3 = ttk.Frame(tab_control)
tab_control.add(spacer_3, text=" ")
tab_control.tab(spacer_3, state='disabled')

tab_4 = ttk.Frame(tab_control)                      # Create a frame widget
tab_control.add(tab_4, text="Filter Videos")        # Add the frame widget to the tab control
FilterVideos(tab_4)                                 # Create the FilterVideos object

tab_control.pack(expand=1, fill="both")     # Pack the tab control widget

window.mainloop()       # Call the mainloop method to run the application