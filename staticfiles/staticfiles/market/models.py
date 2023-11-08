from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
class Category(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        ordering=['-name']
        verbose_name_plural='Categories'
        verbose_name='Category'

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE , related_name='categories')
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique_for_date='publish')
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/%Y/%m/%d')
    is_sold=models.BooleanField(default=False)
    publish=models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish',]),
            models.Index(fields=['seller',]),
            models.Index(fields=['name',])

        ]
    def __str__(self):
        return f'{self.name}'
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('market:detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,

        ])