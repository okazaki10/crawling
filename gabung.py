import pandas as pd
import glob

all_files = glob.glob("*.csv")
li = []

for filename in all_files:
    a = pd.read_csv(filename, sep=";")
    li.append(a)

c = pd.concat(li)
c.to_csv('dataset/dataset alodokter.csv', index=False,sep=";")