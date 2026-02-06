from django.test import TestCase, Client
from django.urls import reverse
from .models import Species

class SpeciesModelTest(TestCase):
    def setUp(self):
        self.species = Species.objects.create(
            family="Rosaceae",
            genus="Rosa",
            species="damascena",
            barcode="TEST001",
            country="Turkey",
            major_taxon_group="Angiosperms",
            is_cultivated=True
        )

    def test_species_creation(self):
        """Test that the species is created correctly."""
        rose = Species.objects.get(barcode="TEST001")
        self.assertEqual(rose.genus, "Rosa")
        self.assertEqual(rose.family, "Rosaceae")
        self.assertTrue(rose.is_cultivated)

    def test_string_representation(self):
        """Test the string representation of the model."""
        self.assertEqual(str(self.species), "Rosa damascena")


class IndexViewTest(TestCase):
    def test_index_page_loads(self):
        """Test that the index page loads successfully."""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/index.html')


class SearchAPITest(TestCase):
    def setUp(self):
        Species.objects.create(
            family="Rosaceae",
            genus="Rosa",
            species="indica",
            barcode="11111",
            country="India",
            major_taxon_group="Angiosperms"
        )
        Species.objects.create(
            family="Fabaceae",
            genus="Pisum",
            species="sativum",
            barcode="22222",
            country="UK",
            major_taxon_group="Angiosperms"
        )

    def test_search_by_barcode(self):
        """Test searching by specific barcode."""
        client = Client()
        response = client.get(reverse('search_api'), {'barcode': '11111'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['genus'], 'Rosa')

    def test_search_by_family(self):
        """Test searching by family name."""
        client = Client()
        response = client.get(reverse('search_api'), {'family': 'Fabaceae'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['genus'], 'Pisum')

    def test_search_no_results(self):
        """Test search returning no results."""
        client = Client()
        response = client.get(reverse('search_api'), {'genus': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['results']), 0)


class DetailViewTest(TestCase):
    def setUp(self):
        self.plant = Species.objects.create(
            family="Anacardiaceae",
            genus="Mangifera",
            species="indica",
            barcode="DSAH000999",
            country="India",
            major_taxon_group="Angiosperms",
            collection_number="123/A",
            collector="John Doe",
            locality="Silent Valley",
            district="Palakkad",
            state="Kerala",
            altitude="1000m"
        )
        self.url = reverse('detail', args=[self.plant.barcode])

    def test_detail_view_success(self):
        """Test that the detail view loads correct data."""
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mangifera")
        self.assertContains(response, "DSAH000999")
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Silent Valley")

    def test_detail_view_404(self):
        """Test that invalid barcode returns 404."""
        client = Client()
        response = client.get(reverse('detail', args=['INVALID_CODE']))
        self.assertEqual(response.status_code, 404)
