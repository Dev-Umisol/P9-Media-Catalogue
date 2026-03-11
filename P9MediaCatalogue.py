# Building a Media Catalogue

class Movie:
    """Parent class representing a movie."""
    
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
    
class TVSeries(Movie):
    """Child class representing an entire TV series."""
    
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        
        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")
        
        self.seasons = seasons
        self.total_episodes = total_episodes
        
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"
    
class MediaCatalogue:
    def __init__(self):
        self.items = [] # Empty List

    def add(self, media_item):
        self.items.append(media_item)
        
    def __str__(self):
        if self.items == []:
            return "Media Catalogue (empty)"
        
        result = f"Media Catalogue ({len(self.items)} items):\n\n" # <-- number of items(movies) in the catalogue
        
        for n, movie in enumerate(self.items, 1):
            result += f"{n}. {movie}\n"
        return result

catalogue = MediaCatalogue()

try:
    movie1 = Movie("Swiss Army Man", 2016, "Daniel Scheinert and Daniel Kwan", 97)
    catalogue.add(movie1)
    
    movie2 = Movie("The Matrix", 1999, "The Wachowskis", 136)
    catalogue.add(movie2)
    
    series1 = TVSeries("The Flash", 2014, "Greg Berlanti, Andrew Kreisberg, and Geoff Johns", 30, 9, 184)
    catalogue.add(series1)
    
    series2 = TVSeries("Scrubs", 2001, "Bill Lawrence", 24, 9, 182)
    catalogue.add(series2)
    # print(series1)
    print(catalogue)
except ValueError as e:
    print(f"Validation Error: {e}")

# print(movie1.__doc__)
# print(series1.__doc__)
# print(movie1)