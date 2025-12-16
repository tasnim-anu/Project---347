from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    review_text = models.TextField()
    STAR_CHOICES = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    star_rating = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.product_name} ({self.star_rating}⭐)"




class Product(models.Model):
    CATEGORY_CHOICES = [
        ('resin', 'Resin Art'),
        ('custom', 'Customised Work'),
        ('chocolate', 'Chololate Box'),
        ('ScrapBook', 'Scrapbook'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    short_description = models.TextField(max_length=300, blank=True)

    is_featured = models.BooleanField(default=False)  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name







