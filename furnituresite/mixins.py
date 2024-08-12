from django.utils.text import slugify
from django.db import models


class SlugAndNameMixin(models.Model):
    slug = models.SlugField(
        max_length=255,
        blank=True,
        unique=True,
        )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
