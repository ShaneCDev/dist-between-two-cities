import requests
import streamlit as st
import os

if os.path.exists('env.py'):
    import env

API_KEY = os.environ.get('API_KEY')


def vincenty_geodesic():
    """
    return distance on the ellipsoid between two points using Vincentys inverse method
    a, b - semi-major and minor axes WGS84 model
    f - inverse flattening
    L, dL - delta longitude initial and subsequent
    u0, u1 reduced latitude
    s_sig - sine sigma
    c_sig - cosine sigma
    """
    a = 6378137.0
    b = 6356752.314245
    ab_b = (a**2 - b**2) / b**2
    f = 1.0/298.257223563
    pass


def get_lati_longi(api_key, address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address={address}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == 'OK':
            location = data["results"][0]["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]
            return lat, lng
        else:
            print(f'Error: {data["error_message"]}')
            return 0, 0
    else:
        print('Failed to make request')
        return 0, 0

if __name__ == '__main__':
    lati, longi = get_lati_longi(API_KEY, address='26 Ashfield Dr Townparks, Wexford, Y35 F5H6')
    print('Latitude:', lati)
    print('Longitude:', longi)




