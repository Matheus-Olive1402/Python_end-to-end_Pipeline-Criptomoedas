#pipeline

from etl.extract import extract
from etl.transform import transform
from etl.load import load


def run_pipeline():

    print("Extraindo dados...")
    extract()

    print("Transformando dados...")
    transform()

    print("Carregando dados...")
    load()

    print("Pipeline finalizado!")


if __name__ == "__main__":
    run_pipeline()