from django.db import models

from album.models import Album
from artist.models import Artist


class Song(models.Model):
    artist = models.ManyToManyField(Artist, through='ArtistSong', related_name='song_list')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    lyrics = models.TextField(blank=True)
    composer = models.CharField('작곡', max_length=50)
    lyricist = models.CharField('작사', max_length=50)
    arranger = models.CharField('편곡', max_length=50)

    def __str__(self):
        return self.title


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.artist} | {self.song.title}'
