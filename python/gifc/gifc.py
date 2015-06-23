import os
import sys
import subprocess

# Need to install ffmpeg and gifsicle to run gifc.

def createPngs():
  cmd = 'ffmpeg -i '+ name +' -r 8 '+ directories[0] +'/'+ title +'%04d.png'
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print '2. created pngs '+ directories[0]
  convertToGifs()

def convertToGifs():
  cmd = 'sips -s format gif '+ directories[0] +'/* --out '+ directories[1]
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print '3. converted pngs '+ directories[0] +' to gifs '+ directories[1]
  finalizeGif()

def finalizeGif():
  cmd = 'gifsicle --optimize=3 --colors 256 --loopcount '+ directories[1] +'/* >'+ directories[2] +'/'+ title +'.gif -d1000 "#-1"'
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print '4. merged gifs in '+ directories[1] +' into "'+ directories[2] +'/'+ title +'"'

# Define input file name and a folder for the specific assets
name = sys.argv[1];
title = os.path.splitext(name)[0]

# Create driectories to stick the assets
directories = [ '_assets/'+ title +'/pngs', '_assets/'+ title +'/gifs', '_final']

print '1. evaluating file structure'
for directory in directories:
  if not os.path.exists(directory):
    os.makedirs(directory)
    print '   -  '+ directory + ' was created'
  else:
    print '   -  '+ directory + ' already exists'

ex = createPngs()
