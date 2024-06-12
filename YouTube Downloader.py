from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
save_location = "./"

yt = YouTube(video_url)
stream = yt.streams.filter(res="720p", progressive=True).first()
stream.download(output_path=save_location)