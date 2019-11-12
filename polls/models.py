from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True)
    draft = models.BooleanField(default=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created", "-updated"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "[%s] %s" % (self.author, self.text)


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class UploadImageTest(models.Model):
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

