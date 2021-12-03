from pytube import YouTube
from datetime import datetime
from tqdm import tqdm

with open('source.txt') as src, open('logs.txt', 'a') as logs:
    num_lines = sum(1 for line in src)
    src.seek(0)
    for _ in tqdm(range(num_lines)):
        data = src.readline().strip()
        yt = YouTube(data)
        videos = yt.streams.filter(type='video')
        try:
            dn_video = videos.get_highest_resolution()
            logs.write(f'''{datetime.now()}\nDownloading {data}\n''')
            dn_video.download(output_path='output')
            logs.write("Completed.\n\n")
        except IndexError:
            logs.write(f'''-------------------------WARNING-------------------------\n{datetime.now()}\n\
{data}\nFailed.\n---------------------------------------------------------\n\n''')
