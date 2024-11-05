# animais/utils.py
import requests
import ipaddress

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_client_ipv4(request):
    ip = get_client_ip(request)
    try:
        ip_obj = ipaddress.ip_address(ip)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return str(ip_obj)
        else:
            return None
    except ValueError:
        return None

def get_geolocation(ip_address):
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url)
    data = response.json()
    latitude = data['lat']
    longitude = data['lon']
    return latitude, longitude