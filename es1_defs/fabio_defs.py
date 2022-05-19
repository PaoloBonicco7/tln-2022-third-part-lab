from pprint import pprint

#* Leggo il file in input, mi salvo ogni riga in minuscolo ed evito di salvare la prima parola (non è una definizione)
def read_file_line(path):
    defs = []
    with open(path, 'r') as f:
        for line in f:
            defs.append(line.lower().split(',')[1:])  
    return defs

#* Per l'ultimo ciclo non serve ripetere le iterazioni nel senso opposto (se contro A con B, non serve controllare B con A)
def calculate_similarity(defs):
    for i in range(len(defs)):
        for j in range(len(defs[i])):
            for k in range(j+1, len(defs[i])):
                print(f'*{defs[i][j]}* has score {similarity(defs[i][k].split(" "), defs[i][j].split(" "))} with *{defs[i][k]}*')

#* Calcolo la similarità come la lunghezza dell'intersezione tra i due set (le definizioni)
def similarity(def_1, def_2):
    return len(set(def_1).intersection(set(def_2)))
    
    
defs = read_file_line("/home/fazza/Documents/tln-2022-third-part-lab/def.csv")
calculate_similarity(defs)