# TECON Web Scraper

A Python-based web scraping project built using Selenium and Beautiful Soup to extract product information from TE Connectivity product pages and export them into an Excel file.

---

# Features

This scraper extracts the following product details:

- Product Title
- Product Description
- Product Price
- Breadcrumb Navigation
- Product Images (High Resolution)
- Datasheet PDF Links
- Product Specifications (Headers & Values)

All data is stored in a structured Excel file.

---

# Project Structure

```plaintext
TECON-Scraper/
│
├── input/
│   └── TECON_List.xlsx
│
├── output/
│   └── tecon_out.xlsx
│
├── images/
│   └── sample_output.png
│
├── scraper.py
├── requirements.txt
└── README.md
```

---

# Input Format

The scraper reads data from an Excel file located in:

```
input/TECON_List.xlsx
```

### Required Columns:

| Manuf_no | Link |
|----------|------|
| Example 1 | https://example.com |
| Example 2 | https://example.com |

---

# Output Format

The scraped data is saved in:

```
output/tecon_out.xlsx
```

### Output Columns:

- SKU
- URL
- Title
- Description
- Price
- Breadcrumb
- Images
- Datasheet
- Spec_Headers
- Spec_Values

---

# Technologies Used

- Python
- Selenium
- BeautifulSoup4
- Pandas
- OpenPyXL
- WebDriver Manager

---

# Installation

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```
pandas
beautifulsoup4
selenium
webdriver-manager
openpyxl
```

---

# How to Run

Run the scraper using:

```bash
python scraper.py
```

---

# How It Works

1. Reads product URLs from Excel file
2. Opens each product page using Selenium
3. Waits for page to fully load
4. Extracts required product information using BeautifulSoup
5. Stores data in structured format
6. Saves final output into Excel file

---

# Notes

- Selenium is used for dynamic content rendering
- BeautifulSoup is used for HTML parsing
- Internet connection is required while running
- Chrome browser must be installed
- Some pages may take time to load depending on network speed

---

# Example Folder Layout

```plaintext
TECON-Scraper/
│
├── input/
│   └── TECON_List.xlsx
│
├── output/
│   └── tecon_out.xlsx
│
├── images/
│   └── sample_output.png
│
├── scraper.py
├── requirements.txt
└── README.md
```

---

# Future Improvements

- Headless browser execution
- Faster scraping with parallel processing
- Retry mechanism for failed URLs
- Logging system for debugging
- Database integration
```