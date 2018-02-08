from django.db import models

from artist.models import Artist


class Album(models.Model):
    artist = models.ManyToManyField(Artist, related_name='album_list')
    album_name = models.CharField('앨범명', max_length=50)
    release_date = models.DateField('발매일', null=False, blank=False)
    genre = models.CharField('장르', max_length=50, blank=True)
    album_intro = models.TextField('소개', blank=True)
    img_cover = models.ImageField(
        '커버 이미지',
        upload_to='album',
        blank=True,
    )

    # @property
    # def genre(self):
    #     return ''
    #
    def __str__(self):
        artist = ', '.join(self.artist.values_list('name', flat=True))
        return '{title} [{artist}]'.format(
            title = self.album_name,
            artist = artist,
        )
