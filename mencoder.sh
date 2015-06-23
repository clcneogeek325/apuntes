#esto es para convetir videos mkv a .avi
mencoder Video.mkv -vf scale=720:304 -oac mp3lame -lameopts preset=128 -ovc xvid -xvidencopts bitrate=700 -ofps 25 -of avi -vobsubid 0 -o Video.avi


# -vobsubid    es el numero del subtitulo
# scale es     scale=720:304 es la resolucion
