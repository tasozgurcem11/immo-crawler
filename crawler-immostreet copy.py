import requests
from bs4 import BeautifulSoup
import json, urllib.request
import urllib
import ssl

def cities_function():
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_North_Rhine-Westphalia_by_population"

    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    pretty_soup = soup.prettify()
    all_tables=soup.find_all('table')
    right_table=soup.find('table', {"class":'wikitable sortable'})
    for row in right_table.findAll("tr"):
        cells = row.findAll('td')

    rows = right_table.findAll("tr")
    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    lst_data = []
    for row in rows[1:]:
                data = [d.text.rstrip() for d in row.find_all('td')]
                lst_data.append(data)

    lst_data1 = []
    for row in rows[1:]:
                data = [d.text.rstrip() for d in row.select('td')]
                lst_data1.append(data)

    cities = []
    population = []

    for x in range(len(lst_data1)):
        cities.append(lst_data1[x][1])
        population.append(lst_data1[x][3])

    return cities, population

zip1 = 50670
address = "Wuppertal Adolfstr. 3"

context = ssl._create_unverified_context()
zipurl = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyA2At8jJ9fut9UYGBXWy3t0gXyPcm-PJPQ&address=" + str(zip1) + "&sensor=false&components=country:DE"
with urllib.request.urlopen(zipurl, context=context) as url:
    data = json.loads(url.read().decode())
    if "address_components" in str(data):
        print(data)
        data2 = data["results"][0]["formatted_address"]
        data2 = data2.replace(str(zip1), "")
        data2 = data2.replace(",", "")
        data2 = data2.replace(" ", "") 
        city = data2.replace("Germany", "")
        print(city)

        building_type = "flat" #house/flat
        sale_type = "rent" #buy/rent
        state = "nordrhein-westfalen"

        house_number = ''.join(x for x in address if x.isdigit())
        address_url = address.split(" ")

        length = len(address_url)
        control = 0
        y = 0
        for y in range(length):
            print(y)
            if house_number in address_url[y]:
                control = y
            y = y + 1
            
        del address_url[control:length]

        print(house_number)
        print(address)
        print(address_url)

        street_adress = ""

        try:
            address_url.remove(city.lower())
            print("removed city name!")
        except:
            pass
        try:
            address_url.remove(city)
            print("removed city name!")
        except:
            pass

        for item in address_url:
            if "Straße" in item:
                item = item.replace("Straße", "str")
            elif "straße" in item:
                item = item.replace("straße", "str")
            elif "strasse" in item:
                item = item.replace("strasse", "str")
            elif "str." in item:
                item = item.replace("str.", "str")
            elif "str ." in item:
                item = item.replace("str .", "str")
            street_adress = street_adress + item.lower() + "-"



        street_adress = street_adress + str(house_number)
        total_address = str(zip1) + "-" + city.lower() + "-" + street_adress
        print(total_address)
        urlx = "https://atlas.immobilienscout24.de/adresse/"+ total_address + "?marketingFocus=HOUSE_BUY#/"

        print(urlx)

        loop_number = 10
        total_count = 0

        while loop_number == 10 and total_count <= 3:
            total_count = total_count + 1
            s = requests.Session()
            response = s.get(urlx, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            pretty_soup = soup.prettify()
            test = soup.find(string="window.IS24.PropertyBook.onPageletReceiveSuccessful")
            test = soup.find_all("script", {"type": "text/javascript"})
            data = ""
            a = 0
            for tag in soup.find_all("script", {"type": "text/javascript"}):
                a = a + 1

                print(tag.sourceline, tag.sourcepos, a)
                if "priceHistory" in str(tag.string):
                    print("false")
                    data = tag.string
                    data = str(data)
                    loop_number = 0
                    
                else:
                    print("false")
                    loop_number = 10

        replace_list = [
            '<script type="text/javascript">',
            '</script>',
            'window.IS24.PropertyBook.onPageletReceiveSuccessful(',
            ');'
        ]
        for item in replace_list:
            data = data.replace(item, "")


        whole_data = data.split('{"year":2020,"price":', 10)
        tem_data = ["", "", "", "", "", "", "", ""]

        print(len(whole_data))
        tem_data2 = []
        a = []
        if len(whole_data) > 6:
            for x in range(0,8):
                # print(whole_data[1])
                tem_data[x] = whole_data[x].split('}],"mostRecentData"', 1)[0]
                # print(a)
                # print(tem_data[x])
                # tem_data2.append(float(tem_data[0]))
                
            print( "Haus kaufen:      " + str(tem_data[1]) + "€")
            print( "Wohnung kaufen:   " + str(tem_data[3])+ "€")
            print( "Haus mieten:      " + str(tem_data[5])+ "€")
            print( "Wohnung mieten:   " + str(tem_data[7])+ "€")

        elif len(whole_data) < 6:

            for x in range(0,5):
                # print(whole_data[1])
                tem_data[x] = whole_data[x].split('}],"mostRecentData"', 1)[0]
                # print(a)
                # print(tem_data[x])
                # tem_data2.append(float(tem_data[0]))

            print( "Haus kaufen:      " + str(tem_data[1]) + "€")
            print( "Wohnung kaufen:   " + str(tem_data[2])+ "€")
            print( "Haus mieten:      " + str(tem_data[3])+ "€")
            print( "Wohnung mieten:   " + str(tem_data[4])+ "€")
    elif "ZERO_RESULTS" in str(data):
        print("zip not found!")










    















