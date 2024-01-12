import requests
import json

class GetPrograms:

    @staticmethod
    def get_programs():
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        try:
            response = requests.get(URL)
            response.raise_for_status() # Raises a HTTPError if the response was an HTTP error (4xx or 5xx).

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as err:
            print(f'Error occurred: {err}')
        except Exception as e:
            print(f'An error occurred: {e}')

programs = GetPrograms.get_programs()
print(programs)