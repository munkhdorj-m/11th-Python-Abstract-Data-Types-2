# Exercise 1
class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        # TODO: implement
        pass

    def delete_song(self, title):
        # TODO: implement
        pass

    def show_playlist(self):
        # numbered list
        # "1. Imagine - John Lennon\n2. Hey Jude - The Beatles"
        pass

    def count_songs(self):
        # return integer count
        pass
