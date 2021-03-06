from django.db import models

class CommonInfo(models.Model):
    title = models.CharField(max_length=140, default="Без заголовка")
    counter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Page(CommonInfo):
    pass

class MediaInfo(CommonInfo):
    page = models.ForeignKey(Page, related_name="%(app_label)s_%(class)s", blank=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Video(MediaInfo):
    video_url = models.URLField()
    subs_url  = models.URLField()

class Audio(MediaInfo):
    # page = models.ForeignKey(Page, related_name="audios", blank=True, on_delete=models.CASCADE)
    bitrate = models.IntegerField()

class Text(MediaInfo):
    # page = models.ForeignKey(Page, related_name="texts", blank=True, on_delete=models.CASCADE)
    content = models.TextField()
