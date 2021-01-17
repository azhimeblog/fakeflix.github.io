from django.db import models
from django.urls import reverse


class Movie(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    picture = models.FileField()
    detail = models.TextField(max_length=10000)
    watch_time = models.CharField(max_length=1000)
    sound = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    trailer = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    movievideo = models.CharField(max_length=1000)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("movieapi_Movie_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("movieapi_Movie_update", args=(self.pk,))


class Category(models.Model):

    # Fields
    cat_name = models.CharField(max_length=1000)
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("movieapi_Category_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("movieapi_Category_update", args=(self.slug,))
