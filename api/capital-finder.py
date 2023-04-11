from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data["capital"][0]
                definitions.append(definition)
            message = str(f"The capital of {dic['country']} is {definitions[0]}")

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data['name']['common'][0]
                definitions.append(definition)
            message = str(f"{dic['capital']} is the capital of {definitions[0]}")

        else:
            message = "Give me a word to define please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return