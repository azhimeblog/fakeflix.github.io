from django.views import generic
from . import models
from . import forms


class MovieListView(generic.ListView):
    model = models.Movie
    form_class = forms.MovieForm


class MovieCreateView(generic.CreateView):
    model = models.Movie
    form_class = forms.MovieForm


class MovieDetailView(generic.DetailView):
    model = models.Movie
    form_class = forms.MovieForm


class MovieUpdateView(generic.UpdateView):
    model = models.Movie
    form_class = forms.MovieForm
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm
    slug_url_kwarg = "slug"


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    slug_url_kwarg = "slug"
