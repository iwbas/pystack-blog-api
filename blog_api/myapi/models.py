from django.db import models

class CommonInfo(models.Model):
    title = models.CharField(max_length=140)
    counter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Page(CommonInfo):
    pass

class Video(CommonInfo):
    video_url = models.URLField()
    subs_url  = models.URLField()

class Audio(CommonInfo):
    bitrate = models.IntegerField()

class Text(CommonInfo):
    content = models.TextField()
