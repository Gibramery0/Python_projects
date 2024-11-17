import pyautogui
import clipboard
import time

sayac = 0
az_onceki_url = 'url'
TEXT_FILE_PATH = "C:/Users/ibrya/Desktop/open_tabs.txt"

def main():
    global az_onceki_url, sayac
    url_list = []
    print("Program başladı, 5 saniye bekliyor...")
    time.sleep(5)

    while True:
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)
        current_url = clipboard.paste()

        if url_list and current_url == url_list[0]:
            break
        elif az_onceki_url == current_url:
            pyautogui.hotkey("ctrl", "shift", "tab")
            time.sleep(0.5)
        else:
            url_list.append(current_url)
            print(f"Kopyalanan URL: {current_url}")
            sayac += 1
            pyautogui.hotkey("ctrl", "shift", "tab")
            time.sleep(0.5)
        az_onceki_url = current_url

    print(f"Sekme sayısı: {sayac}")
    save_urls_to_file(url_list)

def save_urls_to_file(url_list):
    with open(TEXT_FILE_PATH, "w") as file:
        for url in url_list:
            file.write(url + "\n")
    print(f"Tüm URL'ler {TEXT_FILE_PATH} dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
