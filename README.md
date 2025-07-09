# Tudengite arvu ja korterihindade korrelatsioon
# Kõik skriptid on autori koostatud, ning töötavad vastavalt dokumenteeritud sisendfailide ja väljunditega.

## 1. Märkus aastate kohta
Graafikutel kujutatud tudengite arv aastate lõikes tähendab seda, et kui graafikul on aasta 2014, on selle all mõeldud õppeaastat 2014/15.
   
## 2. Üliõpilaste arv
   
Üliõpilaste arvu saamiseks koostasin exceli tabeli, kus on õppeaastate kohta kirjas tudengite arv kõikides Tallinna ja Tartu ülikoolides.
Õppeaastate kaupa liitsin tudengite arvud kokku eri Tallinna ja Tartu koolides, kasutades Pythonit ja Pandas teeki.
**skript** "KoolideKokkuLiitja.py"

Koodijupis saab kasutada järgnevaid koostatud exceli faile: **sisendfailid** "TartuUliopilased.xlsx" ja "TallinnaUliopilased.xlsx".
Antud kood joonistab graafiku tudengite koguarvu kohta eraldi linnades (vastavalt soovile kas Tallinnas või Tartus), ning salvestab ka saadud tulemuse exceli faili.
Kood väljastas järgnevad failid: **tagastatud failid** "Tulemus_Tallinna_üliõpilased.xlsx", "Tulemus_Tartu_Tudengid.xlsx".

## 3. Korterite üürihinnad
Laadisin alla üürihindade andmed Kinnisvara.ee lehelt. Saadud PDF fail tuli ümber teha exceli failiks, kasutasin selleks https://www.freeconvert.com/pdf-to-excel.
Paraku ei teinud ta seda ideaalselt, saadud exceli failis kuupäevad ei olnud date formaadis, ning seetõttu pidin Pythoniga muutma need väärtused date-ks.
Saadud konverteeritud fail oli "korterihinnad.xlsx", kasutasin andmete korrastamiseks, keskmise üürihinna õppeaastate kaupa leidmiseks **skript** "Korterihindade keskmise leidja.py".
Koodijupp tagastab korrastatud exceli faili **tagastatud fail**"akadeemilised_keskmised.xlsx".

Graafiku joonistamiseks on kasutatud **skript** "Korterite üürihindade keskmise graafik.py"

## 4. Korrelatsioon tudengite ja korteri üürihindade vahel
**skript** "Korrelatsioon.py" arvutab välja korrelatsiooni ning P-väärtuse, samuti joonistab graafiku. Antud koodijupis kasutan eelnevalt saadud exceli faile "Tulemus_Tallinna_üliõpilased.xlsx",  "Tulemus_Tartu_Tudengid.xlsx",
"akadeemilised_keskmised.xlsx".
   

   
   
