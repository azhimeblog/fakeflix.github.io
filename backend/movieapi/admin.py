from django.contrib import admin
from django import forms

from . import models


class MovieAdminForm(forms.ModelForm):

    class Meta:
        model = models.Movie
        fields = "__all__"


class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    list_display = [
        "name",
        "detail",
        "watch_time",
        "sound",
        "category",
        "trailer",
        "year",
        "picture",
        "movievideo",
    ]
    


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "cat_name",
        "slug",
    ]
    readonly_fields = [
        "cat_name",
        "slug",
    ]


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Category, CategoryAdmin)
