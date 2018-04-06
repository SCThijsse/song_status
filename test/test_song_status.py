import unittest
from fixture_helpers import fixture_path
from SongStatus_StreamlabsParameter import SongStatus, JsonDataParser


def song_status(fixture_name):
    path = fixture_path(fixture_name)
    parser = JsonDataParser(path).load()
    return SongStatus(parser.data)


class TestSongStatus(unittest.TestCase):

    def test_paused(self):
        status = song_status("paused")

        self.assertFalse(status.is_playing())

        self.assertTrue(status.is_paused())
        self.assertFalse(status.is_stopped())

        self.assertIsNone(status.artist())
        self.assertIsNone(status.title())

    def test_stopped(self):
        status = song_status("missing")

        self.assertFalse(status.is_playing())

        self.assertFalse(status.is_paused())
        self.assertTrue(status.is_stopped())

        self.assertIsNone(status.artist())
        self.assertIsNone(status.title())

    def test_playing(self):
        status = song_status("playing")

        self.assertTrue(status.is_playing())
        self.assertFalse(status.is_paused())
        self.assertFalse(status.is_stopped())

    def test_artist(self):
        self.assertEqual("Joy Division", song_status("playing").artist(), "Joy Division")

    def test_title(self):
        self.assertEqual("Shadowplay", song_status("playing").title())
