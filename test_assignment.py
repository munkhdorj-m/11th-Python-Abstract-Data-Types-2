import pytest
from assignment import Playlist
def test_playlist_add_and_count():
    p = Playlist()
    p.add_song("Imagine", "John Lennon")
    p.add_song("Hey Jude", "The Beatles")
    assert p.count_songs() == 2


def test_playlist_delete():
    p = Playlist()
    p.add_song("Imagine", "John Lennon")
    p.add_song("Numb", "Linkin Park")
    p.add_song("Hey Jude", "The Beatles")
    p.delete_song("Numb")
    assert p.count_songs() == 2


def test_playlist_show():
    p = Playlist()
    p.add_song("Imagine", "John Lennon")
    p.add_song("Hey Jude", "The Beatles")
    expected = (
        "1. Imagine - John Lennon\n"
        "2. Hey Jude - The Beatles"
    )
    assert p.show_playlist() == expected
