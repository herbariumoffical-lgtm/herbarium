from django.contrib import admin
from .models import Species

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'genus', 'species', 'family', 'collection_date', 'collector', 'country')
    search_fields = ('genus', 'species', 'barcode', 'family', 'collector')
    list_filter = ('family', 'country', 'major_taxon_group', 'is_cultivated')
