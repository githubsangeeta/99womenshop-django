#takes request as an argument and return the dictionary of data as a context
from .models import catagory

def menu_links(request):
    links = catagory.objects.all()
    return dict(links=links)