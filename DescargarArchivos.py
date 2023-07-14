from pytube import YouTube
import pytube
import moviepy.editor as mp
import os
import sys
path = r"C:\Users\Avaya\Proyectos\DescargarVideos"

if len(sys.argv) != 3:
    print("It's has to have 2 parameters url author")
    print(sys.argv[2])
    sys.exit()
#This function downloads the video which was passed
def Download(link):
    youtubeObject = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        if youtubeObject is not None:
            youtubeObject.download(path + "\\Videos")
    except:
        print("An error has ocurred")
    print("Download is completed successfully")
    title = youtubeObject.title
    del youtubeObject
    return title

#This change the extension from mp4 to mp3
def changeFormat(videoName):
    songPath = path + "\\Canciones\\" + sys.argv[2] + " - " + videoName
    videoName = path + "\\Videos\\" + videoName
    clip = mp.VideoFileClip(videoName + ".mp4")

    #Write this as audio and the extension is .mp3
    clip.audio.write_audiofile(songPath + ".mp3")
    return videoName + ".mp4"

#The first code to run
def main():
    name = sys.argv[1]
    name = Download(name)
    name = changeFormat(name)

main()
sys.exit()