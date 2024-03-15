import requests
from .models import Proxy
from celery import shared_task


@shared_task()
def task_to_scrape_data():
    """
    This task is used to scrape and save data.
    """
    print('Task is Running....')
    url = "https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc"
    response = requests.get(url)

    if response.status_code == 200:
        response_data = response.json().get("data")
        proxies = []
        for data in response_data:
            ip = data.get("ip")
            port = data.get("port")
            protocols = data.get("protocols")
            country = data.get("country")
            uptime = data.get("upTime")
            proxies.append(Proxy(ip=ip, port=port, protocols=protocols, country=country, uptime=uptime))
        Proxy.objects.bulk_create(proxies)

    return response.status_code
