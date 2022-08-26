import re, os, time, urllib.request, urllib.error, pytube

video_file = "video_list.txt"
path = "Video"
url = "https://www.youtube.com/playlist?list=myplaylist"

if not os.path.exists(path):
    os.mkdir(path)

def get_playlist(url):
    amp = 0
    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]   
    else:
        print('Incorrect Playlist.')
        exit(1)
    try:
        sTUBE = str(urllib.request.urlopen(url).read())
    except urllib.error.URLError as e:
        print(e.reason)
    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    if mat := re.findall(tmp_mat, sTUBE):
        final_url = []
        for PL in mat:
            yPL = str(PL)
            if '&' in yPL:
                yPL_amp = yPL.index('&')
            final_url.append(f'http://www.youtube.com/{yPL[:yPL_amp]}')
        all_url = list(set(final_url))
        i = 0
        with open(video_file, "w", encoding="utf-8") as file:
            while i < len(all_url):
                file.write(all_url[i].strip() + '\n')
                time.sleep(0.04)
                i += 1
    else:
        print('No videos found.')
        exit(1)

if 'http' not in url:
    url = f'http://{url}'
get_playlist(url)

with open(video_file) as file:
    for line in file:
        pytube.YouTube(line).streams.filter(subtype="mp4").filter(progressive=True).first().download(path)
