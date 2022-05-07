import csv
import pandas as pd

df = pd.read_csv('Definizioni-TLN-22.csv')
# If you know the name of the column skip this
first_column = df.columns[0]

# Delete firstn col and row
# df = df.drop([first_column], axis=1)
'''data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}'''

print(df)

'''f = open("", "r")
csvreader = csv.reader(f)

rows = []
for row in csvreader:
    
    rows.append(row)

print(rows)'''

# 1 Creare una dizionario di tutte le definizioni per ogni emozione
# 2 Fare stemming/lemming di ogni frase
# 3 calcolare similarità tra tutte le definizioni di una singola categoria
'''for line in f:
    print(line)'''
