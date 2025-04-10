import pytest

from modules.client import PetShop
from create_user_data import *

url = 'user/delete/'

class TestDeleteUser:
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
        def test_delete_valid_user(self, create_user):
            client, user = create_user
            response = client.delete_request(url + user["username"])
            assert response.status_code == 200

    class TestInvalid:
        @pytest.mark.parametrize('create_user', VALID_USER_DATA, indirect=True)
        def test_incorrect_delete_user(self, create_user):
            client, user = create_user
            response = client.delete_request(url + user["username"] + '32950ejf34ndi')
            assert response.status_code == 404

        def test_empty_field_delete_user(self, pet_shop_client):
            response = pet_shop_client.delete_request(url)
            assert response.status_code == 400