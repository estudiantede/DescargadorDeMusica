import os
import time

path = r"C:\Users\Avaya\Proyectos\DescargarVideos\Videos"

#Thsi delates every video that is on the paht's folder
def delateVideo(videoPath):
    videos = os.listdir(videoPath)
    for i in videos:
        if ".mp4" in i:
            os.unlink(videoPath + "\\" + i)
delateVideo(path)