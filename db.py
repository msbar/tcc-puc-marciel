from sqlalchemy import create_engine, text


class ConnectionHandler:

    engine = None

    def __init__(self):
        self.sqlite_file_name = "base.db"
        self.sqlite_url = f"sqlite:///{self.sqlite_file_name}"
        self.engine = create_engine(self.sqlite_url)

    def create_table(self, model):
        model.metadata.create_all(self.engine)
