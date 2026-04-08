"""
=============================================================
Projekt:  Budget Manager Web-Interface (Flask)
Autor:    Mehmet Durular
Kurs:     Programmierung mit Python – alfatraining
Datum:    April 2026

Beschreibung:
    Diese Flask-App dient als Web-Interface für den
    originalen BudgetManager. Sie ermöglicht die Anzeige
    und Verwaltung von Finanzen im Browser.
=============================================================
"""

from flask import Flask, render_template, request, redirect, url_for
from budget_manager import BudgetManager, Einnahme, Ausgabe
import io
import base64
import matplotlib.pyplot as plt

# Flask App Initialisierung
app = Flask(__name__)

# Instanz des BudgetManagers erstellen
manager = BudgetManager()

# Beispieldaten aus dem Originalprojekt laden
if not manager.transaktionen:
    manager.hinzufuegen(Einnahme("Gehalt", 2500.00))
    manager.hinzufuegen(Ausgabe("Miete", 800.00))


def plot_erstellen():
    """
    Erstellt die grafische Auswertung (Balken- & Kreisdiagramm)
    und konvertiert diese in einen Base64-String für HTML.
    """
    if not manager.transaktionen:
        return None

    # Daten für die Grafik berechnen
    einnahmen = sum(t.betrag for t in manager.transaktionen if t.typ == "Einnahme")
    ausgaben = sum(t.betrag for t in manager.transaktionen if t.typ == "Ausgabe")

    # Erstellung der Matplotlib-Figure (ähnlich wie in budget_manager.py)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle("Finanzübersicht", fontweight="bold")

    # Balkendiagramm (Vergleich)
    ax1.bar(["Einnahmen", "Ausgaben"], [einnahmen, ausgaben],
            color=["#2ecc71", "#e74c3c"], edgecolor="white")
    ax1.set_ylabel("Betrag (EUR)")
    ax1.set_title("Vergleich")

    # Kreisdiagramm (Verteilung)
    if (einnahmen + ausgaben) > 0:
        ax2.pie([einnahmen, ausgaben], labels=["Einnahmen", "Ausgaben"],
                colors=["#2ecc71", "#e74c3c"], autopct="%1.1f%%", startangle=90)
        ax2.set_title("Verteilung")

    plt.tight_layout()

    # Grafik in Buffer speichern und encodieren
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)
    return f"data:image/png;base64,{img_base64}"


@app.route('/')
def index():
    """Hauptseite: Zeigt die Liste, den Kontostand und die Grafiken an."""
    return render_template('index.html',
                           transaktionen=manager.transaktionen,
                           kontostand=manager.kontostand(),
                           plot_url=plot_erstellen())


@app.route('/add', methods=['POST'])
def add_transaction():
    """Endpunkt zum Hinzufügen einer neuen Transaktion."""
    try:
        desc = request.form.get('beschreibung')
        amount = float(request.form.get('betrag'))
        trans_type = request.form.get('typ')

        if trans_type == "Einnahme":
            manager.hinzufuegen(Einnahme(desc, amount))
        else:
            manager.hinzufuegen(Ausgabe(desc, amount))
    except (ValueError, TypeError):
        # Fehlerhafte Eingaben werden ignoriert
        pass

    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete_transaction(index):
    """Endpunkt zum Löschen einer Transaktion anhand des Index."""
    manager.loeschen(index)
    return redirect(url_for('index'))


# Start des Flask-Servers
if __name__ == '__main__':
    print("\n--- Budget Manager Web-Interface aktiv ---")
    print("Öffnen Sie: http://127.0.0.1:5000")
    print("------------------------------------------\n")
    app.run(debug=True, port=5000)