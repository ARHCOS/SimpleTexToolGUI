import os
from mega import Mega

def download_file_from_mega(url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    mega = Mega()

    m = mega.login()

    print(f"Downloading PVRTexTool...")
    file = m.download_url(url, destination_folder)

    if file:
        print(f"The file has been successfuly downloaded")
    else:
        print(f"Unable to download the file")

# Exemple d'utilisation
url = 'https://mega.nz/file/3L41DbTB#6UvK-Ae2PtsdG6_8JuL-kIcImEOxsnrnIvqvT91Eo9k'
destination_folder = './scripts'

download_file_from_mega(url, destination_folder)
