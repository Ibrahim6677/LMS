from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Book(models.Model):

    status_books = [
        ('Available', 'Available'),
        ('Rented', 'Rented'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rental_peroiod = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=status_books, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.title 

    def __unicode__(self):
        return 
