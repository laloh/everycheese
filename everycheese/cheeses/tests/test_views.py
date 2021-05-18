import pytest
from django.test.testcases import SimpleTestCase
from django.urls import reverse
from django.contrib.sessions.middleware \
    import SessionMiddleware

from django.test import RequestFactory
from everycheese.users.models import User
from ..models import Cheese
from ..views import (
    CheeseCreateView,
    CheeseListView,
    CheeseDetailView
)
from .factories import CheeseFactory
pytestmark = pytest.mark.django_db


def test_good_cheese_create_view(rf, admin_user): # Order some cheese from the CheeseFactory cheese = CheeseFactory()
    # Make a request for our new cheese
    request = rf.get(reverse("cheeses:add"))
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    response = CheeseCreateView.as_view()(request) # Test that the response is valid
    assert response.status_code == 200
