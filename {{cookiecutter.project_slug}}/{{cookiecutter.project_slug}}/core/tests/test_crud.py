from http import HTTPStatus

import pytest
from django.urls import reverse
from model_bakery import baker

from {{cookiecutter.project_slug}}.core.models import User


@pytest.mark.django_db
def test_create(client):
    response = client.post(
        reverse("api-1.0.0:users"),
        content_type="application/json",
        data={
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@mail.com",
            "username": "john.doe",
            "password": "123456",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert User.objects.count() == 1
    user = User.objects.get()
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "test@mail.com"
    assert user.username == "john.doe"


@pytest.mark.django_db
def test_retrieve(client):
    user = baker.make(User)

    response = client.get(reverse("api-1.0.0:user", kwargs={"id": user.pk}))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }


@pytest.mark.django_db
def test_list(client):
    user = baker.make(User)

    response = client.get(reverse("api-1.0.0:users"))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "count": 1,
        "items": [
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        ],
    }
