from django.db import models

class Species(models.Model):
    family = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    major_taxon_group = models.CharField(max_length=100, blank=True, null=True)
    is_cultivated = models.BooleanField(default=False, verbose_name="Cultivated")
    collection_date = models.DateField(null=True, blank=True, verbose_name="Collection Date")
    collection_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Collection Number")
    collector = models.CharField(max_length=255, blank=True, null=True, verbose_name="Collector")
    locality = models.TextField(blank=True, null=True, verbose_name="Locality")
    district = models.CharField(max_length=100, blank=True, null=True, verbose_name="District")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="State")
    altitude = models.CharField(max_length=100, blank=True, null=True, verbose_name="Altitude")
    image = models.ImageField(upload_to='species_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.genus} {self.species}"

    class Meta:
        verbose_name_plural = "Species"
