from django.db import models
from django.shortcuts import reverse



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('books_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('id', 'slug'),)
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id, self.slug])
    
    def __str__(self):
        return "%d-%s" % (self.id, self.title)


