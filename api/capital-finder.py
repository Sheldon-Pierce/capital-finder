from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        args = requests.args

        if 'country' in args:
            country = args['country']
            url = f'https://restcountries.com/v3.1/name/{country}?fullText=true&fields=name,capital'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                capital = data[0]['capital'][0]
                return f"The capital of {country} is {capital}."
            else:
                return 'Failed to retrieve data.'

        elif 'capital' in args:
            capital = args['capital']
            url = f'https://restcountries.com/v3.1/capital/{capital}?fields=name,capital'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                country = data[0]['name']['common']
                return f"{capital} is the capital of {country}."
            else:
                return 'Failed to retrieve data.'

        else:
            return 'Invalid request.'

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return