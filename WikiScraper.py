from bs4 import BeautifulSoup
import requests


class WikiScraper:
    def __init__(self, target):
        self.target = target
        self.path = target.replace(" ", "_")
        self.url = f"https://en.wikipedia.org/wiki/{self.path}"

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml"
        }

    def Scraper(self) -> dict:    
        """fetch and return wikipedia article titles."""
        page_to_scrape = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")

        return self._getTitles(soup)

    def getStatusCode(self):
        """ 
            Get the status code:
            1xx = Informational
            2xx = Success
            3xx = Redirection
            4xx = Client Error
            5xx = Server Error
        """
        response = requests.get(self.url, headers=self.headers, timeout=10)
        print(response.status_code)
        
    def checkIfExists(self):
        page_to_scrape = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        noArticle = soup.find("div", id="noarticletext")
        
        if (noArticle):
            return False
        
        return True

    def _getTitles(self, soup) -> dict:
        """Return a dictionary of title -> full Wikipedia URL."""
        wiki = {}

        for link in soup.find_all("a", href=True):
            href = link["href"]

            if href.startswith("/wiki/") and ":" not in href:
                title = link.get("title")
                if title:
                    wiki[title] = href

        return wiki
