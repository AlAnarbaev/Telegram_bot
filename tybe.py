from pytube import YouTube

url = input('Введите ссылку')
yt = YouTube(url)
print('Начинаем скачивание, ожидайте')
yt.streams.filter(progressive=True, file_extension='.mp4').order_by('resolution').desc().first().download()

