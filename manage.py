import argparse

import insert_data_db
import scrapy
from logger import logger

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--runscript", help="Executa os scripts pelo nome")

args = parser.parse_args()

log = logger().getLogger("manage.py")


def main():
    if args.runscript:
        match args.runscript:
            case "scrapy":
                scrapy.execute()

            case "insert_data_db":
                insert_data_db.execute()

            case _:
                log.info(f"Script {args.runscript} não encontrado.")


if __name__ == "__main__":
    main()
