"""
=============================================================
Projekt:  Budget Manager – Persönliche Finanzverwaltung
Autor:    Mehmet Durular
Kurs:     Programmierung mit Python – alfatraining
Datum:    April 2026

Beschreibung:
    Der Benutzer kann Einnahmen und Ausgaben erfassen,
    anzeigen, löschen und grafisch auswerten (matplotlib).

Verwendete Konzepte:
    OOP, Vererbung, Funktionen, Callback, list, dict,
    try/except, datetime, for/while/if, matplotlib, PEP-8
=============================================================
"""

from datetime import datetime          # Datum und Uhrzeit
import matplotlib.pyplot as plt        # Grafische Darstellung


# ── Basisklasse ──────────────────────────────────────────
class Transaction:
    """Basisklasse für eine Finanztransaktion."""

    def __init__(self, beschreibung: str, betrag: float, typ: str):
        self.beschreibung = beschreibung
        self.betrag = abs(betrag)                          # immer positiv
        self.typ = typ                                     # "Einnahme" oder "Ausgabe"
        self.datum = datetime.now().strftime("%d.%m.%Y")   # automatisches Datum

    def __str__(self) -> str:
        vorzeichen = "+" if self.typ == "Einnahme" else "-"
        return f"[{vorzeichen}] {self.datum} | {self.beschreibung:<18} | {self.betrag:>8.2f} EUR"


# ── Unterklassen (Vererbung) ──────────────────────────────
class Einnahme(Transaction):
    """Einnahme – erbt von Transaction."""
    def __init__(self, beschreibung: str, betrag: float):
        super().__init__(beschreibung, betrag, "Einnahme")


class Ausgabe(Transaction):
    """Ausgabe – erbt von Transaction."""
    def __init__(self, beschreibung: str, betrag: float):
        super().__init__(beschreibung, betrag, "Ausgabe")


# ── Hauptklasse ───────────────────────────────────────────
class BudgetManager:
    """Verwaltet alle Transaktionen und erstellt Auswertungen."""

    def __init__(self):
        self.transaktionen = []   # Liste aller Transaktionen

    def hinzufuegen(self, transaktion: Transaction) -> None:
        """Fügt eine Transaktion zur Liste hinzu."""
        self.transaktionen.append(transaktion)
        print(f"  ✔ Gespeichert: {transaktion.beschreibung}")

    def anzeigen(self) -> None:
        """Zeigt alle Transaktionen mit Index an."""
        if not self.transaktionen:
            print("  Keine Transaktionen vorhanden.")
            return
        print("\n" + "-" * 55)
        for i, t in enumerate(self.transaktionen):
            print(f"  [{i}] {t}")
        print("-" * 55)
        print(f"  KONTOSTAND: {self.kontostand():.2f} EUR")
        print("-" * 55)

    def kontostand(self) -> float:
        """Berechnet und gibt den aktuellen Kontostand zurück."""
        summe = 0.0
        for t in self.transaktionen:
            if t.typ == "Einnahme":
                summe += t.betrag
            else:
                summe -= t.betrag
        return summe

    def loeschen(self, index: int) -> None:
        """Löscht eine Transaktion anhand des Index."""
        if 0 <= index < len(self.transaktionen):
            entfernt = self.transaktionen.pop(index)
            print(f"  ✔ Gelöscht: {entfernt.beschreibung}")
        else:
            print("  ✘ Ungültiger Index!")

    def grafik(self) -> None:
        """Erstellt ein Balken- und Kreisdiagramm mit matplotlib."""
        if not self.transaktionen:
            print("  Keine Daten für die Grafik.")
            return

        # Summen berechnen
        einnahmen = sum(t.betrag for t in self.transaktionen if t.typ == "Einnahme")
        ausgaben  = sum(t.betrag for t in self.transaktionen if t.typ == "Ausgabe")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        fig.suptitle("Budget Manager – Übersicht", fontweight="bold")

        # Balkendiagramm
        ax1.bar(["Einnahmen", "Ausgaben"], [einnahmen, ausgaben],
                color=["#2ecc71", "#e74c3c"], edgecolor="white")
        ax1.set_ylabel("Betrag (EUR)")
        ax1.set_title("Vergleich")

        # Kreisdiagramm
        ax2.pie([einnahmen, ausgaben], labels=["Einnahmen", "Ausgaben"],
                colors=["#2ecc71", "#e74c3c"], autopct="%1.1f%%", startangle=90)
        ax2.set_title("Verteilung")

        plt.tight_layout()
        plt.show()


# ── Callback-Funktion ─────────────────────────────────────
def berechnung_anwenden(funktion, manager: BudgetManager) -> float:
    """Callback: Übergibt eine Funktion als Parameter und ruft sie auf."""
    return funktion(manager)


# ── Hilfsfunktion: sichere Eingabe ───────────────────────
def eingabe_betrag() -> float:
    """Liest einen positiven Betrag ein – mit Fehlerbehandlung (try/except)."""
    while True:
        try:
            wert = float(input("  Betrag (EUR): "))
            if wert <= 0:
                print("  ✘ Bitte einen positiven Betrag eingeben.")
            else:
                return wert
        except ValueError:
            print("  ✘ Ungültige Eingabe! Bitte eine Zahl eingeben.")


# ── Hauptprogramm ─────────────────────────────────────────
def main():
    """Startet den Budget Manager und steuert die Benutzerinteraktion."""
    print("\n  💰 Willkommen beim Budget Manager!\n")

    manager = BudgetManager()

    # Beispieldaten beim Start
    manager.hinzufuegen(Einnahme("Gehalt", 2500.00))
    manager.hinzufuegen(Ausgabe("Miete", 800.00))
    manager.hinzufuegen(Ausgabe("Lebensmittel", 200.00))

    # Hauptschleife
    while True:
        print("\n  1: Einnahme hinzufügen")
        print("  2: Ausgabe hinzufügen")
        print("  3: Transaktionen anzeigen")
        print("  4: Transaktion löschen")
        print("  5: Kontostand anzeigen")
        print("  6: Grafik anzeigen")
        print("  7: Beenden")

        auswahl = input("\n  Ihre Auswahl: ").strip()

        if auswahl == "1":
            beschreibung = input("  Beschreibung: ")
            manager.hinzufuegen(Einnahme(beschreibung, eingabe_betrag()))

        elif auswahl == "2":
            beschreibung = input("  Beschreibung: ")
            manager.hinzufuegen(Ausgabe(beschreibung, eingabe_betrag()))

        elif auswahl == "3":
            manager.anzeigen()

        elif auswahl == "4":
            manager.anzeigen()
            try:
                index = int(input("  Index zum Löschen: "))
                manager.loeschen(index)
            except ValueError:
                print("  ✘ Bitte eine ganze Zahl eingeben.")

        elif auswahl == "5":
            # Kontostand über Callback-Funktion abrufen
            stand = berechnung_anwenden(lambda m: m.kontostand(), manager)
            print(f"\n  💰 Kontostand: {stand:.2f} EUR")

        elif auswahl == "6":
            manager.grafik()

        elif auswahl == "7":
            print("\n  Auf Wiedersehen! 👋\n")
            break

        else:
            print("  ✘ Ungültige Auswahl! Bitte 1–7 eingeben.")


# Programm nur starten wenn direkt ausgeführt
if __name__ == "__main__":
    main()
