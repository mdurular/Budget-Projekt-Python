# 💰 Budget Manager – Persönliche Finanzverwaltung

## Projektbeschreibung

Der **Budget Manager** ist eine Konsolenanwendung in Python 3.12, mit der Benutzer ihre persönlichen Finanzen verwalten können. Das Programm ermöglicht das Erfassen von Einnahmen und Ausgaben, zeigt den aktuellen Kontostand an und erstellt eine grafische Auswertung mit **matplotlib**.

---

## 🚀 Programmstart

```bash
python budget_manager.py
```

> **Voraussetzung:** Python 3.12 und matplotlib müssen installiert sein.
> matplotlib installieren: `pip install matplotlib`

---

## 📋 Funktionen

| Funktion | Beschreibung |
|---|---|
| Einnahme hinzufügen | Beschreibung und Betrag eingeben |
| Ausgabe hinzufügen | Beschreibung und Betrag eingeben |
| Alle anzeigen | Vollständige Transaktionsliste |
| Löschen | Transaktion per Index entfernen |
| Kontostand | Aktueller Saldo (via Callback) |
| Grafik | Balken und Kreisdiagramm |

---

## 🏗️ Verwendete Python-Konzepte

**Objektorientierung (OOP)**
- `Transaction` -- Basisklasse für alle Transaktionen
- `Einnahme` -- erbt von `Transaction` (Vererbung)
- `Ausgabe` -- erbt von `Transaction` (Vererbung)
- `BudgetManager` -- Hauptklasse zur Verwaltung

**Funktionen**
- Eigene Funktionen mit Parametern und Rückgabewerten
- Callback Funktion (`berechnung_anwenden`)
- Hilfsfunktionen für sichere Benutzereingaben

**Datenstrukturen**
- `list` -- Speicherung aller Transaktionen
- `dict` -- Zusammenfassung der Finanzen

**Kontrollstrukturen**
- `while` Schleife -- Hauptmenü
- `for` Schleife  -- Transaktionen anzeigen
- `if / elif / else` -- Menüsteuerung

**Fehlerbehandlung**
- `try / except` -- Schutz vor ungültigen Eingaben (`ValueError`)

**Datum und Zeit**
- `datetime` -- automatische Datums- und Zeitstempelung

**Grafik**
- `matplotlib` -- Balkendiagramm und Kreisdiagramm

**Dokumentation**
- Docstrings bei allen Klassen und Funktionen
- Kommentare im Quellcode (PEP8 konform)

---

## 📁 Projektstruktur

```
projekt/
├── budget_manager.py     ← Hauptprogramm
├── README.md             ← Diese Datei
└── screenshots/
    ├── screenshot_1.png  ← Hauptmenü
    ├── screenshot_2.png  ← Transaktionseingabe
    └── screenshot_3.png  ← Matplotlib Grafik
```

---

## 📊 Klassendiagramm

```
+-------------------+
|    Transaction    |  ← Basisklasse
+-------------------+
| - beschreibung    |
| - betrag          |
| - datum           |
+-------------------+
| + __init__()      |
| + __str__()       |
+-------------------+
        △
        |  (Vererbung)
   _____|______
   |           |
+----------+ +----------+
| Einnahme | |  Ausgabe  |
+----------+ +----------+
| typ="+"  | | typ="-"   |
+----------+ +----------+

+----------------------+
|    BudgetManager     |  ← Hauptklasse
+----------------------+
| - transaktionen: list|
+----------------------+
| + transaktion        |
|   hinzufuegen()      |
| + alle_anzeigen()    |
| + kontostand         |
|   berechnen()        |
| + transaktion        |
|   loeschen()         |
| + zusammenfassung()  |
| + grafik_anzeigen()  |
+----------------------+
```

---

## 💡 Beispielausgabe

```
========================================
       💰 BUDGET MANAGER 💰
========================================
  1: Einnahme hinzufügen
  2: Ausgabe hinzufügen
  3: Alle Transaktionen anzeigen
  4: Transaktion löschen
  5: Kontostand anzeigen
  6: Grafik anzeigen
  7: Beenden
========================================

  [0] [+] 01.04.2025 10:00 | Gehalt               |    2500.00 EUR
  [1] [-] 01.04.2025 10:00 | Miete                |     800.00 EUR

  KONTOSTAND: 1700.00 EUR
```

---

## 👤 Autor

- **Name:** Mehmet Durular
- **Kurs:** Programmierung mit Python – alfatraining
- **Datum:** April 2026
