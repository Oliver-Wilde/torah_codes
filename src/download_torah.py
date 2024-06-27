import requests

def download_torah():
    books = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy"]
    torah_text = ""
    
    for book in books:
        url = f"https://www.sefaria.org/api/texts/{book}?context=0&pad=0&wrapLinks=0&commentary=0&version=Tanach%20with%20Ta'amei%20HaMikra%2C%20On%20Your%20Way%2C%202013"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for section in data['he']:
                if isinstance(section, list):
                    torah_text += " ".join(section) + " "
                else:
                    torah_text += section + " "
        else:
            print(f"Failed to download {book}")
    
    with open("../data/torah.txt", "w", encoding="utf-8") as file:
        file.write(torah_text.strip())

if __name__ == "__main__":
    download_torah()
