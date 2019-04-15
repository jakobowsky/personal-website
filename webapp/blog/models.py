from django.db import models


class InstaPost(models.Model):
    link_id = models.CharField(unique=True, max_length=200)
    img = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.description[:30]
