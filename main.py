from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Download started")
        youtubeObject.download()
        print("Downloaded Successfully")
    except:
        print("Error Occured")


link = input("Enter the link: ")
Download(link)