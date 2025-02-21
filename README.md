
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

## Features

- KTX to PNG
- PVR to PNG
- PNG to KTX
- SCTX to PNG
- PNG to SCTX

## About SCTX textures

SCTX is a new format created by SC and it is now implemented and almost all of their games. If you want more precisions about this format go read [SCTX conversion's README](https://github.com/Daniil-SV/SCTX-Converter/blob/main/README.md) but what you need to understand is that sctx2png gives out two files : 

- The actual texture in the form a PNG file
- A JSON file handling properties

If all you want is the texture, you can delete the JSON file but what you need to know is that the JSON file is **REQUIRED** if you want to convert the PNG texture back to SCTX.

To convert back the PNG texture to SCTX you need to select the "png2sctx" option, drag and drop either the PNG or JSON file and click convert. You obviously need to have both the PNG and JSON file in the same directory.

If the SCTX file is going to be used for a 3D model you **NEED** to enable the "Compress Data" option or your texture won't work.

## Limitations

 - Does NOT support multiple file drop
 - Based on [PVRTexToolCLI](https://developer.imaginationtech.com/solutions/pvrtextool/) and [SCXT-Converter](https://github.com/Daniil-SV/SCTX-Converter) so it only works on Windows


## Known Issues

- After the installation of PVRTexTool you might have an error that it's not in the PATH when converting. To resolve that just add the "scripts" folder to the system or user PATH
- Everytime you do any conversion with SCTX files you'll get a help screen that pop up in the console. Just ignore it

## Credits

 - As stated before, this project is mainly based on [PVRTexToolCLI](https://developer.imaginationtech.com/solutions/pvrtextool/) by [ImaginationTech](https://developer.imaginationtech.com/) for everything about KTX and PVR.

 - Big thanks to [Daniil SV](https://github.com/Daniil-SV) for the [SCTX conversion](https://github.com/Daniil-SV/SCTX-Converter) part and generally for helping me and giving feedback for this project
