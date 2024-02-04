class Music:
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    @property
    def song(self):
        return self.name, self.artist, self.genre
    
    @song.setter
    def song(self, new_name):
        if not isinstance(new_name, str):
            if (len(new_name) == 2):
                val3 = "No input"
                val1, val2 = new_name
            else:
                val1 , val2, val3 = new_name
        else:
            val1 = new_name
            val2 = "No input"
            val3 = "No input"
        self.name = val1
        self.artist = val2
        self.genre = val3

def main():
    music = Music("William Tell Oveture", "Gioachino Rossini", "Classical")
    print("Song Properties: ", music.song)

    music.song = ["One Life Short", "Geoxor"]
    print("Song Properties after change: ", music.song)

    music.song = "Dynamite"
    print("Song Properties after final change: ", music.song)

if __name__=="__main__":
    main()