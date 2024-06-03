import pandas as pd
import re
import csv

file_path = "italianwords.txt"
df = pd.read_csv(file_path, sep="\t", header=None)

for index, row in df.iterrows():
    italian_word = re.findall(r'[a-zA-Z]+', row[0])
    chinese_word = re.findall(r'[\u4e00-\u9fff]+', row[0])

    i = 1
    while True:
        italian_word.insert(i, " ")
        i += 2
        if i >= len(italian_word):
            break

    with open("italianwords.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([''.join(italian_word), ''.join(chinese_word)])

