import requests
from bs4 import BeautifulSoup
import pandas as pd # The crucial tool for this step

# --- 1. SETUP & SCRAPING ---
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store our data
titles = []
prices = []

# --- 2. EXTRACTION (The part you mastered) ---
# Extract Titles
for header in soup.find_all("h3"):
    title = header.find("a")['title']
    titles.append(title)

# Extract Prices
for price_tag in soup.find_all("p", class_="price_color"):
    price = price_tag.text
    prices.append(price)

# --- 3. THE DELIVERABLE (Pandas) ---
# A. Create a Dictionary from our lists
data = {
    'Title': titles,
    'Price': prices
}

# B. Convert the Dictionary into a Pandas DataFrame (like a spreadsheet)
df = pd.DataFrame(data)

# C. Save the DataFrame to a CSV file (client-ready format)
df.to_csv('book_data.csv', index=False) # index=False prevents writing a row number

print("---")
print("✅ Success! Data has been saved to 'book_data.csv'")
print(df.head()) # Shows the first 5 rows in the terminal for confirmation
print("---")