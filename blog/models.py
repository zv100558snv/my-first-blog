from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name = "автор")
    title = models.CharField(max_length=200, verbose_name = "Заголовок")
    text = models.TextField(verbose_name = "Полное содержание")
    created_date = models.DateTimeField(default=timezone.now, verbose_name = "Дата создания")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name = "Дата публикации")

    def publish(self):                                            # метод публикации
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"
