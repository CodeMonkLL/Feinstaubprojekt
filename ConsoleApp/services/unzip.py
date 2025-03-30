import os
import gzip

def unzip_files(download_dir):
    """
    Entpackt alle .gz Dateien im angegebenen Verzeichnis und speichert sie als .csv Dateien.
    
    :param download_dir: Pfad zum Ordner mit den heruntergeladenen .gz Dateien
    """
    for filename in os.listdir(download_dir):
        if filename.endswith(".gz"):
            gz_path = os.path.join(download_dir, filename)
            csv_path = gz_path[:-3]  # Entfernt das ".gz" Suffix
            
            try:
                with gzip.open(gz_path, 'rt', encoding='utf-8') as gz_file:
                    with open(csv_path, 'w', encoding='utf-8') as csv_file:
                        csv_file.write(gz_file.read())
                print(f"✅ Entpackt: {filename} -> {os.path.basename(csv_path)}")
                
            except Exception as e:
                print(f"❌ Fehler beim Entpacken von {filename}: {e}")

if __name__ == "__main__":
    # Relativer Pfad zum Download-Verzeichnis
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','downloads')
    unzip_files(download_dir)