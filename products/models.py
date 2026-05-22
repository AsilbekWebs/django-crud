from django.db import models

# Create your models here.

class Book(models.Model):
    GENRE = (
        ('artistic', 'ARTISTIC'),
        ('comedy', "COMEDY"),
        ('historical','HISTORICAL'),
        ('adventure', 'ADVENTURE'),
        ('fantastic', 'FANTASTIC'),
    )
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, choices=GENRE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='books/', default='books/default_img.avif')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'books'

