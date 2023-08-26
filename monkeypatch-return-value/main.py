import pandas as pd


def max_in_columns(filename):
    df = pd.read_csv(filepath_or_buffer=filename, sep="|", header=0)
    return {col: max(df[col]) for col in df.columns}


if __name__ == "__main__":
    print(max_in_columns(filename="animals.txt"))
