# Lab Activity 9 — Django Application with Tables and Grids (Bootstrap)

## Aim
Create a Django application that displays database records using:
- **Bootstrap Table View**
- **Bootstrap Grid/Card View**

## Install Requirements (one-time, at repo root)
```bash
pip install -r requirements.txt
```

## Steps and Commands (after cloning)
```bash
cd LabActivity09_Django_Tables_Grids/django_tables_grids

# Create DB tables (default apps)
python manage.py migrate

# Create migration for catalog app + apply it
python manage.py makemigrations catalog
python manage.py migrate

# (Optional) Insert sample data using Django shell
python manage.py shell
```

### Optional sample data (paste inside shell)
```python
from catalog.models import Product

Product.objects.bulk_create([
    Product(name="Laptop Bag", category="Accessories", price=799.00, stock=25),
    Product(name="Wireless Mouse", category="Electronics", price=499.00, stock=40),
    Product(name="Notebook A4", category="Stationery", price=59.00, stock=120),
    Product(name="Water Bottle", category="Home", price=199.00, stock=60),
    Product(name="USB-C Cable", category="Electronics", price=149.00, stock=80),
])
```

### Run server
```bash
python manage.py runserver
```

## Test in Browser
- Home: http://127.0.0.1:8000/
- Table view: http://127.0.0.1:8000/catalog/products/table/
- Grid view: http://127.0.0.1:8000/catalog/products/grid/

## Files to observe
- `catalog/models.py` (Product model)
- `catalog/views.py` (table + grid views)
- `catalog/templates/catalog/*` (Bootstrap table & grid templates)
- `pages/templates/pages/base.html` (navbar updated with links)

---
**Watermark (do not remove):**  
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025–26**  

## Watermark
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025-26**  
Phone: **+91 6281487836**  
Email: **chaitanyamokkapati0@gmail.com**  
GitHub Repo: **[<GITHUB_REPO_LINK_PLACEHOLDER>](https://github.com/ChaituMokkapati/python_django_lab_activities_2025-26.git)**

