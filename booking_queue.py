from playwright.sync_api import sync_playwright
from lxml import etree
import json


def make_queue(number_of_properties = 50):
    with sync_playwright() as pw:
        browser = pw.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        #go to url
        page.goto("https://www.booking.com/searchresults.en-gb.html?ss=Spain&dest_type=country&dest_id=197")

        properties_parsed = []

        _prev_height = -1
        _max_properties = number_of_properties
        _properties_count = 0

        while _properties_count <= _max_properties:
            page.keyboard.down('End')
            page.wait_for_timeout(2000)

            page_html = page.content()
            tree = etree.HTML(page_html)

            _new_height = page.evaluate("document.body.scrollHeight")
            if _new_height == _prev_height:
                page.wait_for_selector('//span[text()="Load more results"]')
                button = page.locator('//span[text()="Load more results"]//parent::button')
                button.click()
            
            _prev_height = _new_height
            num_loaded_properties = tree.xpath('//a[@data-testid="title-link"]/@href')
            _properties_count = len(num_loaded_properties)
            print('Number of loaded properties:', _properties_count)

        properties_parsed.extend(tree.xpath('//a[@data-testid="title-link"]/@href'))
        print("Number of properties added to queue:",len(properties_parsed))
        return properties_parsed


def save_queue(queue):
    properties_dict = {"urls_to_scrap": queue}

    with open('url_queue.json', 'w') as fp:
        json.dump(properties_dict, fp)

    print("url_queue exported")


prop_queue = make_queue(number_of_properties = 200)
save_queue(queue=prop_queue)