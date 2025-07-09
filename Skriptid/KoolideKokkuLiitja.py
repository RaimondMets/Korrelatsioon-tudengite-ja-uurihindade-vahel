import pandas as pd
import matplotlib.pyplot as plt

def funktsioon(failitee, ridadearv, pealkiri):
    #loen exceli faili sisse

    df = pd.read_excel(failitee, skiprows=1)
    df.columns = ['Aasta'] + list(df.columns[1:])

    #kustutan tühjad väärtused

    df = df.dropna()

    #teisendan kõik väärtused arvudeks

    for veerg in df.columns[1:]:
        df[veerg] = pd.to_numeric(df[veerg], errors='coerce')
    print(df.head(ridadearv))

    #liidan kõik väärtused kokku õppeaastate kaupa

    df['Koguarv'] = df.iloc[:, 1:].sum(axis=1)

    #väljastan andmed

    print(df[['Aasta', 'Koguarv']].head(ridadearv))

    #joonistan graafiku
    plt.figure(figsize=(10, 6))
    plt.plot(df['Aasta'], df['Koguarv'], marker='o')
    plt.title(pealkiri)
    plt.xlabel("Aasta")
    plt.ylabel("Tudengite koguarv")
    plt.grid(True)
    plt.xticks(df['Aasta'])
    plt.tight_layout()
    plt.show()

    # salvestame uue Excel-faili
    salvestusfail = "Tulemus_" + pealkiri.replace(" ", "_") + ".xlsx"
    df[['Aasta', 'Koguarv']].to_excel(salvestusfail, index=False)
    print(f"Andmed salvestatud faili: {salvestusfail}")


def main():
    failitee = input("Sisesta failitee: ")
    ridadearv = int(input("Sisesta ridadearv (pane 100): "))
    pealkiri = input("Sisesta pealkiri: ")
    funktsioon(failitee, ridadearv, pealkiri)

main()