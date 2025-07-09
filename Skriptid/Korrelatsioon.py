import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

AkadKeskmine = pd.read_excel("akadeemilised_keskmised.xlsx")

#Tartu veerg  = AkadKeskmine["Tartu €/m²"])
#Tallinna veerg = AkadKeskmine["Tallinn €/m²"]

TudengiteArvTallinn = pd.read_excel("Tulemus_Talinna_üliõpilased.xlsx")

TudengiteArvTartu = pd.read_excel("Tulemus_Tartu_Tudengid.xlsx")

Aastad = ["2014/15", "2015/16", "2016/17", "2017/18", "2018/19", "2019/20", "2020/21", "2021/22", "2022/23", "2023/24", "2024/25"]
TudengidTallinnas = TudengiteArvTallinn["Koguarv"]
TudengidTartus = TudengiteArvTartu["Koguarv"]
df = pd.DataFrame({
    'Aasta': Aastad,
    'Tudengid': TudengidTartus, #Vastavalt vajadusele, kas TudengidTartus või TudengidTallinnas
    'Korterihind': AkadKeskmine["Tartu €/m²"] #Vastavalt vajadusele, kas tartu või tallinna hinnad.
})

#arvutan korrelatsiooni
corr, p_value = pearsonr(df['Tudengid'], df['Korterihind'])
print(f"Korrelatsioonikordaja: {corr:.3f}")
print(f"P-väärtus: {p_value:.4f}")

#joonistame
fig, ax1 = plt.subplots(figsize=(12, 8))

# vasak telg tudengid
ax1.plot(df['Aasta'], df['Tudengid'], color='blue', label='Tudengite arv', linewidth=2)
ax1.set_ylabel('Tudengite arv')
ax1.tick_params(axis='y')

# parem telg korterihind
ax2 = ax1.twinx()
ax2.plot(df['Aasta'], df['Korterihind'], color='red', label='Korterihind (€/m²)', linewidth=2)
ax2.set_ylabel('Korterihind (€/m²)')
ax2.tick_params(axis='y')

# üldine info
plt.title("Tudengite arv ja Tartu üürihind aastate kaupa", fontsize=14) #Pealkiri vastavalt sellele, kas tartu või tallinn
ax1.set_xlabel("Aasta")
ax1.grid(True)

# legendid (mõlema telje jaoks)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.tight_layout()
plt.show()



