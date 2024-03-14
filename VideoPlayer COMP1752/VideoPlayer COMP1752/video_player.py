import tkinter as tk                    # Import the Tkinter module for creating GUI applications
import sys                              # Import the sys module for system-specific parameters and functions
import font_manager as fonts            # Import the font_manager module for managing fonts
from check_videos import CheckVideos    # Import the CheckVideos class from the check_videos module
from create_videos import CreateVideos  # Import the CreateVideos class from the create_videos module
from update_videos import UpdateVideos  # Import the UpdateVideos class from the update_videos module

current_font = None     # Create a variable to store the current font

def check_videos_clicked():                                                     # Function to handle the "Check Videos" button click event
    status_lbl.configure(text="Check Videos button was clicked!")               # Update status label text
    window.withdraw()                                                           # Hide the main window
    new_window = tk.Toplevel(window)                                            # Create a new top-level window
    new_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(new_window))     # Handle window closing event
    CheckVideos(new_window)                                                     # Instantiate the CheckVideos class with the new window

def create_video_list_clicked():                                                # Function to handle the "Create Video List" button click event
    status_lbl.configure(text="Create Video List button was clicked!")          # Update status label text
    window.withdraw()                                                           # Hide the main window
    new_window = tk.Toplevel(window)                                            # Create a new top-level window
    new_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(new_window))     # Handle window closing event
    CreateVideos(new_window)                                                    # Instantiate the CreateVideos class with the new window

def update_video_clicked():                                                   # Function to handle the "Update Videos" button click event
    status_lbl.configure(text="Update Videos button was clicked!")            # Update status label text
    window.withdraw()                                                         # Hide the main window
    new_window = tk.Toplevel(window)                                          # Create a new top-level window
    new_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(new_window))   # Handle window closing event
    UpdateVideos(new_window)                                                  # Instantiate the UpdateVideos class with the new window

def on_closing(new_window):             # Function to handle the closing of secondary windows
    window.deiconify()                  # Restore the main window when the secondary window is closed
    new_window.destroy()                # Destroy the secondary window
    if current_font is not None:        # If the current font is not None
        fonts.configure(current_font)   # Re-apply the font configuration

    
window = tk.Tk()                # Create a TK object
# window.geometry("520x150")    # Set the window size
window.title("Video Player")    # Set the window title

fonts.configure()    # TẠI SAO LẠI BỊ LỖI KHI BACK VỀ TỪ CÁC WINDOW KHÁC  # Configure the fonts

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")   # Create a label widget
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)                              # Place the label widget in the window

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)   # Create "Check Videos" button and assign the check_videos_clicked function to it
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)                                  # Place Check Videos button widget in the window

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked)  # Create "Create Videos List" button and assign the create_video_list_clicked function to it
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)                                           # Place Create Videos List button widget in the window

update_videos_btn = tk.Button(window, text="Update Videos", command=update_video_clicked)   # Create "Update Videos" button and assign the update_video_clicked function to it
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)                                   # Place Update Videos button widget in the window

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))      # Create a label for status messages
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)    # Place the label widget in the window

window.protocol("WM_DELETE_WINDOW", sys.exit)   # Handle the main window closing event
window.mainloop()                               # Start the Tkinter event loop


#Mở từ cehck_videos.py thì ảnh bình thường, nhưng mở từ đây thì bị lỗi, font cũng tương tụ
