import webbrowser
import time
import subprocess

TEXT_FILE_PATH = "C:/Users/ibrya/Desktop/open_tabs.txt"

webbrowser.register("opera", None, webbrowser.BackgroundBrowser("C:/Users/ibrya/AppData/Local/Programs/Opera GX/opera.exe"))
open ("C:/Users/ibrya/AppData/Local/Programs/Opera GX/opera.exe")


def open_opera():
    opera_path = r"C:/Users/ibrya/AppData/Local/Programs/Opera GX/opera.exe"  # Opera GX'in tam yolu
    try:
        subprocess.Popen(opera_path)
        print("Opera GX açıldı.")
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {opera_path}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def open_websites_from_file():
    try:
        with open(TEXT_FILE_PATH, "r") as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()
            if url:
                print(f"Açılıyor: {url}")
                webbrowser.get("opera").open(url)
                time.sleep(1)  # Her URL arasında 1 saniye bekle
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {TEXT_FILE_PATH}")
    except Exception as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    open_opera()
    open_websites_from_file()
