
# SimpleTexToolGUI

A simple texture converter for SC Games with a GUI. Based on PVRTexTool.




## First Installation

Before anything, be sure you have [Python 3.10](https://www.python.org/downloads/release/python-31011/) installed.

For the first install, double click on setup.py or run the following command :

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

<p align="left">
<img src="./ressources/main_menu.png?raw=true"  width="60%">
</p>

In order to convert a file, just simply drag and drop it in the "drop area", select a conversion method and click convert.

Your converted file should appear in the folder it originated from.
## Limitations

 - Only supports ktx2png, png2ktx, pvr2png and sctx2png
 - Does NOT support multiple file drop
 - Based on [PVRTexToolCLI](https://developer.imaginationtech.com/solutions/pvrtextool/) and [SCXT-Converter](https://github.com/Daniil-SV/SCTX-Converter) so it only works on Windows


## Known Issues

- After the installation of PVRTexTool you might have an error that it's not in the PATH when converting. To resolve that just add the "scripts" folder to the system or user PATH

## Credits

 - As stated before, this project is mainly based on [PVRTexToolCLI](https://developer.imaginationtech.com/solutions/pvrtextool/) by [ImaginationTech](https://developer.imaginationtech.com/) for everything about KTX and PVR.

 - Big thanks to [Daniil SV](https://github.com/Daniil-SV) for the [SCTX conversion](https://github.com/Daniil-SV/SCTX-Converter) part and generally for helping me and giving feedback for this project
