import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\TudengiteInfo\\akadeemilised_keskmised.xlsx")

print(df.columns)

#joonistame graafiku
plt.figure(figsize = (12,8))
#df['Tartu €/m²'] kui Tartu kohta, df['Tallinn €/m²'], kui Tallinna kohta
plt.plot(df['Akadeemiline_aasta'], df['Tartu €/m²'], marker='o')
plt.title("Keskmine üürihind ruutmeetri kohta Tartus")
plt.xlabel("Akadeemiline aasta")
plt.ylabel("Keskmine üürihind")
plt.grid(True)
plt.tight_layout()
plt.show()