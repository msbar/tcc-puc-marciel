import os

import requests


def download_file_stream(url_download: str, dest_folder: str):
    """
    Realiza o download do link filtrado e salva na pasta indicada.
    :param url_download: str
    :param dest_folder: str
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url_download.split("/")[-1].replace(" ", "_")
    file_path = os.path.join(dest_folder, filename)

    print(f"Tentando baixar a URL: {url_download}")
    r = requests.get(url_download, stream=True, headers={"User-Agent": "Custom"})
    if r.ok:
        print("Salvando em: ", os.path.abspath(file_path))
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download falhou: status code {}\n{}".format(r.status_code, r.text))


class FilesHandler:
    _dirs_path = None
    _dirs = None
    _files = None
    _files_list = None

    def __init__(self, root_dir):
        self._root_dir = root_dir
        self._walk_root_dir()

    def _walk_root_dir(self):
        for dirs_path, dirs, files in os.walk(self._root_dir):
            self._dirs_path = dirs_path
            self._dirs = dirs
            self._files = files
            self._files_list = [os.path.join(dirs_path, file) for file in files]

    def get_dirs_path(self):
        return self._dirs_path

    def get_dirs(self):
        return self._dirs

    def get_files(self):
        return self._files

    def get_files_list(self):
        return self._files_list

    def get_file_from_full_path(self, full_path):
        return os.path.split(full_path)[-1]
