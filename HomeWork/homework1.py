
import time
import webbrowser

def  openVideo():
    webbrowser.open("https://www.youtube.com/watch?v=TgqiSBxvdws")

def main():
    while True:
        time.sleep(30)
        openVideo()


main()