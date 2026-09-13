from scraper import scrape_books
from pipeline import process_books, save_data
import logging
import argparse 

parser = argparse.ArgumentParser()

parser.add_argument(
    "--url",
    required=True,
    help="Website URL to scrape"
)
parser.add_argument(
    "--output",
    required=True,
    help="Output file name without extension"
)

args = parser.parse_args()

url = args.url

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# url = "https://books.toscrape.com/"
try:
    books = scrape_books(url)
    df = process_books(books)

    save_data(
        df,
        f"{args.output}.csv",
        f"{args.output}.xlsx"
    )
except Exception as e:
    logger.error("Pipeline failed: %s", e)