import requests
from bs4 import BeautifulSoup

# اینجا 'https://www.wikipedia.org' رو وارد کن
my_URL = str(input("please enter your link:\n"))
# <-- اینجا 'central-featured-lang' رو وارد کن
my_class = str(input("please enter your class:\n"))

x = requests.get(my_URL, verify=True)

x.encoding = 'utf-8'

soup = BeautifulSoup(x.text, 'html.parser')

print(f"HTTP Status Code: {x.status_code}")
print("First 500 characters of received HTML:")
print(x.text[:500])
print("---------------------------------")

print("Page Title:", soup.title.text)

elements_with_specific_class = soup.find_all('div', class_=my_class)
if elements_with_specific_class:
    print(f"\nFound Language Links with class '{my_class}':")
    for element_div in elements_with_specific_class:
        language_link = element_div.find('a')
        if language_link:
            print(f"  - {language_link.text.split('articles')
                  [0].strip().replace('+', '')}")
else:
    print(f"No elements found with class '{my_class}'.")

print("\n--- Extracting Image Links ---")

image_tags = soup.find_all('img')

if image_tags:
    print("Image links found:")
    for img_tag in image_tags:
        image_url = img_tag.get('src')
        if image_url:
            print(f"  - {image_url}")
else:
    print("No images found on the page.")
