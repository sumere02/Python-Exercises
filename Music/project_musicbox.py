import sqlite3

class Music():
    def __init__(self,song,singer,album,producer,time):
        self.song = song
        self.singer = singer
        self.album = album
        self.producer = producer
        self.time = time
    def __str__(self):
        return "Song: {}\nSinger: {}\nAlbum: {}\nProducer: {}\nTime: {}\n".format(self.song,self.singer,self.album,self.producer,self.time)
    def __len__(self):
        print(self.time)
class Music_Box():
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()     
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Playlist (Song TEXT,Singer TEXT,Album TEXT,Producer TEXT,Time FLOAT)")
        self.connection.commit()
    def unconnect(self):
        self.connection.close()
    def show_musics_detail(self):
        self.cursor.execute("SELECT * FROM Playlist")
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                print(music)
    def show_musics(self):
        self.cursor.execute("SELECT Song,Singer,Time FROM Playlist")
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            for i in musics:
                print("Song: {}\nSinger: {}\nTime: {}\n".format(i[0],i[1],i[2]))
    def search_musics_by_song(self,song):
        self.cursor.execute("SELECT * FROM Playlist WHERE Song = ?",(song,))
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                print(music)
    def search_musics_by_singer(self,singer):
        self.cursor.execute("SELECT * FROM Playlist WHERE Singer = ?",(singer,))
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                print(music)
    def add_music(self,music):
        self.cursor.execute("INSERT INTO Playlist VALUES (?,?,?,?,?)",(music.song,music.singer,music.album,music.producer,music.time))
        self.connection.commit()
    def delete_music(self,song):
        self.cursor.execute("SELECT * FROM Playlist where Song= ?",(song,))
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Song already not exist in playlist")
        else:
            self.cursor.execute("DELETE FROM Playlist WHERE Song = ?",(song,))
            self.connection.commit()
    def update(self,album,song):
        self.cursor.execute("SELECT * FROM Playlist where Song = ?",(song,))
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Song does not exists in playlist")
        else:
            self.cursor.execute("UPDATE Playlist set album = ? where Song = ?",(album,song))
            self.connection.commit()
    def sort_by_song(self):
        self.cursor.execute("SELECT * FROM Playlist")
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            musics.sort()
            self.cursor.execute("DELETE FROM Playlist")
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                self.cursor.execute("INSERT INTO Playlist VALUES (?,?,?,?,?)",(music.song,music.singer,music.album,music.producer,music.time))
            self.connection.commit()
    def sort_by_singer(self):
        self.cursor.execute("SELECT * FROM Playlist")
        musics = self.cursor.fetchall()
        if len(musics) == 0:
            print("Playlist is empty")
        else:
            musics.sort(key = lambda music:music[1])
            self.cursor.execute("DELETE FROM Playlist")
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                self.cursor.execute("INSERT INTO Playlist VALUES (?,?,?,?,?)",(music.song,music.singer,music.album,music.producer,music.time))
            self.connection.commit()
    def playlist_time(self):
        self.cursor.execute("SELECT * FROM Playlist")
        musics = self.cursor.fetchall()
        total = 0
        for i in musics:
            total += i[4]
        print("Total Time: {}".format(total))