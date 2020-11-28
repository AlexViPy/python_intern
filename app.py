"""
app example

"""

import requests

def is_alive_host(hostname):
    #Проверить, что запрашиваемый хост возвращает http status 100<=x<400.
    try:
        response = requests.get(f"https://{hostname}")
        if 100 <= response.status_code <= 400:
            return True
    except requests.exceptions.ConnectionError:
            return False