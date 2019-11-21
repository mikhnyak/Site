from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class PublicPlaylist(models.Model):
    name = models.CharField("Playlist name", max_length=60)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField("Username", max_length=60)
    first_name = models.CharField("First name", max_length=60)
    last_name = models.CharField("Last name", max_length=60)
    email = models.CharField("E-mail", max_length=60)
    password = models.CharField("Password", max_length=60)
    phone = models.CharField("Phone number", max_length=60)
    public_playlists = models.ManyToManyField(PublicPlaylist)

    def __str__(self):
        return self.username

class PrivatePlaylist(models.Model):
    name = models.CharField("Playlist name", max_length=60)
    songs = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




























