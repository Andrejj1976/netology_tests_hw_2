import os
import pytest
import requests

YD_TOKEN = os.getenv("YD_TOKEN", "YOUR_YANDEX_DISK_TOKEN")
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"


@pytest.mark.skipif(
    YD_TOKEN == "YOUR_YANDEX_DISK_TOKEN",
    reason="Не задан токен Яндекс.Диска в переменной окружения YD_TOKEN",
)
class TestYandexDiskAPI:
    def setup_method(self):
        self.headers = {"Authorization": f"OAuth {YD_TOKEN}"}
        self.folder_name = "test_netology_folder"
        requests.delete(
            BASE_URL,
            headers=self.headers,
            params={"path": self.folder_name, "permanently": True},
        )

    def teardown_method(self):
        requests.delete(
            BASE_URL,
            headers=self.headers,
            params={"path": self.folder_name, "permanently": True},
        )

    def test_create_folder_success(self):
        response = requests.put(
            BASE_URL,
            headers=self.headers,
            params={"path": self.folder_name},
        )
        assert response.status_code == 201

        check_response = requests.get(
            BASE_URL,
            headers=self.headers,
            params={"path": self.folder_name},
        )
        assert check_response.status_code == 200
        assert check_response.json()["name"] == self.folder_name

    def test_create_existing_folder(self):
        requests.put(BASE_URL, headers=self.headers, params={"path": self.folder_name})
        response = requests.put(
            BASE_URL,
            headers=self.headers,
            params={"path": self.folder_name},
        )
        assert response.status_code == 409

    def test_create_folder_unauthorized(self):
        bad_headers = {"Authorization": "OAuth invalid_token_12345"}
        response = requests.put(
            BASE_URL,
            headers=bad_headers,
            params={"path": self.folder_name},
        )
        assert response.status_code == 401

    def test_create_folder_invalid_path(self):
        response = requests.put(
            BASE_URL,
            headers=self.headers,
            params={"path": "non_existent_parent_folder/sub_folder"},
        )
        assert response.status_code == 409