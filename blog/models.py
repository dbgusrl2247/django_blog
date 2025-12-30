from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # 여기!
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
