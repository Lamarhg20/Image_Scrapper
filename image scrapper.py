import requests
from bs4 import BeautifulSoup
site_map = 'https://www.pngmart.com/sitemap.xml'
response = requests.get(site_map)
xml = response.text
soup = BeautifulSoup(xml, 'xml')

#sitemap necissary
site_maps = []

for loc in soup.find_all('loc'):
    url = loc.text
    if 'part' in url:
        print(loc.text)
        site_maps.append(url)

site_map_1 = site_maps[0]
response = requests.get(site_map_1)

soup = BeautifulSoup(response.text, 'xml')

master_list = []
for loc in soup.find_all('loc'):
    url = loc.text
    master_list.append(url)

for image_url in master_list:
    print(image_url) #print url
    #request image from webpage
    response =requests.get(image_url)
    #parse through webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    #find specified line description with url and get image
    png_url = soup.find('a', {'class': 'download'})['href']
    image = requests.get(png_url)
    #name the image
    image_id = image_url.split('/')[-1]
    image_name = png_url.split('/')[-1]
    image_title = image_id + '-' + image_name
    #save image
    with open(image_title, 'wb') as file:
        file.write(image.content)
    #iterate only once
    break
#error handling
#if response.status_code > 200 and response.status_code < 400



