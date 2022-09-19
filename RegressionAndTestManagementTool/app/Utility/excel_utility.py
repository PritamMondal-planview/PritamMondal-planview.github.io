import pandas as pd

file = "/resources/Regression_History.xlsx"


def write_to_csv(data_frame):
    df = pd.DataFrame(data=data_frame)
    df.to_csv(file, mode='a', index=False, header=False)
