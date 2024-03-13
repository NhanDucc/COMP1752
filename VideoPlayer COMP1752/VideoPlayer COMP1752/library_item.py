class LibraryItem:  # Create a class called LibraryItem
    def __init__(self, name, director, rating=0, image_path=None):  # Constructor method
        self.name = name    # Store the name in an instance variable
        self.director = director    # Store the director in an instance variable
        self.rating = rating    # Store the rating in an instance variable
        self.play_count = 0 # Store the play count in an instance variable
        self.image_path = image_path    # Store the image path in an instance variable

    def info(self): # Method to return the details of the library item
        return f"{self.name} - {self.director} {self.stars()}"  # Return the name, director, and rating of the library item

    def stars(self):    # Method to return the rating of the library item as stars
        stars = ""  # Create an empty string
        for i in range(self.rating):    # For each star
            stars += "*"    # Add a star to the string
        return stars    # Return the string with stars
