import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

file_path = r"C:\Users\matha\PycharmProjects\Scrape\TECON_List.xlsx"
df = pd.read_excel(file_path)
output_data = []
options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
wait = WebDriverWait(driver, 15)
def scrape_product(url):
    data = {
        "title": "Not Found",
        "description": "Not Found",
        "price": "Not Found",
        "breadcrumb": [],
        "images": [],
        "h_list": [],
        "v_list": [],
        "datasheet": "Not Found"
    }
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            data["title"] = soup.find("h1").text.strip()
        except:
            pass
        try:
            desc = soup.find("div", class_="pdp-friendly-part-description")
            if desc:
                data["description"] = desc.text.strip()
        except:
            pass
        try:
            price = soup.find("span", class_="price-range").get_text(strip=True)
            if price:
                data["price"] = price.strip()
        except:
            pass
        try:
            breadcrumbs = [
                p.get_text(strip=True)
                for p in soup.select("p.breadcrumb-expanded-heading")
            ]
            data["breadcrumb"] = breadcrumbs
        except:
            pass
        try:
            imgs = soup.find(
                "div",
                class_="product-summary-gallery"
            )
            if imgs:
                img1 = imgs.find_all("img")
                data["images"] = list(set([
                    "https://www.te.com" + img.get("src").replace("product-small.png", "product-high-res.png")
                    for img in img1
                    if img.get("src")
                ]))
        except:
            pass
        try:
            h=[]
            v=[]
            features = soup.select("li.product-feature")
            for feat in features:
                title = feat.select_one("span.feature-title")
                value = feat.select_one("em.feature-value")
                if title and value:
                    clean_title = (title.get_text(strip=True).replace('\u2009', '').replace(" :", "").replace(":", "").strip())
                    h.append(clean_title)
                    v.append(value.get_text(strip=True).replace('\u2009', ''))
                    data["h_list"] = h
                    data["v_list"] = v
        except:
            pass
        try:
            pdf_links = []
            docs_div = soup.find("div", id="pdp-documents-tabpanel")
            if docs_div:
                for a in docs_div.find_all("a", href=True):
                    href = a["href"]
                    if "DocFormat=pdf" in href:
                        if href.startswith("/"):
                            href = "https://www.te.com" + href
                        pdf_links.append(href)
            data["datasheet"] = pdf_links
        except:
            pass
    except Exception as e:
        print(f"Scrape error: {e}")
    return data
for i in range(len(df)):
    sku = df.iloc[i, 0]
    url = df.iloc[i, 1]
    result = scrape_product(url)
    # PRINT DETAILS
    print(sku, url, result["title"], result["description"], sku, result["images"], result["breadcrumb"], result["price"], result["datasheet"],
          result["h_list"], result["v_list"])
    # Store output
    output_data.append({
        "SKU": sku, "URL": url, "Title": result["title"], "Description": result["description"], "Price": result["price"], "Breadcrumb": str(result["breadcrumb"]), "Images": str(result["images"]), "Datasheet": result["datasheet"], "Spec_Headers": str(result["h_list"]), "Spec_Values": str(result["v_list"])
    })
driver.quit()
output_df = pd.DataFrame(output_data)
output_path = r"C:\Users\matha\PycharmProjects\Scrape\tecon_out.xlsx"
output_df.to_excel(output_path, index=False)
print("Scrape completed. File saved at:", output_path)
