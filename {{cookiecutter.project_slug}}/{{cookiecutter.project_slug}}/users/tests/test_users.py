import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker


@pytest.mark.django_db
def test_ok():
    baker.make(get_user_model())
    assert True
