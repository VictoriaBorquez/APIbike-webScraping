from django.http import HttpResponse
from django.shortcuts import render
import requests
from bike.models import Network, Location, Extra, Station







url = "https://api.citybik.es/v2/networks/bikerio"
response = requests.get(url)


if response.status_code == 200:
   json_data = response.json()

   

   location_data = json_data['network']['location']
   location = Location.objects.create(
      city=location_data['city'],
      country=location_data['country'],
      latitude=location_data['latitude'],
      longitude=location_data['longitude']
   )

   network = Network.objects.create(
      company=json_data['network']['company'],
      gbfs_href=json_data['network']['gbfs_href'],
      href=json_data['network']['href'],
      name=json_data['network']['name'],
      id_network=json_data['network']['id'],
      location=location
   )

   network.save()

   stations_data = json_data['network']['stations']
   for station_data in stations_data:
      extra_data = station_data['extra']
      extra = Extra.objects.create(
         address=extra_data['address'],
         altitude=extra_data['altitude'],
         ebikes=extra_data['ebikes'],
         has_ebikes=extra_data['has_ebikes'],
         last_updated=extra_data['last_updated'],
         normal_bikes=extra_data['normal_bikes'],
         payment=extra_data['payment'],
         payment_terminal=extra_data['payment-terminal'],
         renting=extra_data['renting'],
         returning=extra_data['returning'],
         slots=extra_data['slots'],
         uid=extra_data['uid']
      )

      station = Station.objects.create(
         empty_slots=station_data['empty_slots'],
         extra=extra,
         free_bikes=station_data['free_bikes'],
         id_station=station_data['id'],
         latitude=station_data['latitude'],
         longitude=station_data['longitude'],
         name=station_data['name'],
         timestamp=station_data['timestamp']
      )

      network.stations.add(station)

   network.save()

def station(request):
   networks = Network.objects.all()
   return render(request, "bike/home.html", {'networks':networks})