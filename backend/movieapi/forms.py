from django import forms
from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = [
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


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "cat_name",
            "slug",
        ]
