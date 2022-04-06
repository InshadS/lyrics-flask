from flask import Flask, render_template
import lyrics
app = Flask(__name__)

@app.route("/")
def hello():
    artists = lyrics.get_all_artist()
    return render_template("index.html", artists=artists)

@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    artists = lyrics.get_all_artist()
    songs= lyrics.get_all_songs(aid)
    singer= lyrics.singer(aid)
    return render_template("songlist.html",artists=artists,songs=songs,singer=singer,currentartist=aid)

@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyric(sid,aid):
    lyric= lyrics.get_lyrics(sid)
    artists = lyrics.get_all_artist()
    songs= lyrics.get_all_songs(aid)
    singer= lyrics.singer(aid)
    return render_template("lyrics.html",lyrics=lyric,artists=artists,songs=songs,singer=singer,currentsong=sid,currentartist=aid)

if __name__=="__main__":
    app.run(debug=True)