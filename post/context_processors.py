# myapp/context_processors.py

from .models import SiteLogo

def site_logo(request):
    try:        
        logo = SiteLogo.objects.first()
        logo2 = SiteLogo.objects.last()
    except SiteLogo.DoesNotExist:        
        logo = None 
        logo2 = None     
    return {'site_logo': logo, 'site_logo2': logo2}
