from django.urls import reverse
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='article_image/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'articles:detail',
            kwargs={
                'pk': self.pk,
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug
            }
        )


class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    comment = models.TextField()
    your_email = models.EmailField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.first_name




