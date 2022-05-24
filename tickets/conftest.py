import os

import pytest
from celery import Celery
from rest_framework.test import APIClient

from tickets.models import Ticket
from users.models import CustomUser


#  Create client 1
@pytest.fixture
def test_user_1(db):
    user = CustomUser.objects.create_user(username='client 1', email='test@client1.test')
    return user


#  Create client 2
@pytest.fixture
def test_user_2(db):
    user = CustomUser.objects.create_user(username='client 2', email='test@client2.test')
    return user


#  Create support
@pytest.fixture
def test_user_sup(db):
    user = CustomUser.objects.create_user(username='support', email='test@support.test', type='support')
    return user


# Auth client 1
@pytest.fixture
def api_client_1(test_user_1):
    client = APIClient()
    client.force_authenticate(test_user_1)
    return client


# Auth client 2
@pytest.fixture
def api_client_2(test_user_2):
    client = APIClient()
    client.force_authenticate(test_user_2)
    return client


# Auth support
@pytest.fixture
def api_support(test_user_sup):
    support = APIClient()
    support.force_authenticate(test_user_sup)
    return support


# Create ticket 1 for client 1
@pytest.fixture
def test_ticket_1(db, test_user_1):
    ticket, _ = Ticket.objects.get_or_create(
        title='test ticket 1',
        text='text ticket test 1',
        author=test_user_1
    )
    return ticket


# Create ticket 2 for client 1
@pytest.fixture
def test_ticket_2(db, test_user_1):
    ticket, _ = Ticket.objects.get_or_create(
        title='test ticket 2',
        text='text ticket test 2',
        author=test_user_1
    )
    return ticket


# Create ticket 3 for client 2
@pytest.fixture
def test_ticket_3(db, test_user_2):
    ticket, _ = Ticket.objects.get_or_create(
        title='test ticket 2',
        text='text ticket test 2',
        author=test_user_2
    )
    return ticket


@pytest.fixture(scope='module')
def celery_app(request):
    app = Celery()
    app.conf.task_always_eager = True
    return app
