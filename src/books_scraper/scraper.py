from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

def scrape_books(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(url)

        all_books = []
        while True:
            books = page.locator("article.product_pod").all()
            for bookie in books:
                d={}
                title1 = bookie.locator("h3 a").first.get_attribute("title")
                price1 = bookie.locator("p.price_color").text_content()
                rating1 = bookie.locator("p.star-rating").get_attribute("class").split()[1]
                availability1 = bookie.locator("p.instock.availability").text_content().strip() # removes trailing ( end and beginnning both ) white spaces
                d={
                    "title":title1,
                    "price":price1,
                    "rating":rating1,
                    "availability":availability1
                }
                all_books.append(d)
            next_button = page.locator("li.next a")
            logger.info("Scraping: %s", page.url)
            if next_button.count()==0:
                break
            relative = next_button.get_attribute("href")
            absolute = urljoin(page.url, relative)
            page.goto(absolute)


        browser.close()
        return all_books
