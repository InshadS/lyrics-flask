from flask import Blueprint, jsonify
import lyrics

api = Blueprint('api',__name__)

@api.route("/artists")
def get_artists():
    artists = lyrics.get_all_artist()
    artists_arr = [{'id':i[0], "name":i[1]} for i in artists]
    return jsonify(artists_arr)

@api.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= lyrics.get_all_songs(aid)
    songs_arr = [{'id':i[1], "name":i[0]} for i in songs]
    print(songs_arr)
    return jsonify(songs_arr)


@api.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyric(sid,aid):
    lyric= lyrics.get_lyrics(sid)
    songs= lyrics.get_all_songs(aid)
    return jsonify(lyric)