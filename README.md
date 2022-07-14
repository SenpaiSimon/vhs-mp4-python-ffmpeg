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
