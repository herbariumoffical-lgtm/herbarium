from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Species

def index(request):
    families = Species.objects.values_list('family', flat=True).distinct().order_by('family')
    genera = Species.objects.values_list('genus', flat=True).distinct().order_by('genus')
    species_list = Species.objects.values_list('species', flat=True).distinct().order_by('species')
    barcodes = Species.objects.values_list('barcode', flat=True).distinct().order_by('barcode')
    countries = Species.objects.values_list('country', flat=True).distinct().order_by('country')
    major_groups = Species.objects.values_list('major_taxon_group', flat=True).distinct().order_by('major_taxon_group')
    
    context = {
        'families': families,
        'genera': genera,
        'species_list': species_list,
        'barcodes': barcodes,
        'countries': countries,
        'major_groups': major_groups,
    }
    return render(request, 'catalogue/index.html', context)


def detail(request, barcode):
    from django.shortcuts import get_object_or_404
    plant = get_object_or_404(Species, barcode=barcode)
    return render(request, 'catalogue/species_detail.html', {'plant': plant})

def search_api(request):
    query = request.GET
    
    results = Species.objects.all()

    # Filter by specific fields
    if query.get('family'):
        results = results.filter(family__icontains=query.get('family'))
    if query.get('genus'):
        results = results.filter(genus__icontains=query.get('genus'))
    if query.get('species'):
        results = results.filter(species__icontains=query.get('species'))
    if query.get('barcode'):
        results = results.filter(barcode__icontains=query.get('barcode'))
    
    # Dropdowns
    if query.get('country'):
        results = results.filter(country__iexact=query.get('country'))
    if query.get('major_group'):
        results = results.filter(major_taxon_group__iexact=query.get('major_group'))


        
    
    data = []
    for plant in results:
        data.append({
            'family': plant.family,
            'genus': plant.genus,
            'species': plant.species,
            'barcode': plant.barcode,
            'country': plant.country,
            'image_url': plant.image.url if plant.image else None,
            'id': plant.id
        })
    
    return JsonResponse({'results': data})
