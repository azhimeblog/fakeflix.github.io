from rest_framework import routers
from django.urls import path, include        # add this
from django.conf import settings             # add this
from django.conf.urls.static import static

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Movie", api.MovieViewSet)
router.register("Category", api.CategoryViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("movieapi/Movie/", views.MovieListView.as_view(), name="movieapi_Movie_list"),
    path("movieapi/Movie/create/", views.MovieCreateView.as_view(), name="movieapi_Movie_create"),
    path("movieapi/Movie/detail/<int:pk>/", views.MovieDetailView.as_view(), name="movieapi_Movie_detail"),
    path("movieapi/Movie/update/<int:pk>/", views.MovieUpdateView.as_view(), name="movieapi_Movie_update"),
    path("movieapi/Category/", views.CategoryListView.as_view(), name="movieapi_Category_list"),
    path("movieapi/Category/create/", views.CategoryCreateView.as_view(), name="movieapi_Category_create"),
    path("movieapi/Category/detail/<slug:slug>/", views.CategoryDetailView.as_view(), name="movieapi_Category_detail"),
    path("movieapi/Category/update/<slug:slug>/", views.CategoryUpdateView.as_view(), name="movieapi_Category_update"),
)
