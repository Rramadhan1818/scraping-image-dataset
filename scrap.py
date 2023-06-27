import requests
from bs4 import BeautifulSoup
import os

url = 'https://portal.at-indonesia.co.id/'
save_folder = "images"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

for img in soup.findAll('img'):
    img_url = img.get('src')
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    elif not img_url.startswith('http'):
        img_url = url + '/' + img_url
    filename = os.path.join(save_folder, img_url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(img_url).content)
        print(f"Saved {filename}")