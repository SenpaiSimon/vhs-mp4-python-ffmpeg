import os
import ffmpeg
import shutil
import time
import datetime
from contextlib import redirect_stdout

##############################################################################################
# Settings - the extended settings can be untouched 
# - only modify pahts and file extensions if you dont know what you are doing
##############################################################################################

# Search Directory relative to this script -- use "/" not "\"
# This will search recursivly in all dirs following "seachDir"
searchDir = '../Digitalisierung-VHS' 
targetFileType = '.mpg'
desiredFileType = '.mp4'

# Codec Stuff for base mode
videoCodec = 'copy'
audioCodec = 'aac'
presetNormal = 'veryslow'

# Additional Filters, set "extendedMode" to "True" for these to take affect
# This might take a loooooong time - if executed on a slow system (like a Raspberry PI)
# Takes about 3-4 times as long as the video itself (tested on raspberry pi 3B)
extendedMode = True
pixelFormat = 'yuv420p'
movieflags='faststart'
presetExtended = 'medium'



##############################################################################################
# Programm
##############################################################################################

# Setting up folder structure
if os.path.exists("log.txt"):
    os.remove("log.txt")
with open("log.txt", 'w'):
    pass
if not os.path.exists("/done"):
    os.makedirs("/done")

# setup timer and vars
totalStartTime = time.time() 
totalOriginalSize = 0
totalNewSize = 0

# start log with time
with open('log.txt', 'a') as stream:
    with redirect_stdout(stream):
        print("Script written by: SenpaiSimon\n\n")
        start = datetime.datetime.now()
        print("Start time and date: %s:%s:%s - %s.%s.%s\n\n" % (start.hour, start.minute, start.second, start.day, start.month, start.year))
        
# Gather Files    
inputFiles = []
for root, dirs, files in os.walk(searchDir):
    for file in files:
        if file.endswith(targetFileType):
            inputFiles.append(os.path.join(root, file))

# list the files in log
with open('log.txt', 'a') as stream:
    with redirect_stdout(stream):
        print("Found: %s files to convert!\n" % len(inputFiles))
        for inputFile in inputFiles:
            print(os.path.basename(inputFile))
        print("\n")

# Convert steps for each file
for inputFile in inputFiles:
    # start timer and output
    fileTimeStart = time.time()
    inputFile = "../" + inputFile[3:]
    
    output = inputFile.removesuffix(targetFileType) + desiredFileType

    # conversion start log
    with open('log.txt', 'a') as stream:
        with redirect_stdout(stream):
            print(">-----------------------------------------------------<")
            print("Input:   " + inputFile)
            print("Output:  " + output)
            print("\nConverting...")
           
    movieTitle = os.path.basename(inputFile).removesuffix(targetFileType); 
    
    # conversion modes  
    if extendedMode:
        # extended mode
        inStream = ffmpeg.input(inputFile)
        audioStream = inStream.audio
        
        inStream.filter('yadif', mode=0, parity=0).filter('hqdn3d', 3).output(audioStream, output, crf=23, acodec=audioCodec, preset=presetExtended, pix_fmt=pixelFormat, movflags=movieflags, metadata='title=' + movieTitle).run()
    else:
        # base mode
        ffmpeg.input(inputFile).output(output, crf=23, vcodec=videoCodec, acodec=audioCodec, preset=presetNormal, metadata='title=' + movieTitle).run()
           
    # end log 
    with open('log.txt', 'a') as stream:
        with redirect_stdout(stream):
            print("DONE\n")
            
            # size log
            originalSize = os.path.getsize(inputFile) / (1024*1024)
            newSize = os.path.getsize(output) / (1024*1024)
            totalOriginalSize += originalSize
            totalNewSize += newSize
            print("Original Size: %s MB" % originalSize)
            print("New File Size: %s MB" % newSize)
            print("Saved: %s MB with compression rate of %s%s\n" % ((originalSize - newSize), ((originalSize - newSize) / originalSize) * 100, "%"))
            
            # time log
            print("Conversion took --- %s seconds ---" % (time.time() - fileTimeStart))
            print("Total time elapsed so far --- %s seconds ---\n" % (time.time() - totalStartTime))
            
            # move log
            shutil.move(inputFile, "done/" + os.path.basename(inputFile))
            print("Moved: \"" + movieTitle +"\" to /done")
            print(">-----------------------------------------------------<")
            print("\n\n\n")
  
# Show end stats          
with open('log.txt', 'a') as stream:
        with redirect_stdout(stream):
            start = datetime.datetime.now()
            print("End time and date: %s:%s:%s - %s.%s.%s" % (start.hour, start.minute, start.second, start.day, start.month, start.year))
            print("Conversion took --- %s seconds --- total\n" % (time.time() - totalStartTime))
            
            print("Total of: %s files!") % len(inputFiles)
            print("Total Original Size: %s MB" % totalOriginalSize)
            print("Total New File Size: %s MB" % totalNewSize)
            print("Saved: %s MB with compression rate of %s%s\n" % ((totalOriginalSize - totalNewSize), ((totalOriginalSize - totalNewSize) / totalOriginalSize) * 100, "%"))
            
