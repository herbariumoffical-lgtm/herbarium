
import zipfile
import os

def zip_project():
    project_files = [
        'manage.py',
        'requirements.txt',
        'db.sqlite3'
    ]
    project_dirs = [
        'herbarium_project',
        'catalogue',
        'media'
    ]
    
    zip_name = 'herbarium_deploy.zip'
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add individual files
        for file in project_files:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added {file}")
        
        # Add directories
        for directory in project_dirs:
            for root, dirs, files in os.walk(directory):
                # Skip __pycache__
                if '__pycache__' in dirs:
                    dirs.remove('__pycache__')
                
                for file in files:
                    if file.endswith('.pyc'):
                        continue
                    file_path = os.path.join(root, file)
                    zipf.write(file_path)
                    print(f"Added {file_path}")

    print(f"Successfully created {zip_name}")

if __name__ == "__main__":
    zip_project()
