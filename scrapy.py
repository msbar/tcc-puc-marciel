from pathlib import Path

import requests
from bs4 import BeautifulSoup

from utils import download_file_stream

BASE_URL = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis"


def get_dataset_url_list():

    soup = BeautifulSoup(requests.get(BASE_URL).content, "html.parser")
    hrefs = [x.attrs["href"] for x in soup.findAll("a", class_="internal-link")]
    url_list = []
    for href in hrefs:
        if "glp" in href:
            if "2022" in href:
                url_list.append(href)
    return url_list


def download():
    for url in get_dataset_url_list():
        download_file_stream(url, dest_folder="datafiles")


def execute():
    download()
