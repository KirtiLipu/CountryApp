import argparse
import requests
import json

def lookup_country_code(country_code, data):
    try:
        country_name = data['data'][country_code]['name']
        return country_name
    except KeyError:
        return f"Country code {country_code} not found."

def load_data_from_api():
    api_url = 'https://www.travel-advisory.info/api'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        with open('data.json', 'w') as file:
            json.dump(data, file)
        return data
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def load_data_from_file():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Data file not found. Use 'lookup --update' to fetch data from the API.")
        return None

def lookup_country_name(country_name, data):
    for code, country_data in data['data'].items():
        if country_data['name'].lower() == country_name.lower():
            return code
    return f"Country name {country_name} not found."

def main():
    parser = argparse.ArgumentParser(description="Country code lookup service.")
    parser.add_argument('--countryCode', nargs='+', help="Country code(s) to look up")
    parser.add_argument('--update', action='store_true', help="Update data from API")
    args = parser.parse_args()

    if args.update:
        data = load_data_from_api()
    else:
        data = load_data_from_file()

    if data:
        if args.countryCode:
            for country_code in args.countryCode:
                country_name = lookup_country_code(country_code, data)
                print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()
