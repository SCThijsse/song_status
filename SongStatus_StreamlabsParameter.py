import sys
import os
import json
import codecs

ScriptName = "Google Play Current Song"
Website = "https://github.com/nvloff/song_status"
Description = "Provides variables to show the currently playing song from Google Desktop Player"
Creator = "Nikolai Vladimirov<nikolay@vladimiroff.com>"

Version = "1.0.0.0"

m_SongStatusVar = "$song_status"


class Messages:
    IO_ERROR = "I/O error({0}): {1} reading file {2}"
    JSON_PARSE_ERROR = "Failed to parse JSON file at %s"
    UNKNOWN_ERROR = "Unknown exception %s"
    PLAYER_ERROR = "Error loading song."

    def __init__(self, settings):
        self._settings = settings

    def not_available(self):
        return self._settings.not_available_message()

    def stopped(self):
        return self._settings.stopped_message()

    def paused(self):
        return self._settings.paused_message()

    def status_format(self):
        return self._settings.status_format()

    def offline(self):
        return self._settings.offline_message()


class JsonDataParser:
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.error_message = None
        self.load_error = False

    def load(self):
        # if file is not present the player is probably stopped
        if not os.path.isfile(self.path):
            return self

        try:
            with open(self.path, "r") as f:
                self.data = json.load(f)
        except IOError as (errno, strerror):
            self.set_load_error(Messages.IO_ERROR.format(errno, strerror, self.path))
        except ValueError:
            self.set_load_error(Messages.JSON_PARSE_ERROR % self.path)
        except:
            self.set_load_error(Messages.UNKNOWN_ERROR % sys.exc_info()[0])

        return self

    def is_success(self):
        return self.load_error is not True

    def is_error(self):
        return not self.is_success()

    def error(self):
        return self.error_message

    def set_load_error(self, message):
        self.load_error = True
        self.error_message = message


class SongStatus:
    def __init__(self, data):
        self.data = data or {}

    def is_stopped(self):
        return not self.data

    def is_playing(self):
        return not self.is_stopped() and self.data['playing'] is True

    def is_paused(self):
        return not self.is_stopped() and not self.is_playing()

    def artist(self):
        return None if (not self.is_playing()) else self.song()['artist']

    def title(self):
        return None if (not self.is_playing()) else self.song()['title']

    def song(self):
        return self.data.get('song', {})


class DisplayStatus:
    def __init__(self, path, messages):
        self._messages = messages
        self._path = path
        self._song_status = None
        self._parser = None
        self.load()

    def artist(self):
        return self._song_status.artist() or self._messages.not_available()

    def title(self):
        return self._song_status.title() or self._messages.not_available()

    def error_message(self):
        return self._parser.error()

    def song_status(self):
        if self._parser.is_error():
            return Messages.PLAYER_ERROR
        elif self._song_status.is_stopped():
            return self._messages.stopped()
        elif self._song_status.is_paused():
            return self._messages.paused()
        else:
            return self._messages.status_format().format(
                artist=self._song_status.artist(),
                title=self._song_status.title()
            )

    def load(self):
        self.load_parser()
        self.load_song_status()

        return self

    def load_parser(self):
        self._parser = JsonDataParser(self._path)
        self._parser.load()

    def load_song_status(self):
        self._song_status = SongStatus(self._parser.data)


class Settings:
    DEFAULTS = {
        "debug": False,
        "not_available_message": "N/A",
        "paused_message": "Player paused.",
        "stopped_message": "Player stopped.",
        "status_format": "{artist} - {title}",
        "offline_message": "We offline :(",
        "data_path": "%APPDATA%\Google Play Music Desktop Player\json_store\playback.json"
    }

    def __init__(self):
        self._settings = self.__class__.DEFAULTS
        self._loaded = False
        return

    def load(self, json_data):
        tmp = self.__class__.DEFAULTS.copy()
        tmp.update(json.loads(json_data))

        self._settings = tmp
        self._loaded = True

        return self

    def load_from_file(self, path):
        with codecs.open(path, encoding='utf-8-sig', mode='r') as f:
            self.load(f.read())

        return self

    def data_path(self):
        return os.path.expandvars(self._settings["data_path"])

    def is_debug(self):
        return self._settings["debug"]

    def not_available_message(self):
        return self._settings["not_available_message"]

    def paused_message(self):
        return self._settings["paused_message"]

    def stopped_message(self):
        return self._settings["stopped_message"]

    def status_format(self):
        return self._settings["status_format"]

    def offline_message(self):
        return self._settings["offline_message"]


RuntimeSettings = Settings()


def load_settings(json_data):
    RuntimeSettings.load(json_data)


def Init():
    config_file = "settings.json"
    path = os.path.dirname(__file__)
    try:
        RuntimeSettings.load_from_file(os.path.join(path, config_file))
    except:
        Parent.Log(ScriptName, "Failed to load settings from %s", config_file)


def ReloadSettings(jsonData):
    RuntimeSettings.load(jsonData)


def Parse(ParseString, user, target, message):
    messages = Messages(RuntimeSettings)

    if m_SongStatusVar not in ParseString:
        return ParseString

    if Parent.IsLive() or RuntimeSettings.is_debug():
        status = DisplayStatus(RuntimeSettings.data_path(), messages)
        if status.error_message():
            Parent.Log(ScriptName, status.error_message())

        return ParseString \
            .replace(m_SongStatusVar, status.song_status())
    else:
        Parent.Log(ScriptName, "Stream is not live")
        return ParseString.replace(m_SongStatusVar, messages.offline())
