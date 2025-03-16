import argparse
import requests

API_URL = "http://127.0.0.1:8000/predict"

def main():
    """Parses input arguments and-- sends a request to the prediction API."""
    parser = argparse.ArgumentParser(description="Send input data to the prediction API.")
    
    # Definiere alle Eingabeparameter für das Modell
    parser.add_argument("--produktname", type=str, required=True, help="Name des Versicherungsprodukts")
    parser.add_argument("--reisedauer", type=int, required=True, help="Dauer der Reise in Tagen")
    parser.add_argument("--reiseziel", type=str, required=True, help="Reiseziel")
    parser.add_argument("--nettoumsatz", type=int, required=True, help="Nettoumsatz in EUR")
    parser.add_argument("--kommission", type=int, required=True, help="Provision/Kommission in EUR")
    parser.add_argument("--alter", type=int, required=True, help="Alter der Kund*in")
    
    args = parser.parse_args()
    
    # Erstelle das JSON-Payload für die API
    payload = {
        "Produktname": args.produktname,
        "Reisedauer": args.reisedauer,
        "Reiseziel": args.reiseziel,
        "Nettoumsatz": args.nettoumsatz,
        "Kommission": args.kommission,
        "Alter": args.alter
        
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        
        # Ausgabe der Vorhersage
        print("\n✅ Vorhersageergebnis:")
        print(f"  ➝ Wahrscheinlichkeit für Leistungseintritt: {result.get('prediction', 'Keine Antwort'):.4f}\n")
    
    except requests.exceptions.RequestException as e:
        print("\n❌ Fehler beim Senden der Anfrage:", e)

if __name__ == "__main__":
    main()
