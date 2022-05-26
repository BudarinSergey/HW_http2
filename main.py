import os
import requests
from pprint import pprint

BASE_PATH = os.getcwd()
file = 'test11'
file_path = os.path.join(BASE_PATH, file)
print(file_path)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_ulr = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }

        params = {"path": disk_file_path, "overwrite" : "true"}
        response = requests.get(upload_ulr, params=params, headers=headers)
        pprint(response.json())
        return response.json()


    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href","" )
        response=requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Super")

if __name__ == '__main__':
    token = '_____'
    uploader = YaUploader(token)
    result = uploader.upload('my_netology/my_test.txt', 'test11.txt')

