import requests
from pprint import pprint


class YaDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_files(self, file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        responce = requests.get(upload_url, headers = headers, params = params)
        response_getted = responce.json()
        
        href = response_getted.get("href", "")
        result = requests.put(href, data = open(filename, 'rb'))
        return result

if __name__ == '__main__':
    token = 'y0_AgAAAAAI...'
    uploader = YaDisk(token)
    pprint(uploader.upload_files('Homework_Python/Task_2.txt', 'Task 2_text.txt'))