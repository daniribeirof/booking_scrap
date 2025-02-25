import requests
import pandas as pd
import json
from lxml import etree

def scrap_url(url):
    source = requests.get(url)

    tree = etree.HTML(source.text)

    property_title = tree.xpath('//h2[contains(@class, "pp-header__title")]//text()')
    property_title = property_title[0]

    property_latlon = tree.xpath('//a[@data-atlas-latlng]//@data-atlas-latlng')
    property_latlon = property_latlon[0]
    property_latlon = property_latlon.split(',')
    property_lat = property_latlon[0]
    property_lon = property_latlon[1]

    property_dict = {
        'Name of the property': property_title,
        'Latitude': property_lat,
        'Longitude': property_lon
    }

    print('Successfully scraped', property_title)
    return property_dict


with open('url_queue.json', 'r') as file:
    data = json.load(file)

queue = data['urls_to_scrap']

df = []

for url in queue:
    property_data = scrap_url(url=url)
    df.append(property_data)

df = pd.DataFrame(data=df)
df.to_csv('booking_spain.csv', index=False)