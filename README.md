
# SimpleTexTool-GUI

A simple texture converter with a GUI for SC games. Based on PVRTexTool.




## First Installation

Before anything, be sure you have [Python 3.10](https://www.python.org/downloads/release/python-31011/) installed.

For the first intall, run the following command in the root folder :

```python
  python setup.py
```

Wait until the script finish and you'll be good to go !
## How to use ?

Just double click on the main.py file or run the following command :

```python
  python main.py
```

You should see this interface popping up :

![Main Menu](https://github.com/ARHCOS/SimpleTexTool-GUI/tree/main/ressources/main_menu.png?raw=true)

In order to convert a file, just simply drag and drop it in the "drop area", select a conversion method and click convert !

Your converted file should appear in the folder it originated from.
## Limitations

 - Only supports ktx2png, png2ktx and pvr2png
 - Does NOT support multi file drop


## Known Issues

- Sometime during the setup process the script can give you a permission error even though there is no problem. If you encounter this, just check if you have PVRTexToolCLI.exe in the scripts folder and if you have just ignore the error
