import os
import requests
from mega import Mega

def download_file_from_mega(url, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        mega = Mega()

        m = mega.login()

        print(f"Downloading PVRTexTool...")
        file = m.download_url(url, destination_folder)

        if file:
            print(f"The file has been successfuly downloaded")
        else:
            print(f"Failed to download the file")
    except Exception as e:
        pass


def download_file_from_github(url, destination_folder):
    try:
        reponse = requests.get(url)
        
        if reponse.status_code == 200:
            with open(destination_folder, 'wb') as file:
                file.write(reponse.content)
            print(f"The file has been successfully downloaded")
        else:
            print(f"Failed to download the file. Response status: {reponse.status_code}")
    except Exception as e:
        pass


url = 'https://mega.nz/file/3L41DbTB#6UvK-Ae2PtsdG6_8JuL-kIcImEOxsnrnIvqvT91Eo9k'
github_url = 'https://mega.nz/file/2PB0SL5Y#xedYVKW0k-YKBaMhcDgbIQGa5cmeio__zAXhhJ_GoaM'
destination_folder = './scripts'

download_file_from_mega(github_url, destination_folder)
download_file_from_mega(url, destination_folder)
