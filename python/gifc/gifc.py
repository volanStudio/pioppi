import os
import sys
import subprocess

# Need to install ffmpeg and gifsicle to run gifc.

def createPngs():
  cmd = "ffmpeg -i "+ sys.argv[1] +" -r 8 gif/pngs/out%04d.png"
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print output
  convertToGifs()

def convertToGifs():
  cmd = "sips -s format gif gif/pngs/* --out gif/gifs"
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print output
  finalizeGif()

def finalizeGif():
  cmd = "gifsicle --optimize=3 --colors 256 --loopcount gif/gifs/* > gif/anim.gif"
  p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = p.communicate()[0]
  print output

directories = [ "gif/", "gif/pngs", "gif/gifs"]

for dirs in directories:
  if not os.path.exists(dirs):
    os.makedirs(dirs)
  else:
    print "directories already exist"

fun = createPngs()
