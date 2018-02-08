from django.db import models

from album.models import Album
from artist.models import Artist
import datetime


class Song(models.Model):
    artist = models.ManyToManyField(Artist, through='ArtistSong', related_name='song_list')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    lyrics = models.TextField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    composer = models.CharField('작곡', max_length=50, blank=True)
    lyricist = models.CharField('작사', max_length=50, blank=True)
    arranger = models.CharField('편곡', max_length=50, blank=True)

    @property
    def artist(self):
        return self.album.artist.all()

    @property
    def release_date(self):
        return self.album.release_date

    @property
    def formatted_release_date(self):
        return self.release_date.strftime('%Y.%m.%d')

    def __str__(self):
        return '{artist} - {title} ({album})'.format(
            artist=', '.join(self.album.artist.values_list('name', flat=True)),
            title=self.title,
            album=self.album.album_name,
        )


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.artist} | {self.song.title}'
