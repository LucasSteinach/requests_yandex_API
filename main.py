import requests

import os

from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_href(self, file_name: str):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        response = requests.get(files_url, params={'path': f'/free/{file_name}'}, headers=headers)
        pprint(response)
        return response.json()['href']

    def uploading(self, path_to_file: str, list_of_files: list):
        for file in list_of_files:
            with open(path_to_file + file, 'rb') as f:
                requests.put(self.get_href(file),
                             params={'overwrite': True},
                             files={'file': f},
                             headers=self.get_headers()
                             )


def files_list_config(catalog=f'{os.getcwd()}\\'):
    files = []
    for file in os.listdir(catalog):
        files.append(file)
    return files


if __name__ == '__main__':
    directory = f'{os.getcwd()}\\upload\\'
    files_list = files_list_config(directory)
    Token = ''
    ya = YaUploader(token=Token)
    ya.uploading(directory, files_list)
