# Time Tracker: tracks the time you spent on websites
An application is written using Python, Flask, and JS.
<br>Works with Google Chrome browser.

## Getting Started
First of all, make sure you have **Google Chrome** installed.

### Installation
Clone the repo:
```
$ git clone git@github.com:UladzislauBaranau/time-tracker.git
```
Install `flask` and `flask-cors`. The commands below install the tools on your system: 
```
$ pip3 install -U Flask
$ pip3 install -U flask-cors
```
If you don't need flask on your system use a virtual environment, [more information](https://flask.palletsprojects.com/en/1.1.x/installation/).

### Google Chrome Extension
Description and detailed setup information are [here](https://github.com/weastur/chrome_extension).

## How to use it
To start tracking the time just launch the app:
```
$ python3 main.py
```
Current information about your actions is available both in the console and in the file `activities_info.json` created in the directory with the app. After stopping the app (press `ctrl+c`), information about your activities will be updated in the same file. You will get information like this: 
```
{
    "START_ACTIVITIES": "2021.04.13 15:00",
    "ACTIVITIES_INFORMATION": [
        {
            "active_tab": "https://github.com/",
            "last_active_session": {
                "hours": 0,
                "minutes": 0,
                "seconds": 58
            },
            "total_time": "0h 2min 40sec"
        },
        {
            "active_tab": "https://www.python.org/",
            "last_active_session": {
                "hours": 0,
                "minutes": 0,
                "seconds": 30
            },
            "total_time": "0h 1min 38sec"
        }
    ],
    "STOP_ACTIVITIES": "2021.04.13 15:04"
}
```
To get accurate information about the last action, open a new tab `chrome://newtab/` in the browser before stopping.

## License
[MIT license](https://github.com/UladzislauBaranau/time-tracker/blob/master/LICENSE).
