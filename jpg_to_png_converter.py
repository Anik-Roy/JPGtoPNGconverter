import sys
import os
from PIL import Image

# grab the arguments passed from run command
jpgFolder = sys.argv[1]
pngFolder = sys.argv[2]

# check if folder exists or not
if not os.path.exists(pngFolder):
    os.mkdir(pngFolder)

for filename in os.listdir(jpgFolder):
    img = Image.open(f'{jpgFolder}{filename}')
    cleanName = os.path.splitext(filename)[0]
    img.save(f'{pngFolder}{cleanName}.png', 'png')
    print('all done')