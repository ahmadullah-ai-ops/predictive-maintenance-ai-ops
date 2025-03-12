import pandas as pd

def collect_data():
    data = pd.read_csv('data/sample_logs.csv')
    print("Data collected successfully")
    return data

if __name__ == "__main__":
    collect_data()

