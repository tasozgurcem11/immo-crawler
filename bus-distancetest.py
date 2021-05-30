
import json, urllib.request
import ssl

zip1 = 42119
street_adress = "am+freudenberg+75"

key_geo = "AIzaSyDC1RZ-cUJdGrJmLmaDfi7KWPBmiaZTyF4"

if street_adress != "":
                geo_address = street_adress + '-' + str(zip1)

                print(geo_address)



                context = ssl._create_unverified_context()
                geo_api = "https://maps.googleapis.com/maps/api/geocode/json?address=" + geo_address + "&key=" + key_geo
                with urllib.request.urlopen(geo_api, context=context) as url:
                    geo_data = json.loads(url.read().decode())
                    geo_lat = geo_data["results"][0]["geometry"]["location"]["lat"]
                    geo_lng = geo_data["results"][0]["geometry"]["location"]["lng"]
                    print(geo_lat)
                    print(geo_lng)

                nearby_api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(geo_lat) +"%2C" + str(geo_lng) +"&rankby=distance&type=train_station&key=" + key_geo
                print(nearby_api)
                with urllib.request.urlopen(nearby_api, context=context) as url:
                    nearby_data_raw = json.loads(url.read().decode())
                    print(nearby_data_raw)

                    nearby_station_name = nearby_data_raw["results"][0]["name"]
                    nearby_station_lat = nearby_data_raw["results"][0]["geometry"]["location"]["lat"]
                    nearby_station_lng = nearby_data_raw["results"][0]["geometry"]["location"]["lng"]


                    print(nearby_station_name)

                distance_api = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(geo_lat) + "%2c" + str(geo_lng) + "&destination=" + str(nearby_station_lat) + "%2c" + str(nearby_station_lng) + "&mode=walk&key=" + key_geo
                with urllib.request.urlopen(distance_api, context=context) as url:
                    distance_raw = json.loads(url.read().decode())
                    nearby_station_distance = distance_raw["routes"][0]["legs"][0]["distance"]["text"]
                    nearby_station_duration = distance_raw["routes"][0]["legs"][0]["duration"]["text"]
                                                                                                                                                
                distance_api = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(geo_lat) + "%2c" + str(geo_lng) + "&destination=" + "50.9427839" + "%2c" + "6.9590705" + "&mode=walk&key=" + key_geo
                with urllib.request.urlopen(distance_api, context=context) as url:
                    distance_raw2 = json.loads(url.read().decode())
                    cologne_distance = distance_raw2["routes"][0]["legs"][0]["distance"]["text"]
                    cologne_duration = distance_raw2["routes"][0]["legs"][0]["duration"]["text"]                                                                    

                distance_api = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(geo_lat) + "%2c" + str(geo_lng) + "&destination=" + "51.22019577026367" + "%2c" + "6.792957305908203" + "&mode=walk&key=" + key_geo
                with urllib.request.urlopen(distance_api, context=context) as url:
                    distance_raw2 = json.loads(url.read().decode())    
                    dusseldorf_distance = distance_raw2["routes"][0]["legs"][0]["distance"]["text"]
                    dusseldorf_duration = distance_raw2["routes"][0]["legs"][0]["duration"]["text"]