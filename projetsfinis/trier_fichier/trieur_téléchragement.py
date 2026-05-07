from pathlib import Path

chemin = Path(r"C:\Users\boris\Downloads")

EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".JPG": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents",
                      ".pdf": "Documents"}

fichiers = [f for f in chemin.iterdir() if f.is_file()]

for d in fichiers:
    type_d = EXTENSIONS_MAPPING.get(d.suffix, "Divers")
    dossier_type_d = chemin / type_d
    dossier_type_d.mkdir(exist_ok=True)
    fichier_d = dossier_type_d / d.name
    d.rename(fichier_d)
