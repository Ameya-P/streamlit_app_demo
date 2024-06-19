import pandas as pd

df = pd.read_csv("resources/v11.csv")
i = 0
for col in df.columns:
    print(str(i) + " - " + col)
    i += 1

""" df = pd.read_csv("resources/v11.csv")
string = "["
for col in df.columns:
    string = string + '"' + col + '", '

print(string) """

print(type('7,984,006') == type("string"))
int('7,984,006'.replace(",", ""))