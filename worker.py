import os
import random
import string
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def generate_client_id(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def send_event_to_google_analytics(event_name: str, value: float):
    measurement_id = os.getenv('MEASUREMENT_ID')
    api_secret = os.getenv('API_SECRET')
    ga_url = f'https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}'
    ga_data = {
        'client_id': generate_client_id(),
        'events': [{
            'name': event_name,
            'params': {
                'value': value
            }
        }]
    }

    ga_response = requests.post(ga_url, json=ga_data)
    if ga_response.status_code == 204:
        print('Data sent to Google Analytics successfully.')
    else:
        print(f'Failed to send data to'
              f' Google Analytics. Status Code: {ga_response.status_code}'
              )


def fetch_current_currency() -> float:
    """
    [
        {
            "r030":840,
            "txt":"Долар США(довідковий)",
            "rate":38.9549,
            "cc":"USD",
            "exchangedate":"18.03.2024"
        }
    ]
    :return:
    """
    endpoint = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/dollar_info?json'
    response = requests.get(endpoint)
    if response.ok:
        data = response.json()
        return data[0]['rate']

    return 0.0


if __name__ == '__main__':
    usd_uah = fetch_current_currency()
    send_event_to_google_analytics('usd_uah', usd_uah)
    now = datetime.now().isoformat()
    print(f'{now}: Current USD to UAH exchange rate: {usd_uah}')
