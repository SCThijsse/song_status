import unittest

from SongStatus_StreamlabsParameter import Messages, DisplayStatus, Settings
from fixture_helpers import fixture_path


class TestDisplayStatus(unittest.TestCase):
    def test_stopped(self):
        messages = Messages(Settings())
        status = DisplayStatus(fixture_path("missing"), messages)

        self.assertIsNone(status.error_message())
        self.assertEqual(messages.not_available(), status.title())
        self.assertEqual(messages.not_available(), status.artist())
        self.assertEqual(messages.stopped(), status.song_status())

    def test_paused(self):
        messages = Messages(Settings())
        status = DisplayStatus(fixture_path("paused"), messages)

        self.assertIsNone(status.error_message())
        self.assertEqual(messages.not_available(), status.title())
        self.assertEqual(messages.not_available(), status.artist())
        self.assertEqual(messages.paused(), status.song_status())

    def test_error(self):
        messages = Messages(Settings())
        status = DisplayStatus(fixture_path("invalid"), messages)

        self.assertIn("Failed", status.error_message())
        self.assertEqual(messages.not_available(), status.title())
        self.assertEqual(messages.not_available(), status.artist())
        self.assertEqual(Messages.PLAYER_ERROR, status.song_status())

    def test_playing(self):
        messages = Messages(Settings())
        status = DisplayStatus(fixture_path("playing"), messages)

        self.assertIsNone(status.error_message())
        self.assertEqual("Joy Division", status.artist())
        self.assertEqual("Shadowplay", status.title())
        self.assertEqual("Joy Division - Shadowplay", status.song_status())


