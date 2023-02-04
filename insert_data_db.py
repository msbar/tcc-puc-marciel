import math
from pathlib import Path

import pandas as pd

from db import ConnectionHandler
from logger import logger
from models import Dataset
from utils import FilesHandler

log = logger().getLogger(__name__)


class InsertDataDb:

    DATAFILES = Path("datafiles")

    def __init__(self) -> None:
        self.model = Dataset
        self.fh = FilesHandler(self.DATAFILES)
        self.files_list = self.fh.get_files_list()
        self.names = self.get_names()
        self.table = self.model.__tablename__
        self.db = ConnectionHandler()
        self.dtype = {}
        self.converters = {}

    def get_names(self):
        if not hasattr(self.model, "__added_columns__"):
            return self.model.__table__.columns.keys()

        return [
            name
            for name in self.model.__table__.columns.keys()
            if name not in self.model.__added_columns__
        ]

    def create_df(self, file=None, encoding="utf-8"):
        self.df = pd.read_csv(
            file,
            skiprows=1,
            sep=";",
            quotechar='"',
            encoding=encoding,
            names=self.names,
            dtype=self.dtype,
            converters=self.converters,
            on_bad_lines="warn",
            usecols=self.names,
        )

    def create_table(self):
        log.info(f"Criando tabela {self.table}")
        self.db.create_table(self.model)

    def insert_db(self, table):
        chunksize = math.floor(2097 / len(self.df.columns))
        chunksize = 1000 if chunksize > 1000 else chunksize
        self.df.to_sql(
            table,
            con=self.db.engine,
            index=False,
            method="multi",
            chunksize=chunksize,
            if_exists="append",
        )

    def load_data(self):
        self.create_table()

        for file in self.files_list:
            log.info(f"Criando DataFrame para o arquivo {file}.")
            if "precos-2022-11-glp.csv" in file or "precos-glp-09.csv" in file:
                encoding = "ISO-8859-1"
            else:
                encoding = "utf-8"

            self.create_df(file=file, encoding=encoding)

            log.info(f"Inserindo registros no Banco de Dados.")
            self.insert_db(self.table)
            log.info(f"Registros inseridos no Banco de Dados.")


def execute():
    insert_data_db = InsertDataDb()
    insert_data_db.load_data()
