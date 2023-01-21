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
