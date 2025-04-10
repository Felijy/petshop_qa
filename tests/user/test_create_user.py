import pytest

from modules.client import PetShop
from create_user_data import *

url = 'user'

class TestCreateUser:
    @pytest.fixture
    def pet_shop_client(self):
        return PetShop()

    class TestValid:
        @pytest.mark.parametrize('data', VALID_USER_DATA)
        def test_create_valid_user(self, pet_shop_client, data):
            response = pet_shop_client.post_request(url, data)
            assert response.status_code == 200

    class TestInvalid:

        @pytest.mark.parametrize('data', INCORRECT_ID_DATA)
        def test_incorrect_id_user(self, pet_shop_client, data):
            response = pet_shop_client.post_request(url, data)
            assert response.status_code == 400 # в доке ничего не написано, сервер возвращает 500, по хорошему должно быть 400

        @pytest.mark.parametrize('data', INCORRECT_FIELDS_DATA)
        def test_incorrect_fields_user(self, pet_shop_client, data):
            response = pet_shop_client.post_request(url, data)
            assert response.status_code == 400

        @pytest.mark.parametrize('data', EMPTY_FIELDS_DATA)
        def test_empty_fields_user(self, pet_shop_client, data):
            response = pet_shop_client.post_request(url, data)
            assert response.status_code == 400