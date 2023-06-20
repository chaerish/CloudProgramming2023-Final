from django.contrib import admin

from diary.models import Post, Profile, Calendar

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Calendar)