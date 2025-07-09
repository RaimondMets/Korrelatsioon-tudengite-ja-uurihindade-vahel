import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\TudengiteInfo\\akadeemilised_keskmised.xlsx")

print(df.columns) #selleks, et näha, mis veerud on, et saaks graafiku koostada

#joonistame graafiku, hetkel tartu kohta.
plt.figure(figsize = (12,8))
#df['Tartu €/m²'], marker='o') #Tallinna kohta tegemiseks tuleb df['Tartu €/m²'] asendada df['Tallinn €/m²']
plt.plot(df['Akadeemiline_aasta']
plt.title("Keskmine üürihind ruutmeetri kohta Tartus") #Pealkiri samuti, kui teha Tallinna kohta
plt.xlabel("Akadeemiline aasta")
plt.ylabel("Keskmine üürihind")
plt.grid(True)
plt.tight_layout()
plt.show()
