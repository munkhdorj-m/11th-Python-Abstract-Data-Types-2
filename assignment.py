class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new = SongNode(title, artist)
        if not self.head:
            self.head = new
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def delete_song(self, title):
        if not self.head:
            return

        if self.head.title == title:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next and curr.next.title != title:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

    def show_playlist(self):
        curr = self.head
        if not curr:
            return ""

        result = []
        i = 1
        while curr:
            result.append(f"{i}. {curr.title} - {curr.artist}")
            curr = curr.next
            i += 1
        return "\n".join(result)

    def count_songs(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
