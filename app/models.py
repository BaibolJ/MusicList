from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=123)
    description = models.TextField()
    music = models.FileField(upload_to='music/')

    def __str__(self):
        return self.name