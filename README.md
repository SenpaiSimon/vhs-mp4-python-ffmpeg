# vhs-mp4-python-ffmpeg

## Important for Windows

Install FFMPEG to your local enviroment following this guide
https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/

verify by typing
```bash
ffmpeg -version
```

## Python

Install the librarys using pip install

```bash
pip install ffmpeg-python
```

## Setting up file structure

1. Create a folder in the same hirarchy level like the folder with all your movies
2. Move the script into the newly created folder
3. Change `searchDir` to `../yourFolder`, where `yourFolder` is the folder where all your movies are
4. If you convert from vhs grabber files then the `targetFileType = '.mpg'` is already correct

## Working with the script

1. Execute it using `python convert.py`
2. You have to keep this terminal open until the script is done!
3. You can monitor the conversion of the currrent file in the terminal window
4. If you want to see the whole progress, you can look into the generated `log.txt`
5. This will also display some extra logging, like times and storage savings
6. If a file is complete, it will move the file with the extension of `targetFileType` into a folder in the script directory

## Addition
If you want to compress and convert your files properly then set `extendedMode` in `line 27` to `True`
See code comments for further information
