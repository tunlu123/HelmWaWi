from Controller.Logic import filter_helme

def benutzereingabe():
    print("=== Motorradhelm-Suche ===")
    groesse = input("Größe (z.B. M, L, XL, S, leer lassen für alle): ").strip() or None
    max_preis = input("Maximaler Preis (z.B. 200, leer lassen für alle): ").strip()
    max_preis = float(max_preis) if max_preis else None
    art = input("Art (z.B. Sport, Enduro, leer lassen für alle): ").strip() or None
    material = input("Material (z.B. Carbon, Polycarbonat, leer lassen für alle): ").strip() or None
    
    # Controller-Funktion aufrufen
    ergebnisse = filter_helme(
        groesse=groesse,
        max_preis=max_preis,
        art=art,
        material=material
    )
    
    # Ergebnisse ausgeben
    if not ergebnisse:
        print("\n❌ Keine passenden Helme gefunden.")
    else:
        print(f"\n🔍 Gefundene Helme ({len(ergebnisse)}):")
        for helm in ergebnisse:
            print(helm)