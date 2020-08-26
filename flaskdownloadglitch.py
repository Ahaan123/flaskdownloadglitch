from flask import Flask
from youtube_search import YoutubeSearch
from flask import request
from pytube import YouTube
from flask import send_file
import os
app = Flask(__name__)
@app.route('/download', methods=['GET', 'POST'])
def download():
    song = request.args.get('song')
    song_new = song + ' lyrics'
    results = YoutubeSearch(song_new, max_results=1).to_dict()
    vid = results[0]
    vid_url = 'https://www.youtube.com/' + vid['url_suffix']
    video = YouTube(url=vid_url)
    stream = video.streams.filter(only_audio=True).first()
    file = stream.download()
    os.remove(file)
    return send_file(file)

if __name__ == '__main__':
    app.run()

