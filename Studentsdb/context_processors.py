from .settings import PORTAL_URL

def get_portalUrl(request):
    return {'PORTAL_URL': PORTAL_URL}