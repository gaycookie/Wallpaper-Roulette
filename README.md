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

## Configuration
This script automatically creates a `config.json` file with configurations that can be changed.

```js
{
    "searchTags": String[],
    "width": String,
    "height": String,
    "rating": String,
    "downloadFolder": String,
    "removeOld": Boolean
}
```
*Above you see the config file with the corresponding types*

[Konachan]: https://konachan.net/