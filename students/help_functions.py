from django.http import HttpRequest

def get_portalUrl():
    return 'http://' + HttpRequest.get_host()