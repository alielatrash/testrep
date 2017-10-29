import urllib2
import bs4
import pandas as pd

makes = 2000
pages = 25

for make in range(1,makes):
    for page in range(1,pages):
        theurl = 'https://www.contactcars.com/usedcars?search=uc&mk=%s&page=%s' % (make, page)

        headers = "car_make, car_model, car_year, car_price, car_km, car_cc\n"

        data_set = []

        # for url in theurl:
        thepage = urllib2.urlopen(theurl)
        soup = bs4.BeautifulSoup(thepage, "html.parser")

        g_data = soup.findAll('div', {"class":"panel custom_p_2"})
        z_data = soup.findAll('div', {"class": "large-9 medium-9 small-9 columns"})

        i = 0

        for item in g_data:

            print i

            data_2 = g_data[i].div
            car_make = data_2.findAll('p', {"class":"tit_2"})[0].text.encode('utf-8')
            car_model = data_2.findAll('p', {"class": "tit_3 right"})[0].text.encode('utf-8')
            car_year = data_2.findAll('p', {"class": "tit_3 right"})[1].text.encode('utf-8')
            car_price = data_2.findAll('span', {"class": "orange_txt left"})[0].text.encode('utf-8')

            for data in z_data:
                data_3 = z_data[i]
                car_cc = data_3.findAll('p', {"class": "right tit_3"})[0].text.encode('utf-8')
                car_km = data_3.findAll('span', {"class": "right tit_2"})[0].text.encode('utf-8')

            i = i + 1

            final = data_set.append((car_make, car_model, car_year, car_price, car_km, car_cc))

            print car_make
            print car_model
            print car_year
            print car_price
            print car_cc
            print car_km
            print theurl

            data_frame = pd.DataFrame(final, columns = [car_make, car_model, car_year, car_price, car_km, car_cc])

            data_frame.to_csv('contact_cars_final.csv', index=False, encoding='utf-8')

