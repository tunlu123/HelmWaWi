from Model.HelmBestand import helme  # Importiere das Dictionary mit den Helm-Daten

def filter_helme(groesse=None, max_preis=None, art=None, material=None):
    gefilterte_helme = []
    
    for helm in helme.values():
        # Prüfe alle Filterkriterien (Groß-/Kleinschreibung ignorieren)
        groesse_ok = (groesse is None) or (helm.groesse.upper() == groesse.upper())
        preis_ok = (max_preis is None) or (helm.preis <= max_preis)
        art_ok = (art is None) or (helm.art.lower() == art.lower())
        material_ok = (material is None) or (helm.material.lower() == material.lower())
        
        if groesse_ok and preis_ok and art_ok and material_ok:
            gefilterte_helme.append(helm)
    
    return gefilterte_helme