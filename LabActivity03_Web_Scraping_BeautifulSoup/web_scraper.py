import requests
from bs4 import BeautifulSoup

def main():
    url = "http://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        print("Scraped Quotes:")
        for q in quotes:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            print(f"Quote: {text}")
            print(f"Author: {author}")
            print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
