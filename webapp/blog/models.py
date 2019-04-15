from django.db import models


class InstaPost(models.Model):
    link_id = models.CharField(unique=True, max_length=200)
    img = models.CharField(max_length=200)
    description = models.TextField()

    def get_url(self):
        return f'www.instagram.com/jakobowsky/p/{self.link_id}'

    def __str__(self):
        return self.description[:30]
