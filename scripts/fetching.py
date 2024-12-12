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

def download_file_from_github(url, destination_folder, filename):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        print(f"Downloading SctxConverter...")
        reponse = requests.get(url)
        
        if reponse.status_code == 200:
            file_path = os.path.join(destination_folder, filename)
            with open(file_path, 'wb') as file:
                file.write(reponse.content)
        else:
            print(f"Failed to download the file. Response status: {reponse.status_code}")
    except Exception as e:
        pass


url = 'https://mega.nz/file/3L41DbTB#6UvK-Ae2PtsdG6_8JuL-kIcImEOxsnrnIvqvT91Eo9k'
github_url = 'https://github.com/Daniil-SV/SCTX-Converter/releases/download/1.0.0/SctxConverter.exe'
sc_script_name = 'SctxConverter.exe'
destination_folder = './scripts'

download_file_from_mega(url, destination_folder)
download_file_from_github(github_url, destination_folder, sc_script_name)

print('Done !')