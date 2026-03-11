#pipeline

from etl.extract import extract
from etl.transform import transform
from etl.load import load

if __name__ == "__main__":
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)