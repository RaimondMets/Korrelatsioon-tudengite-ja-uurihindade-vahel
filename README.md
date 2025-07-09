# Tudengite arvu ja korterihindade korrelatsioon Tartus ja Tallinnas 2014/15 - 2024/25
# Kõik skriptid on autori koostatud, ning töötavad vastavalt dokumenteeritud sisendfailide ja väljunditega.
> ⚠️ NB! Skriptide töötamiseks on vajalikud järgmised Python teegid:  
**`pandas`**, **`matplotlib`**, **`scipy`**

## 1. Märkus aastate kohta
Graafikutel ja Exceli failides kujutatud aastad viitavad vastavale õppeaastale.  
Näiteks märgitud aasta **2014** vastab õppeaastale **2014/2015**.  
Sama loogika kehtib kogu andmestikus.
   
## 2. Üliõpilaste arv
   
Üliõpilaste arvu saamiseks koostati exceli tabel, kus on õppeaastate kohta kirjas tudengite arv kõikides Tallinna ja Tartu ülikoolides.
Õppeaastate kaupa liideti tudengite arvud kokku eri Tallinna ja Tartu koolides, kasutades Pythonit ja Pandas teeki.
**skript** "KoolideKokkuLiitja.py"
**sisendfailid** "TartuUliopilased.xlsx" või "TallinnaUliopilased.xlsx"

Antud koodis arvutatakse tudengite arvu õppeaastate kaupa vastavalt sisendile - kas Tartus või Tallinnas ning koostatakse graafik.

## 3. Korterite üürihinnad

Kasutatud on üürihindade andmeid leheküljelt Kinnisvara.ee. Saadud PDF fail teisendati exceli failiks, selleks kasutati lehekülge https://www.freeconvert.com/pdf-to-excel.
Vigase teisenduse tõttu ei olnud saadud exceli failis kuupäevad õiges vormingus ning need tuli Pythonit kasutades õigeks muuta (date vorming). 

**skript** "Korterihindade keskmise leidja.py"
**sisendfail** "korterihinnad.xlsx"
**tagastatud fail** "akadeemilised_keskmised.xlsx"

Programmis korrastatakse andmed, arvutatakse keskmine üürihind õppeaasta kohta ning tagastatakse
korrastatud exceli fail "akadeemilised_keskmised.xlsx".

Keskmiste üürihindade graafikute koostamiseks on kasutatud:
**skript** "Korterite üürihindade keskmise graafik.py"
**sisendfail** "akadeemilised_keskmised.xlsx"


## 4. Korrelatsioon tudengite ja korteri üürihindade vahel

**skript** "Korrelatsioon.py"
**sisendfailid** "Tulemus_Tallinna_üliõpilased.xlsx",  "Tulemus_Tartu_Tudengid.xlsx",
"akadeemilised_keskmised.xlsx".

Koodis leitakse korrelatsioon, P-väärtus ning koostatakse korrelatsiooni visualiseerimiseks graafik. 


## Kausta struktuur

📁 Sisendfailid/
   ├── TartuUliopilased.xlsx
   ├── TallinnaUliopilased.xlsx
   └── korterihinnad.xlsx

📁 Skriptid/
   ├── KoolideKokkuLiitja.py
   ├── Korterihindade keskmise leidja.py
   ├── Korrelatsioon.py
   └── Korterite üürihindade keskmise graafik.py

📁 Valjundfailid/
   ├── Tulemus_Tartu_Tudengid.xlsx
   ├── Tulemus_Tallinna_üliõpilased.xlsx
   └── akadeemilised_keskmised.xlsx

   

   
   
