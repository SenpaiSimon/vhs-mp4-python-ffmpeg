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
pip install -r requirements.txt
```

## Folder Structure

![dirStruct](https://github.com/SenpaiSimon/vhs-mp4-python-ffmpeg/blob/main/img/dir.png)

1. The `log.txt` and `/done` will be created automatically
2. Put your files or even files sctructure into the `input`-directory
3. This script will keep the file structure provided in the `input`-directory!

## Working with the script

> Name all your files with the name you want to keep! This script will embed the file Name (without the file extension like `.mpg`) into the metadata of the file!

1. Execute it using `python convert.py`
2. You have to keep this terminal open until the script is done!
3. You can monitor the conversion of the currrent file in the terminal window
4. If you want to see the whole progress, you can look into the generated `log.txt`
5. This will also display some extra logging, like times and storage savings
6. If a file is complete, it will move the file with the extension of `targetFileType` into the `done`-directory

## Result
At the End you will have all your converted files in the the `input`-directory with your original file structure. All the original files were be moved into the `done`-directory.

## Addition
If you want to compress and convert your files properly then set `extendedMode` in `line 27` to `True`
See code comments for further information
