# Current song script for Youtube Music Desktop and StreamlabsBot 

<img width="490" alt="working" src="https://user-images.githubusercontent.com/127317/38418345-ae67f8d8-39a4-11e8-84e8-742f61e23466.png">


This is a small script that provides current song info from [Youtube Music Desktop Player](https://ytmdesktop.app/)
and makes it available in [StreamlabsBot](https://streamlabs.com/chatbot).

## Installation

Get the latest stable release from the [Releases Page](https://github.com/nvloff/song_status/releases). (Note: use the named `.zip`, while the source `.zip` will also work, it contains code for testing)

Then go to the `Scripts` tab in the Streamlabs bot and `Import` the `.zip` file
## Usage

Use the `$song_status` variable in any command to display the song status.

<img width="446" alt="config" src="https://user-images.githubusercontent.com/127317/38418325-9b9855c2-39a4-11e8-8a66-86635286f668.png">


## Settings

 * status format - display format of the song status(ex. `{artist} - {title}`)
 * Message to display when stream is offline.
 * Debug flag to allow song display, even when the stream is offline
 * Specify the location of player's JSON interface(defaults to windows - `%APPDATA%\youtube-music-desktop-app\logs\main.log`)
 
 
 ## License
 
 Code is distributed under the [MIT license](https://github.com/nvloff/song_status/blob/master/LICENSE)
 
 
 ## Changes
 
 ### v1.0.0.0
   Initial release
 
