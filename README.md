# Gradim

Mobilna aplikacija za organizacijo in spremljanje dela na gradbišču – naloge, izvajalci, napake, termini in material na enem mestu. Razvijamo jo za gradbeno podjetje **Aleks Stanovi** (Makedonija) pri predmetu RVIR, UM FERI 2026/27.

**Tehnologije:** Flutter · Supabase (PostgreSQL, Auth, Storage) · Firebase Cloud Messaging · GitHub Actions

## Ekipa

- Nenad Jocić
- Iva Janeva
- Kristina Radeva

## Struktura repozitorija

```
.
├── lib/                 # koda Flutter aplikacije
├── test/                # testi
├── android/, ios/       # platformni projekti
├── dokumentacija/       # prototipna dokumentacija, mockupi, diagrami
└── .github/workflows/   # CI: Flutter (analiza, testi)
```

## Predpogoji

Za zagon aplikacije potrebujemo:
- Nameščen Flutter SDK in Dart
- Android Studio z Android emulatorjem ali fizično Android napravo
- Git

## Namestitev in zagon

1. Kloniramo GitHub repozitorij:

   ```bash
   git clone https://github.com/ivajaneva/gradim.git
   ```

2. Premaknemo se v mapo projekta:

   ```bash
   cd gradim
   ```

3. Namestimo odvisnosti:

   ```bash
   flutter pub get
   ```

4. Preverimo razpoložljive naprave:

   ```bash
   flutter devices
   ```

5. Zaženemo aplikacijo (ključi za Supabase se podajo ob zagonu, v repozitoriju jih ni):

   ```bash
   flutter run --dart-define=SUPABASE_URL=... --dart-define=SUPABASE_ANON_KEY=...
   ```

   Dokler Supabase še ni povezan, zadošča `flutter run`.

## Preverjanje kode

Za analizo kode in zagon testov uporabimo:

```bash
flutter analyze
flutter test
```

Preverjanja se samodejno izvajajo tudi z GitHub Actions ob spremembah v repozitoriju.

## Dokumentacija

1. [Projektna zasnova](dokumentacija/01-zasnova-projekta.md)
2. [Primeri uporabe in scenariji](dokumentacija/02-primeri-uporabe.md)
3. [Mockupi in navigacija](dokumentacija/03-mockupi-in-navigacija.md)
4. [Podatkovni model](dokumentacija/04-podatkovni-model.md)
5. [Arhitektura in tehnologije](dokumentacija/05-arhitektura-in-tehnologije.md)
6. [Načrt razvoja](dokumentacija/06-nacrt-razvoja.md)

## Mockupi

Najpomembnejši zasloni, razvrščeni po zavihkih spodnje navigacije (podrobno: [Mockupi in navigacija](dokumentacija/03-mockupi-in-navigacija.md)).

#### ① Projekti

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-01-direktor-projekti.png" width="190"><br><b>01</b> Seznam projektov</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-02-nov-projekt.png" width="190"><br><b>02</b> Nov projekt</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-18-pregled-podjetja.png" width="190"><br><b>18</b> Pregled podjetja</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-03-pregled-projekta.png" width="190"><br><b>03</b> Pregled projekta</td></tr><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-04-plan-del-naloge.png" width="190"><br><b>04</b> Plan del – faze in naloge</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-05-nova-naloga.png" width="190"><br><b>05</b> Nova naloga</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-06-podrobnosti-naloge.png" width="190"><br><b>06</b> Podrobnosti naloge</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-07-zakljucek-naloge.png" width="190"><br><b>07</b> Zaključek naloge</td></tr></table>

#### ② Koledar

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-08-koledar.png" width="190"><br><b>08</b> Koledar gradbišča</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-09-nov-termin.png" width="190"><br><b>09</b> Nov termin</td></tr></table>

#### ③ Napake

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-12-seznam-napak.png" width="190"><br><b>12</b> Seznam napak</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-13-podrobnosti-napake.png" width="190"><br><b>13</b> Podrobnosti napake</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-10-prijava-napake.png" width="190"><br><b>10</b> Prijava napake</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-11-viber-sporocilo.png" width="190"><br><b>11</b> Sporočilo v Viberju</td></tr></table>

#### ④ Material

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-14-pregled-materiala.png" width="190"><br><b>14</b> Pregled materiala</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-15-material-vracilo.png" width="190"><br><b>15</b> Podrobnosti materiala</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-16-zahtevek-material.png" width="190"><br><b>16</b> Zahtevek za material</td></tr></table>

#### ⑤ Izvajalci

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-17-izvajalci.png" width="190"><br><b>17</b> Imenik izvajalcev</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/sl/ekran-19-nov-izvajalec.png" width="190"><br><b>19</b> Nov izvajalec</td></tr></table>

<details>
<summary><b>🇲🇰 Makedonska različica (za naročnika)</b> – klikni za prikaz</summary>

Naročnik je iz Severne Makedonije, zato so mockupi pripravljeni tudi v makedonščini.

#### ① Projekti

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-01-direktor-projekti.png" width="190"><br><b>01</b> Seznam projektov</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-02-nov-projekt.png" width="190"><br><b>02</b> Nov projekt</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-18-pregled-podjetja.png" width="190"><br><b>18</b> Pregled podjetja</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-03-pregled-projekta.png" width="190"><br><b>03</b> Pregled projekta</td></tr><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-04-plan-del-naloge.png" width="190"><br><b>04</b> Plan del – faze in naloge</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-05-nova-naloga.png" width="190"><br><b>05</b> Nova naloga</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-06-podrobnosti-naloge.png" width="190"><br><b>06</b> Podrobnosti naloge</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-07-zakljucek-naloge.png" width="190"><br><b>07</b> Zaključek naloge</td></tr></table>

#### ② Koledar

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-08-koledar.png" width="190"><br><b>08</b> Koledar gradbišča</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-09-nov-termin.png" width="190"><br><b>09</b> Nov termin</td></tr></table>

#### ③ Napake

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-12-seznam-napak.png" width="190"><br><b>12</b> Seznam napak</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-13-podrobnosti-napake.png" width="190"><br><b>13</b> Podrobnosti napake</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-10-prijava-napake.png" width="190"><br><b>10</b> Prijava napake</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-11-viber-sporocilo.png" width="190"><br><b>11</b> Sporočilo v Viberju</td></tr></table>

#### ④ Material

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-14-pregled-materiala.png" width="190"><br><b>14</b> Pregled materiala</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-15-material-vracilo.png" width="190"><br><b>15</b> Podrobnosti materiala</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-16-zahtevek-material.png" width="190"><br><b>16</b> Zahtevek za material</td></tr></table>

#### ⑤ Izvajalci

<table><tr><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-17-izvajalci.png" width="190"><br><b>17</b> Imenik izvajalcev</td><td align="center" valign="top" width="25%"><img src="dokumentacija/mockupi/mk/ekran-19-nov-izvajalec.png" width="190"><br><b>19</b> Nov izvajalec</td></tr></table>

</details>

