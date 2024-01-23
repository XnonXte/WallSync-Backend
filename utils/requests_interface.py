import requests


class RequestsInterface:
    """Interface to make blocking requests to the internet."""

    def make_request(url, method="GET", json=None, headers=None):
        response = requests.request(method, url, json=json, headers=headers)

        if response.ok:
            try:
                data = response.json()
                return data
            except:
                return response
        else:
            raise Exception(f"{response.status_code} - {response.text}")
