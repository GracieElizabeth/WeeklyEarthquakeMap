import requests
import folium

api = "https://substack.com/redirect/29a44961-adaf-48b4-ba14-a86b575ea894?j=eyJ1IjoiNHhlMW4wIn0.U-z5hYQuSLbp4tL6d6QEXrp-_8dy7Zp12MR-Djqe5H0"
m = folium.Map()

def get_data(url):
    r = requests.get(url)
    response = r.json()

    for geo in response['features']:
        title = geo['properties']['title']
        url = geo['properties']['url']
        lat, long = geo['geometry']['coordinates'][:2]

        print(f'Title: '
              f'{lat}, {long}\n'
              f'{url}\n')
        generate_map(title, lat, long, url)


def generate_map(place, longitude, latitude, url):
    folium.Marker(
        location=[abs(latitude), longitude],
        tooltip=place,
        popup=f'{latitude}, {longitude}, {url}',
        icon=folium.Icon(color="blue"),
    ).add_to(m)


get_data(api)
m.save("map.html")