class Music:
    def __init__(self):
        self.name="N/A"
        self.artist="N/A"
        self.genre="N/A"

    def song(self):
        text = f"Song song_properties: Name-{self.name}, Artist-{self.artist}, Genre-{self.genre}"
        print(text)
        
    
    def setter(self, song_properties) -> None:
        if (len(song_properties) == 3):
            self.name = song_properties[0]
            self.artist = song_properties[1]
            self.genre = song_properties[2]
        elif(len(song_properties) == 2):
            self.name = song_properties[0]
            self.artist = song_properties[1]
            self.genre = "No Input"
        else:
            self.name = song_properties
            self.artist = "No Input"
            self.genre = "No Input"

        

def main():
    music = Music()
    song_properties = ["Flight of the Bumblebee", "Nikolai Rimsky-Korsakov", "Classical"]
    music.setter(song_properties)
    music.song()

    song_properties = ["Dance of The Violins", "F-777"]
    music.setter(song_properties)
    music.song()

    song_properties = "Cha Cha Slide"
    music.setter(song_properties)
    music.song()

if __name__=="__main__":
    main()