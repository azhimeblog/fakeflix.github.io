from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):

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

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "cat_name",
            "slug",
        ]
