import unittest
from SongStatus_StreamlabsParameter import Settings
from fixture_helpers import fixture_path


class TestSettings(unittest.TestCase):
    def test_defaults(self):
        settings = Settings()

        self.assertEquals(False, settings.is_debug())
        self.assertEquals("N/A", settings.not_available_message())
        self.assertEquals("Player paused.", settings.paused_message())
        self.assertEquals("Player stopped.", settings.stopped_message())
        self.assertEquals("{artist} - {title}", settings.status_format())

    def test_load(self):
        settings = Settings().load_from_file(fixture_path("settings"))

        self.assertEquals(True, settings.is_debug())

        self.assertEquals("N/A", settings.not_available_message())
        self.assertEquals("TEST Player paused.", settings.paused_message())
        self.assertEquals("TEST Player stopped.", settings.stopped_message())
        self.assertEquals("TEST %{artist} - %{title}", settings.status_format())

