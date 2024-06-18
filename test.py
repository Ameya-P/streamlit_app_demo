import pandas as pd

df = pd.read_csv("resources/v11.csv")
i = 0
for col in df.columns:
    print(str(i) + " - " + col)
    i += 1
