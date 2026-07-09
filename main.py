import pandas as pd
from io import StringIO

FILE_PATH = "./data/BI Fullstack case study dataset.csv"

def read_input_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = "\n".join(
        line.strip('"') for line in content.splitlines()
    )

    df = pd.read_csv(
        StringIO(content),
        sep=","
    )
    return df

if __name__ == "__main__":
    df = read_input_file(FILE_PATH)
    print(df.head())