# Wallpaper Roulette
This is a small project I wrote because I got tired of my wallpapers way too fast.  
This way I utilize the [Konachan] API to fetch random wallpapers and automatically apply them.

This was written with Windows 10 and Ubuntu 20.04 in mind.  
So this might not run on your OS or OS version.

## Requirements
- Python 3.5 or higher ([download](https://www.python.org/downloads/))
- Python packages: [Requests](https://pypi.org/project/requests/)
- Active internet connection

## Installation
To install the required packages you can simply run:
```bash
python -m pip install -r requirements.txt
```
*The [requirements.txt](../master/requirements.txt) file has all the required dependencies predefined*

## Location
The download folder and the config file are stored in a folder inside your user directory.

**Windows**: `%USERPROFILE%/Wallpaper Roulette`  
**Ubuntu**: `~/Wallpaper Roulette`

## Configuration
This script automatically creates a `config.json` file with configurations that can be changed.

```js
{
    "searchTags": String[],
    "width": String,
    "height": String,
    "rating": String,
    "removeOld": Boolean
}
```
*Above you see the config file with the corresponding types*

### searchTags
`searchTags` is a string array, that means it only takes an array of strings.  
This script will pick a random item from the array each time it runs.

Tags can be found on this page [tags].

### width / height
`width` and `height` are the dimensions you wish to search for.  
This script will search on the **exact** dimensions you enter.  
Defaults: `"width": "1920", "height": "1080"`

### rating
The `rating` is a string with the rating of the images.  
To find more information on the ratings visit [ratings]

As of this moment the ratings are as follows:

- `"safe"` - Safe
- `"questionable"` - Questionable (ecchi)
- `"explicit"` - Explicit (hentai)
- `"questionableless"` - Safe & Questionable
- `"questionableplus"` - Questionable & Explicit

### removeOld
By default this script removes all the downloaded wallpapers when a new one is set.  
If you would like this script to preserve the downloads, set this to `false`.

[Konachan]: https://konachan.net/
[tags]: https://konachan.net/tag?name=&type=&order=count
[ratings]: https://konachan.net/help/ratings