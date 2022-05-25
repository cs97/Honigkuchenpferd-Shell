# Honigkuchenpferd-Shell

Simple Reverse and Bind Shell 



macOS:
```
screencapture -x /tmp/screenshot.jpg
```
gnu/linux:
```
#screenshot
ffmpeg -f x11grab -framerate 1 -i :0.0 -vframes 1 screenshot.jpg
```
```
#Selfie
ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:1 -frames 1 /tmp/selfie.jpg
```


