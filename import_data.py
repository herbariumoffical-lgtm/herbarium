
import os
import django
import csv
from datetime import datetime

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herbarium_project.settings')
django.setup()

from catalogue.models import Species

def parse_date(date_str):
    if not date_str:
        return None
    
    # Try multiple formats
    formats = [
        '%d/%m/%y',   # 6/6/97
        '%d/%m/%Y',   # 6/6/1997
        '%d-%m-%y',
        '%d-%m-%Y',
        '%Y-%m-%d'
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    
    print(f"Warning: Could not parse date: {date_str}")
    return None

def import_csv():
    file_path = 'DATA.csv'
    
    if not os.path.exists(file_path):
        print("Error: DATA.csv not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        count = 0
        updated = 0
        
        for row in reader:
            barcode = row.get('Barcode', '').strip()
            if not barcode:
                print(f"Skipping row {count+1}: No barcode")
                continue

            # Parse Date
            date_str = row.get('DATE OF COLLECTION', '')
            collection_date = parse_date(date_str)
            
            # Prepare Data
            defaults = {
                'family': row.get('FAMILY', ''),
                'genus': row.get('GENUS', ''),
                'species': row.get('SPECIES', ''),
                'collection_number': row.get('COLLECTION NUMBER', ''),
                'collector': row.get('COLLECTOR', ''),
                'collection_date': collection_date,
                'locality': row.get('LOCALITY', ''),
                'district': row.get('DISTRICT', ''),
                'state': row.get('STATE', ''),
                'country': row.get('COUNTRY', ''),
                'altitude': row.get('ALTITUDE', ''),
            }

            # Update or Create
            obj, created = Species.objects.update_or_create(
                barcode=barcode,
                defaults=defaults
            )
            
            if created:
                count += 1
                print(f"Created: {barcode} - {obj.genus} {obj.species}")
            else:
                updated += 1
                print(f"Updated: {barcode}")
                
        print(f"\nImport Completed!")
        print(f"New Records: {count}")
        print(f"Updated Records: {updated}")

if __name__ == "__main__":
    import_csv()
