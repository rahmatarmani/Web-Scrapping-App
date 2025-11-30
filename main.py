import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    # Check request success
    if response.status_code != 200:
        print("Failed to retrieve website")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all quotes
    quotes = soup.find_all("span", class_="text")

    # Extract authors
    authors = soup.find_all("small", class_="author")

    print("📌 Quotes collected:\n")
    for q, a in zip(quotes, authors):
        print(f"{q.get_text()} — {a.get_text()}")


if __name__ == "__main__":
    scrape_quotes()
