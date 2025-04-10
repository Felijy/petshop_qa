import pytest

from modules.client import PetShop
from create_user_data import *

url = 'user/login'

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
        def test_login_valid_user(self, create_user):
            client, user = create_user
            response = client.get_request(url, {"username": user["username"], "password": user["password"]})
            assert response.status_code == 200
            assert "message" in response.json()

    class TestInvalid:
        @pytest.mark.parametrize('create_user', VALID_USER_DATA, indirect=True)
        def test_incorrect_password_login_user(self, create_user):
            client, user = create_user
            response = client.get_request(url, {"username": user["username"], "password": user["password"] + '124'})
            assert response.status_code == 400

        @pytest.mark.parametrize('login, password', {
            ('', ''), (None, None), ('', None), (None, '')
        })
        def test_empty_fields_login_user(self, pet_shop_client, login, password):
            response = pet_shop_client.get_request(url, {"username": login, "password": password})
            assert response.status_code == 400