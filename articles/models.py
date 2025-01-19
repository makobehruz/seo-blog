from django.db import models
from .base_model import BaseModel


class Author(BaseModel):
    full_name = models.CharField(max_length=50)
    biography = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

class Article(BaseModel):
    title = models.CharField(max_length=50)
    article_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'articles')
    image = models.ImageField(upload_to='article_image/')

    def __str__(self):
        return self.title

class Comment(BaseModel):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.full_name