from django.urls import reverse
from rest_framework import status


#  Get list of tickets for author 1
def test_get_list_client_1(api_client_1, test_ticket_1, test_ticket_2):
    response = api_client_1.get(reverse('ticket_list'))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data['results']) == 2
    assert data['results'][0]['id'] == test_ticket_1.id
    assert data['results'][1]['id'] == test_ticket_2.id


#  Get list of tickets for author 2
def test_get_list_client_2(api_client_2, test_ticket_3):
    response = api_client_2.get(reverse('ticket_list'))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data['results']) == 1
    assert data['results'][0]['id'] == test_ticket_3.id


#  Get list of tickets for another client
def test_get_list_another_client(api_client_2, test_ticket_1, test_ticket_2):
    response = api_client_2.get(reverse('ticket_list'))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data['results']) == 0


#  Get list of tickets for support
def test_get_list_support(api_support, test_ticket_1, test_ticket_2, test_ticket_3):
    response = api_support.get(reverse('ticket_list'))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data['results']) == 3
    assert data['results'][0]['id'] == test_ticket_1.id
    assert data['results'][1]['id'] == test_ticket_2.id
    assert data['results'][2]['id'] == test_ticket_3.id


#  Get ticket detail for author
def test_get_detail_client_1(api_client_1, test_ticket_1):
    response = api_client_1.get(reverse('ticket_detail', args=(test_ticket_1.id,)))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert data['id'] == test_ticket_1.id


#  Get ticket detail for another user
def test_get_detail_another_client(api_client_2, test_ticket_1):
    response = api_client_2.get(reverse('ticket_detail', args=(test_ticket_1.id,)))
    assert response.status_code == status.HTTP_403_FORBIDDEN


#  Get ticket detail for support
def test_get_detail_support(api_support, test_ticket_1):
    response = api_support.get(reverse('ticket_detail', args=(test_ticket_1.id,)))
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert data['id'] == test_ticket_1.id


# Create new ticket for client
def test_post_ok(api_client_1):
    request_data = {
        'title': 'test title ticket',
        'text': 'test text ticket'
    }
    response = api_client_1.post(reverse('ticket_list'), data=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.data
    print(response_data)
    assert response_data['title'] == request_data['title']


#  Invalid data - missing title
def test_post_missing_title(api_client_1):
    request_data = {
        'text': 'test text ticket'
    }
    response = api_client_1.post(reverse('ticket_list'), data=request_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# Invalid - try to create new ticket for support
def test_post_support(api_support):
    request_data = {
        'title': 'test title ticket',
        'text': 'test text ticket'
    }
    response = api_support.post(reverse('ticket_list'), data=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


#  Support can change status of ticket
def test_update_detail_status(api_support, test_ticket_1, celery_app):
    request_data = {
        'status': 'solved'
    }
    response = api_support.put(reverse('ticket_detail', args=(test_ticket_1.id,)), data=request_data)
    print(test_ticket_1.status)
    assert response.status_code == status.HTTP_200_OK


# Invalid - user try to change status of ticket
def test_update_detail_status_client(api_client_1, test_ticket_1, celery_app):
    request_data = {
        'status': 'solved'
    }
    response = api_client_1.put(reverse('ticket_detail', args=(test_ticket_1.id,)), data=request_data)
    print(test_ticket_1.status)
    assert response.status_code == status.HTTP_403_FORBIDDEN
