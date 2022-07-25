from project_musicbox import *

print("""***********************************
SUMER SPOTIFY

1.Show Playlist
2.Show Detailed Playlist
3.Search Musics By Song
4.Search Musics By Singer
5.Add Music
6.Delete Music
7.Update Album
8.Sort By Song
9.Sort By Singer
10.Playlist Time
Q:Exit

***********************************""")

spotify = Music_Box()
while True:
    c = input("Operation: ")
    if c == 'Q':
        print("Goodbye")
        spotify.unconnect()
        break
    else:
        c = int(c)
        if c == 1:
            spotify.show_musics()
        elif c == 2:
            spotify.show_musics_detail()
        elif c == 3:
            song = input("Song: ")
            spotify.search_musics_by_song(song)
        elif c == 4:
            singer = input("Singer: ")
            spotify.search_musics_by_singer(singer)
        elif c == 5:
            song = input("Song: ")
            singer = input("Singer: ")
            album = input("Album: ")
            producer = input("Producer: ")
            time = input("Time: ")
            music = Music(song,singer,album,producer,time)
            spotify.add_music(music)
        elif c == 6:
            song = input("Song: ")
            spotify.delete_music(song)
        elif c == 7:
            song = input("Song: ")
            n_album = input("New Album: ")
            spotify.update(n_album,song)
        elif c == 8:
            spotify.sort_by_song()
        elif c == 9:
            spotify.sort_by_singer()
        elif c == 10:
            spotify.playlist_time()
        else:
            print("Coming Soon...")
