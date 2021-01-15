import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Movie_list_view():
    instance1 = test_helpers.create_movieapi_Movie()
    instance2 = test_helpers.create_movieapi_Movie()
    client = Client()
    url = reverse("movieapi_Movie_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Movie_create_view():
    client = Client()
    url = reverse("movieapi_Movie_create")
    data = {
        "detail": "text",
        "watch_time": 1,
        "sound": "text",
        "category": "text",
        "name": "text",
        "trailer": "text",
        "year": 1,
        "picture": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Movie_detail_view():
    client = Client()
    instance = test_helpers.create_movieapi_Movie()
    url = reverse("movieapi_Movie_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Movie_update_view():
    client = Client()
    instance = test_helpers.create_movieapi_Movie()
    url = reverse("movieapi_Movie_update", args=[instance.pk, ])
    data = {
        "detail": "text",
        "watch_time": 1,
        "sound": "text",
        "category": "text",
        "name": "text",
        "trailer": "text",
        "year": 1,
        "picture": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_list_view():
    instance1 = test_helpers.create_movieapi_Category()
    instance2 = test_helpers.create_movieapi_Category()
    client = Client()
    url = reverse("movieapi_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view():
    client = Client()
    url = reverse("movieapi_Category_create")
    data = {
        "cat_name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view():
    client = Client()
    instance = test_helpers.create_movieapi_Category()
    url = reverse("movieapi_Category_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view():
    client = Client()
    instance = test_helpers.create_movieapi_Category()
    url = reverse("movieapi_Category_update", args=[instance.slug, ])
    data = {
        "cat_name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302
