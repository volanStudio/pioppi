# GIFc

## A (hard G) GIF creation workflow for going from video to GIF

GIFc requires the following packages:

```
brew install ffmpeg
brew install gifsicle
```

## Running GIFc

GIFc takes a video file as an input and creates a directory with frame by frame source pngs and gifs and a compiled final gif at 8 fps that pauses on the last frame for 10 seconds.

```
python GIFc.py {videoFile}
```
results in
```
_assets/
  pngs/
  gifs/
_final/
  {videoFile}
```
