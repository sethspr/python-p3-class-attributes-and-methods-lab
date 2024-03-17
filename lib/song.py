class Song: 
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre): #constructor 
        self.name = name #instance attribute
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod 
    def add_song_to_count(self):
        self.count += 1

    @classmethod
    def add_to_genres(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    @classmethod
    def add_to_artists(self, artist):
        if artist not in self.artists:
            self.artists.append(artist)

    @classmethod
    def add_to_genre_count(self, genre):
        if genre not in self.genre_count:
            self.genre_count[genre] = 1
        else:
            self.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(self, artist):
        if artist not in self.artist_count:
            self.artist_count[artist] = 1
        else:
            self.artist_count[artist] += 1

        
    def __repr__(self):
        return f"<{self.name} is a {self.genre} song by artist {self.artist}.>"
    
my_song = Song("99 Problems", "Jay Z", "Rap")

print(my_song)