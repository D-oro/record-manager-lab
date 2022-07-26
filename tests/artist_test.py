import unittest

from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Ally", 1)

    def test_artist_has_name(self):
        self.assertEqual("Ally", self.artist.name)