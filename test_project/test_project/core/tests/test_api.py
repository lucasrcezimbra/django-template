from http import HTTPStatus

from django.urls import reverse


def test_hello_world(client):
    response = client.get(reverse("api-1.0.0:hello"))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Hello": "world"}
