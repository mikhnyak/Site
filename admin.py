from django.contrib import admin
from .models import PublicPlaylist
from .models import PrivatePlaylist
from .models import User
from .models import Song


admin.site.register(PublicPlaylist)
admin.site.register(PrivatePlaylist)
admin.site.register(User)
admin.site.register(Song)