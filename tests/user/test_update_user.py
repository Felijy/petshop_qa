import pytest

from modules.client import PetShop
from create_user_data import *

url = 'user/'

class TestCreateUser:
    @pytest.fixture
    def create_user(self, request):
        client = PetShop()
        user_data = request.param
        response = client.post_request('user', user_data)
        assert response.status_code == 200
        return client, user_data

    @pytest.fixture
    def pet_shop_client(self):
        return PetShop()

    class TestValid:
        @pytest.mark.parametrize('create_user', VALID_USER_DATA, indirect=True)
        @pytest.mark.parametrize('data', VALID_USER_DATA)
        def test_login_valid_user(self, create_user, data):
            client, user = create_user
            response = client.put_request(url + user['username'], data)
            assert response.status_code == 200
            assert "message" in response.json()

    class TestInvalid:
        @pytest.mark.parametrize('create_user', VALID_USER_DATA, indirect=True)
        @pytest.mark.parametrize('data', VALID_USER_DATA)
        def test_invalid_username_update_user(self, create_user, data):
            client, user = create_user
            response = client.put_request(url + user['username'] + '397hcbn27', data)
            assert response.status_code == 404

        @pytest.mark.parametrize('data', VALID_USER_DATA)
        def test_empty_field_update_user(self, pet_shop_client, data):
            response = pet_shop_client.put_request(url, data)
            assert response.status_code == 400

        @pytest.mark.parametrize('create_user', VALID_USER_DATA, indirect=True)
        def test_empty_body_update_user(self, create_user):
            client, user = create_user
            response = client.put_request(url + user['username'], None)
            assert response.status_code == 400 or response.status_code == 415