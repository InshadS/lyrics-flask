from flask import Flask, render_template, jsonify
import lyrics
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html",)

@app.route("/artists")
def get_artists():
    artists = lyrics.get_all_artist()
    artists_arr = [{'id':i[0], "name":i[1]} for i in artists]
    return jsonify(artists_arr)

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