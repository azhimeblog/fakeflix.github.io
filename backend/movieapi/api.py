from rest_framework import viewsets, permissions

from . import serializers
from . import models


class MovieViewSet(viewsets.ModelViewSet):
    """ViewSet for the Movie class"""

    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
