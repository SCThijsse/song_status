import unittest

from fixture_helpers import fixture_path
from SongStatus_StreamlabsParameter import JsonDataParser


class TestJsonDataParser(unittest.TestCase):
    def test_missing_path(self):
        path = fixture_path("missing")
        parser = JsonDataParser(path).load()

        self.assertTrue(parser.is_success())
        self.assertEqual({}, parser.data)

    def test_json_parse_error(self):
        path = fixture_path("invalid")
        parser = JsonDataParser(path).load()

        self.assertFalse(parser.is_success())
        self.assertIn("Failed to parse", parser.error_message)

    def test_paused(self):
        path = fixture_path("paused")
        self.assertEqual(JsonDataParser(path).load().data["playing"], False)
