from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from PIL import Image

from furnituresite.mixins import SlugAndNameMixin


class Category(SlugAndNameMixin, models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)


class Product(SlugAndNameMixin, models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        blank=True, null=True
    )

    class Meta:
        ordering = ('-created_at',)

    def get_display_price(self):
        return self.price / 100

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image and self.image.name:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        if not image or not image.name or not image.file:
            return None
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
