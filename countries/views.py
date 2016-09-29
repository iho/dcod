from django.http import JsonResponse
from django.shortcuts import get_list_or_404, render

from countries.models import Country, Region

def index(request):
    return render(request, 'countries/index.html')

def regions(request):
    return JsonResponse({region.id: region.name for region in Region.objects.all()})


def region(request, id):
    return JsonResponse({country.id: country.name for country in get_list_or_404(Country, region_id=id)})
