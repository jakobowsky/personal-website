from django.db import models
from PIL import Image


class InstaPost(models.Model):
    link_id = models.CharField(unique=True, max_length=200)
    img = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.description[:30]


class GithubPost(models.Model):
    url = models.CharField(unique=True, max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='github')
    description = models.TextField()
    

    def __str__(self):
        return self.description[:30]
    
    def save(self, *args, **kwargs):
        super(GithubPost, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # if img.height > 400 or img.width > 400:
        #     output_size = (400, 400)
        #     img.thumbnail(output_size)
        img.save(self.image.path)