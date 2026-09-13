# Automated Web Scraper & Data Pipeline

A Python-based web scraping tool that uses Playwright to collect book data across multiple pages, processes and validates the scraped data with Pandas, and exports the final dataset to CSV and Excel.

## Features

- Browser automation with Playwright
- Automatic pagination across multiple pages
- Data extraction:
  - Book title
  - Price
  - Rating
  - Availability
- Data cleaning and type conversion with Pandas
- Data validation using assertions
- CSV and Excel export options
- Command-line interface (CLI) using `argparse`
- Structured logging and error handling

## Project Structure

```
books_scraper/
├── src/
│   └── books_scraper/
│       ├── __init__.py
│       ├── scraper.py
│       ├── pipeline.py
│       └── main.py
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock
```

### File Descriptions

- **`scraper.py`**: Handles browser automation, DOM traversal, data extraction, and pagination logic using Playwright.
- **`pipeline.py`**: Converts raw records into a Pandas DataFrame, cleans data, performs assertions for validation, and exports to CSV/Excel.
- **`main.py`**: Entry point that coordinates the web scraper and data processing pipeline.

## Installation

1. Clone the repository:
   git clone [https://github.com/YOUR_USERNAME/books-scraper.git](https://github.com/YOUR_USERNAME/books-scraper.git)
   cd books-scraper

2. Sync dependencies using `uv`:
   uv sync

3. Install Playwright browser binaries:
   playwright install

## Usage

Run the scraper using `uv`:

uv run src/books_scraper/main.py --url [https://books.toscrape.com/](https://books.toscrape.com/)

Specify a custom output file name (without file extension):

uv run src/books_scraper/main.py --url [https://books.toscrape.com/](https://books.toscrape.com/) --output books_output

This generates:
- `books_output.csv`
- `books_output.xlsx`

## Data Pipeline Flow

```
Website (HTML/DOM)
       ↓
Playwright (Automation & Scraping)
       ↓
Raw Records (List of Dicts)
       ↓
Pandas DataFrame
       ↓
Data Cleaning & Type Conversion
       ↓
Validation (Assertions)
       ↓
CSV & Excel Export
```

## Technologies Used

- **Python**
- **Playwright** – Dynamic web scraping & browser automation
- **Pandas** – Data transformation, cleaning, and export
- **openpyxl** – Excel file generation
- **argparse** – Command-line interface
- **logging** – Structured execution logging
- **uv** – Modern Python package and dependency management

## Example Output

The exported dataset produces the following structured format:

| Title | Price | Rating | Availability |
| :--- | :--- | :--- | :--- |
| A Light in the Attic | 51.77 | 3 | In stock |
| Tipping the Velvet | 53.74 | 1 | In stock |

## Learning Outcomes

This project demonstrates:
- HTTP and web scraping fundamentals
- DOM inspection and CSS selector targeting
- Asynchronous browser automation with Playwright
- Data cleaning and pipeline execution with Pandas
- Modular Python project structuring using the `src` layout