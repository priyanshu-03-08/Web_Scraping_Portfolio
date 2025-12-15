import requests
from bs4 import BeautifulSoup
import pandas as pd

# --- 1. SETUP & SCRAPING ---
# Using the specific "Travel" category page
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store our data
titles = []
prices = []
book_ratings = [] # <--- New List!

# --- 2. EXTRACTION ---

# 2a. Extract Titles
for header in soup.find_all("h3"):
    title = header.find("a")['title']
    titles.append(title)

# 2b. Extract Prices
for price_tag in soup.find_all("p", class_="price_color"):
    price = price_tag.text
    prices.append(price)

# 2c. Extract Ratings (The New Part!)
for rating_tag in soup.find_all("p", class_="star-rating"):
    
    # The HTML looks like <p class="star-rating Three">
    # This line grabs the list of classes: ['star-rating', 'Three']
    rating_classes = rating_tag['class']
    
    # We always want the second item in that list (index 1), which is the word
    rating_word = rating_classes[1] 
    
    book_ratings.append(rating_word)


# --- 3. THE DELIVERABLE (Pandas) ---
# A. Create a Dictionary from our three lists
data = {
    'Title': titles,
    'Price': prices,
    'Rating': book_ratings # <--- New Column!
}

# B. Convert the Dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# C. Save the DataFrame to a CSV file (client-ready format)
df.to_csv('project_A_travel_books.csv', index=False) 

print("---")
print("✅ Project A Complete! Data saved to 'project_A_travel_books.csv'")
print("Head of the data:")
print(df.head())
print("---")