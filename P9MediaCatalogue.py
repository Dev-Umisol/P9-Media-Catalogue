# Building a Media Catalogue

class Movie:
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if year < 1895:
            raise ValueError("Year must be 1895 or later") # <-- First ever movie came out in 1985
        
        if director == '' or not director.strip(' '):
            raise ValueError("Director cannot be empty")
        
        if duration <= 0:
            raise ValueError("Duration must be positive")
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class MediaCatalogue:
    def __init__(self):
        self.items = [] # Empty List

    def add(self, media_item):
        self.items.append(media_item)
        
    def __str__(self):
        if self.items == []:
            return "Media Catalogue (empty)"
        
        result = f"Media Catalogue ({len(self.items)} items):\n\n" # <-- number of items(movies) in the catalogue
        
try:
    movie1 = Movie("Swiss Army Man", 2016, "Daniel Scheinert and Daniel Kwan", 97)
except ValueError as e:
    print(f"Validation Error: {e}")
    
# print(movie1)