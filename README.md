# Booking Scraper
An initial project to scrape some hotel information in Spain from Booking.com

The project is divided into two codes:
1. [booking_queue.py](https://github.com/daniribeirof/booking_scrap/blob/main/booking_queue.py)
It saves the hotel links, which are on the website's home page
Results saved in: [url_queue.json](https://github.com/daniribeirof/booking_scrap/blob/main/url_queue.json)

3. [booking_scrap.py](https://github.com/daniribeirof/booking_scrap/blob/main/booking_scrap.py)
It scrapes the hotel information contained in each link.
In this case, the information was:
- Name of the property
- Latitude
- Longitude
Results saved in: [booking_spain.csv](https://github.com/daniribeirof/booking_scrap/blob/main/booking_spain.csv)
