import requests
from bs4 import BeautifulSoup

address = "Annenstraße 9"
monument = False

quartier_list = [
    "Arrenberg",
    "Barmen-Mitte‎",
    "Beek",
    "Berghausen",
    "Beyenburg-Mitte‎", 
    "Blombach-Lohsiepen‎", 
    "Blutfinke", 
    "Brill", 
    "Buchenhofen‎",
    "Clausen", 
    "Cronenberg-Mitte‎", 
    "Cronenfeld‎", 
    "Dönberg‎",
    "Eckbusch", 
    "Ehrenberg", 
    "Elberfeld-Mitte",
    "Erbschlö-Linde‎",
    "Fleute", 
    "Friedrich-Engels-Allee",
    "Friedrichsberg",
    "Grifflenberg", 
    "Hahnerberg", 
    "Hammesberg", 
    "Hatzfeld", 
    "Heckinghausen", 
    "Heidt", 
    "Herbringhausen", 
    "Hesselnberg",
    "Hilgershöhe‎",
    "Höhe",
    "Industriestraße",
    "Jesinghauser Straße",
    "Kohlfurth", 
    "Kothen", 
    "Küllenhahn",
    "Langerfeld-Mitte‎",
    "Lichtenplatz", 
    "Loh", 
    "Löhrerlen", 
    "Lüntenbeck", 
    "Nächstebreck-Ost",
    "Nächstebreck-West‎", 
    "Nevigeser Straße", 
    "Nordstadt", 
    "Nützenberg", 
    "Oberbarmen-Schwarzbach‎",
    "Osterholz", 
    "Ostersbaum", 
    "Rauental", 
    "Rehsiepen", 
    "Ronsdorf-Mitte/Nord‎", 
    "Rott", 
    "Schenkstraße", 
    "Schöller-Dornap‎", 
    "Schrödersbusch", 
    "Sedansberg",
    "Siebeneick",
    "Sonnborn", 
    "Sudberg", 
    "Südstadt", 
    "Tesche",
    "Uellendahl-Ost‎",
    "Uellendahl-West‎",
    "Varresbeck", 
    "Vohwinkel-Mitte",
    "Westring", 
    "Wichlinghausen-Nord‎",
    "Wichlinghausen-Süd‎",
    "Zoo",
]



urls = [
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Elberfeld-Mitte",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nordstadt_(A%E2%80%93F)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nordstadt_(G%E2%80%93K)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nordstadt_(L%E2%80%93M)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nordstadt_(N%E2%80%93S)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nordstadt_(T%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Ostersbaum_(A%E2%80%93F)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Ostersbaum_(G%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_S%C3%BCdstadt",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Grifflenberg",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Friedrichsberg",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Sonnborn",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Varresbeck",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_N%C3%BCtzenberg",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Brill_(A%E2%80%93F)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Brill_(G%E2%80%93O)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Brill_(P%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Arrenberg_(A%E2%80%93F)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Arrenberg_(G%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Zoo_(A%E2%80%93J)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Zoo_(K%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Buchenhofen",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Uellendahl-West_(A%E2%80%93J)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Uellendahl-West_(K%E2%80%93Z)",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Uellendahl-Ost",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_D%C3%B6nberg",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Nevigeser_Stra%C3%9Fe",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Beek",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Eckbusch",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Siebeneick",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Vohwinkel-Mitte",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Tesche",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Sch%C3%B6ller-Dornap",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_L%C3%BCntenbeck",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Westring",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_H%C3%B6he",
        "https://de.m.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_im_Wuppertaler_Wohnquartier_Schr%C3%B6dersbusch",

    ]

Faddress = []
streetAddress = []
z = 0
while not monument:
    for url in urls:
        
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


        list_row = []
        for row in right_table.findAll("tr"):
            list_row.append(row)

        # print(len(list_row))

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []

        for x in range(len(lst_data1)):
            if ("Wohn" in lst_data1[x][1]) or ("haus" in lst_data1[x][1].lower()) or ("Fabrikgebäude" in lst_data1[x][1]) or ("Villa" in lst_data1[x][1]):
                a.append(lst_data1[x][2])
                b.append(lst_data1[x][4])
                c.append(lst_data1[x][1])
                d.append(lst_data1[x][6])

                e.append(lst_data1[x][0])
                f.append(lst_data1[x][3])
                g.append(lst_data1[x][5])
                
    
        for x in range(len(a)):
            a[x] = a[x].replace("Karte", "")
            a[x] = a[x].replace(u'\xa0', u' ')
            z = z + 1
            d[x] = d[x].replace("Wikidata", "")

            for y in range(len(quartier_list)):
                quartier_list[y] = quartier_list[y].replace(u'\u200e', u'')
                a[x] = a[x].replace(quartier_list[y], "")
            
            if a[x] in address:
                monument = True
                break
            else: 
                continue

            break

print("Total crawl number:" + str(z))
print(monument)
    















