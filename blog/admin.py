from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)       # Чтобы наша модель стала доступна на странице администрирования, нам нужно зарегистрировать
admin.site.register(Comment)