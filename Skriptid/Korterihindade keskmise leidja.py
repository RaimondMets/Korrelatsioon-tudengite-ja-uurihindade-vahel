import pandas as pd

# 1. lae Excelist vajalikud veerud
failinimi = "korterihinnad.xlsx"
df = pd.read_excel(failinimi)

# 2. nimeta veerud ümber selgemaks
df = df[['Kuupäev', 'Hind(m2)', 'Hind(m2).1']].copy()
df.columns = ['Kuupäev', 'Tallinn €/m²', 'Tartu €/m²']

# 3. muudan 'Kuupäev' kuupäevaks
df['Kuupäev'] = df['Kuupäev'].astype(str)
df['Kuupäev'] = pd.to_datetime(df['Kuupäev'], format="%m.%Y", errors='coerce')

# 4. eemalda vigased kuupäevad
df = df.dropna(subset=['Kuupäev'])
print(df[df['Kuupäev'].isna()])


# 5. lisa akadeemiline aasta
def akadeemiline_aasta(kuup):
    aasta = kuup.year
    return f"{aasta}/{aasta+1}" if kuup.month >= 8 else f"{aasta-1}/{aasta}"

df['Akadeemiline_aasta'] = df['Kuupäev'].apply(akadeemiline_aasta)

# 6. arvutan keskmised hinnad akadeemilise aasta järgi
keskmised = df.groupby('Akadeemiline_aasta')[['Tallinn €/m²', 'Tartu €/m²']].mean().reset_index()

# 7. vaata tulemust
print(keskmised)

# salvestan exceli failina
keskmised.to_excel("akadeemilised_keskmised.xlsx", index=False)
