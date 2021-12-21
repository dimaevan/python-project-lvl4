from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_users_view(client):
    url = reverse('users')
    response = client.get(url)
    assert response.status_code == 200
    response = client.get('/')
    assert response.status_code == 200


