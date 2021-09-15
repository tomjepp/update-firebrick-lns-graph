import requests
import requests.auth
import routeros_api
import yaml


def main():
    config = {}

    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    connection = routeros_api.RouterOsApiPool(
        host=config.get('router', {}).get('host'),
        username=config.get('router', {}).get('username'),
        password=config.get('router', {}).get('password'),
        plaintext_login=True
    )
    api = connection.get_api()

    result: list = api.get_resource('/interface/pppoe-client').call(
        'monitor',
        {
            'numbers': config.get('router', {}).get('pppoe-interface'),
            'once': 'once'
        }
    )

    if not len(result) == 1:
        return 1

    item: dict = result.pop()
    requests.post(
        url=f"{config.get('firebrick', {}).get('uri')}/ping",
        data={
            'graph': config.get('firebrick', {}).get('graph'),
            'ip': item.get('remote-address'),
            'table': '0',
        },
        auth=requests.auth.HTTPBasicAuth(
            username=config.get('firebrick', {}).get('username'),
            password=config.get('firebrick', {}).get('password'),
        )
    )


if __name__ == '__main__':
    main()
