# No Idle Bro
is an application which spins your cursor around and presses random keys on your keyboard to simulate activity on your pc.

## How to use
 - Input Duration
 - Unit of time for said duration
 - Press start
 > Note: You can stop script anytime by pressing SPACEBAR

## How to build

### Setting up The Dev Environment
1. Create and activate env using venv
    >```python -m venv /path/to/new/virtual/environment```
    
    >```source ./path/to/env```

2. Install dependecies using pip
    >```pip install -r requirements.txt```
### Building
- Use the app.spec file to create an exe using [Pyinstaller]('www.pyinstaller.org')
    >```pyinstaller app.spec app.py```

## Dependencies
- [keyboard]('https://pypi.org/project/keyboard/')
- [mouse]('https://pypi.org/project/mouse/')
- [pyinstaller]('www.pyinstaller.org')
- [tkinter]('https://wiki.python.org/moin/TkInter')
- [screeninfo]('https://pypi.org/project/screeninfo/')
