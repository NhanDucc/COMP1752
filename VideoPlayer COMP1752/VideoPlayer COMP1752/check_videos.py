import tkinter as tk    # Import the Tkinter module for creating GUI applications
from tkinter import ttk # Import the ttk module for themed widgets
import tkinter.scrolledtext as tkst # Import the scrolledtext module for creating a scrolled text widget
import video_library as lib     # Import the video_library module
import font_manager as fonts    # Import the font_manager module for managing fonts
from PIL import Image, ImageTk  # Import the Image and ImageTk modules from the Python Imaging Library (PIL)

def set_text(text_area, content):   # Function to set the text of a text area
    text_area.delete("1.0", tk.END) # Delete the current text in the text area
    text_area.insert(1.0, content)  # Insert the new text into the text area

class CheckVideos():    # Create the CheckVideos class
    def __init__(self, window): # Constructor method
        self.window = window    # Store the window in an instance variable
        # window.geometry("950x350")    # Set the window size
        window.title("Check Videos")    # Set the window title

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   # Create "List All Videos" button and assign the list_videos_clicked function to it
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)   # Place List All Videos button widget in the window

        enter_lbl = tk.Label(window, text="Choose Video Name")  # Create a label widget
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)   # Place the label widget in the window

        selected_option = tk.StringVar()    # Create a StringVar object to store the selected option
        names = ["Tom and Jerry", "Breakfast at Tiffany's", "Casablanca", "The Sound of Music", "Gone with the Wind"]    # Create a list of video names
        self.name_combo_box = ttk.Combobox(window, textvariable=selected_option, values=names)   # Create a Combobox widget with the list of video names
        self.name_combo_box.grid(row=0, column=2, padx=10, pady=10)   # Place the Combobox widget in the window

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   # Create "Check Video" button and assign the check_video_clicked function to it
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Place Check Video button widget in the window

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")   # Create a scrolled text widget
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place the scrolled text widget in the window

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   # Create a text widget
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Place the text widget in the window
        
        back_btn = tk.Button(window, text="Back", command=self.back_clicked)    # Create "Back" button and assign the back_clicked function to it
        back_btn.grid(row=2, column=3, padx=10, pady=10)    # Place Back button widget in the window
        
        clean_btn = tk.Button(window, text="Clean", command=self.clean_clicked) # Create "Clean" button and assign the clean_clicked function to it
        clean_btn.grid(row=2, column=4, padx=10, pady=10)   # Place Clean button widget in the window
        
        self.image_label = tk.Label(window)   # Create a label widget
        self.image_label.grid(row=1, column=4, padx=10, pady=10)    # Place the label widget in the window

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label for status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the label widget in the window
        
        self.list_videos_clicked()  # Call the list_videos_clicked method to list all videos

    def display_image(self, key):   # Method to display an image
        image_path = lib.get_image_path(key)    # Get the image path from the library
        image = Image.open(image_path)  # Open the image
        image = image.resize((200, 200))  # Adjust the size of the image as needed
        self.photo = ImageTk.PhotoImage(image)  # Create a PhotoImage object from the image
        self.image_label.configure(image=self.photo)    # Configure the label to display the image
        
    def clean_clicked(self):    # Method to handle the "Clean" button click event
        self.name_combo_box.delete(0, tk.END)   # Clear the Combobox widget
        set_text(self.video_txt, "")    # Clear the text widget
        self.image_label.configure(image="")    # Clear the label widget
        self.status_lbl.configure(text="Clean button was clicked!")   # Update status label text

    def check_video_clicked(self):  # Method to handle the "Check Video" button click event
        name = self.name_combo_box.get()    # Get the selected video name
        key = lib.get_key(name)   # Get the key of the selected video

        director = lib.get_director(key)    # Get the director of the selected video
        rating = lib.get_rating(key)    # Get the rating of the selected video
        play_count = lib.get_play_count(key)    # Get the play count of the selected video
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    # Create a string with the video details
        set_text(self.video_txt, video_details)   # Set the text of the text widget

        self.status_lbl.configure(text="Check Video button was clicked!")   # Update status label text
        self.display_image(key) # Call the display_image method to display the image of the selected video

    def list_videos_clicked(self):  # Method to handle the "List All Videos" button click event
        video_list = lib.list_all() # Get the list of all videos
        set_text(self.list_txt, video_list) # Set the text of the scrolled text widget
        self.status_lbl.configure(text="List Videos button was clicked!")   # Update status label text
    
    def back_clicked(self): # Method to handle the "Back" button click event
        self.window.destroy()   # Destroy the window
        import video_player as vp   # Import the video_player module
        vp.window.deiconify()   # Restore the main window

if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()        # Create a TK object
    # fonts.configure()       # Configure the fonts
    CheckVideos(window)     # Open the CheckVideo GUI
    window.mainloop()       # Run the window main loop, reacting to button presses, etc
