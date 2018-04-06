# Current song script for Google Play Music Desktop and StreamlabsBot 

This is a small script that provides current song info from [Google Play Music Desktop Player](https://www.googleplaymusicdesktopplayer.com/)
and makes it available in [StreamlabsBot](https://streamlabs.com/chatbot).

The script uses the player's [JSON Interface](https://github.com/MarshallOfSound/Google-Play-Music-Desktop-Player-UNOFFICIAL-/blob/master/docs/PlaybackAPI.md)
to read a file containing the playback data.

## Installation

Get the latest stable release from the [Releases Page](https://github.com/nvloff/song_status/releases).

Then go to the `Scripts` tab in the Streamlabs bot and `Import` the `.zip` file
## Usage

Use the `$song_status` variable in any command to display the song status.


## Settings

 * status format - display format of the song status(ex. `{artist} - {title}`)
 * Message to display when stream is offline.
 * Message to display when player is stopped.
 * Message to display when song in paused.
 * Debug flag to allow song display, even when the stream is offline
 
 
 ## License
 
 Code is distributed under the [MIT license](https://github.com/nvloff/song_status/blob/master/LICENSE)
 
 
 ## Changes
 
 ### v1.0.0.0
   Initial release
 
