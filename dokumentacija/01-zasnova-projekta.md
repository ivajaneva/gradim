# 1. Projektna zasnova

## 1.1 Opis

**Gradim** je mobilna aplikacija za organizacijo in spremljanje dela na gradbišču, ki jo razvijamo za gradbeno podjetje **Aleks Stanovi** (Makedonija).

Danes se informacije izmenjujejo po telefonu, Viberju in v beležkah, zato je težko vedeti, kaj je narejeno in kaj čaka. Gradim na enem mestu združi naloge, izvajalce, napake, termine in material. Cilj je manj klicev, nič izgubljenih informacij in ažuren pregled za inženirje in vodjo podjetja.

## 1.2 Uporabniki

| Vloga | V aplikaciji |
|---|---|
| **Direktor** | ustvari projekt in dodeli inženirje, vidi vse projekte, odobri zahtevke za material, spremlja statistiko |
| **Inženir** | vodi faze in naloge, prijavlja napake, vnaša termine in material, ureja imenik izvajalcev |
| **Izvajalec** | aplikacije ne uporablja – sporočila prejme v Viberju |

## 1.3 Funkcionalnosti

| # | Funkcionalnost | Prioriteta |
|---|---|---|
| F1 | **Projekti in ekipa** – direktor ustvari projekt (tip, naslov, rok, proračun) z nadstropji in stanovanji ter dodeli inženirje | visoka |
| F2 | **Faze in naloge** – projekt dobi 20 privzetih faz, inženir jih lahko izklopi ali doda nove. Naloga velja za celo stavbo, nadstropje ali izbrana stanovanja in tip prostora (npr. »vse kopalnice v stavbi«) | visoka |
| F3 | **Spremljanje izvedbe** – status *ni začeto / v teku / zaključeno*, neobvezna fotografija ob zaključku | visoka |
| F4 | **Napake** – napaka s fotografijo in označbo, vezana na nalogo in stanovanje, pošiljanje izvajalcu prek Viberja z enim klikom | visoka |
| F5 | **Koledar** – prihodi izvajalcev, dobave, ogledi, opomnik večer prej | srednja |
| F6 | **Material** – naročeno, dokupljeno, porabljeno, preostalo; zahtevek za dokup, ki ga odobri direktor | srednja |
| F7 | **Izvajalci** – imenik kontaktov, dodajanje tudi iz kontaktov telefona | srednja |
| F8 | **Pregled** – napredek, roki, napake po izvajalcih, poraba proti proračunu | nizka |
