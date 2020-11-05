from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title = models.CharField(max_length=120)
    message = models.CharField(max_length=250)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, related_name='snippets')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s" % (self.created_by, self.title)
