from django.db import models
from tinymce.models import HTMLField
from chapters.models import Chapter

class Post(models.Model):
    title = models.CharField(max_length=200)
    link_chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = HTMLField() 
    