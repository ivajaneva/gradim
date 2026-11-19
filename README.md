
# Gradim

Gradim je mobilna aplikacija za organizacijo in spremljanje dela na gradbišču. Namenjena je gradbenim inženirjem in vodstvu podjetja.

## Člani ekipe

- Nenad Jocić (vodja ekipe)
- Iva Janeva
- Kristina Radeva

## Tehnologije

- Flutter (Dart)
- Supabase
- PostgreSQL

## Predpogoji

Za zagon aplikacije potrebujemo:
- Nameščen Flutter SDK in Dart
- Android Studio z Android emulatorjem ali fizično Android napravo
- Git

## Namestitev in zagon

1. Kloniramo GitHub repozitorij:

   ```bash
   git clone https://github.com/USERNAME/gradim.git
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

5. Zaženemo aplikacijo:

   ```bash
   flutter run
   ```

## Preverjanje kode

Za analizo kode in zagon testov uporabimo:

```bash
flutter analyze
flutter test
```

Preverjanja se samodejno izvajajo tudi z GitHub Actions ob spremembah v repozitoriju.

## Dokumentacija

Podrobnejši opis projekta, funkcionalnosti, diagrami in prototipi so na voljo v mapi [dokumentacija](dokumentacija/).
