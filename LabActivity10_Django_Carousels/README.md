# Lab Activity 10 — Django App with Carousels Feature (Bootstrap 5)

**Academic Year:** 2025–26  
**Course:** Python with Django  
**Lab Title:** Create a Django App with Carousels feature  

**GitHub Repository:** `<GITHUB_REPO_LINK_PLACEHOLDER>`  
**Contact (Phone):** `<PHONE_NUMBER_PLACEHOLDER>`  
**Contact (Email):** `<EMAIL_PLACEHOLDER>`  

---

## Aim
To create a Django application that integrates a **Bootstrap 5 Carousel** component to display a rotating slideshow of items, by reusing the `base.html` template and extending the existing Django project from Lab Activity 9.  
(Ref: Lab manual) 

## Objective
- Create a new Django app (`carousel`) inside the existing project.
- Build a Django model (`Slide`) to store carousel slide data.
- Perform migrations and add sample data using Django Admin or Django shell.
- Create a carousel view and template that renders a functional Bootstrap Carousel.
- Reuse template inheritance from `pages/base.html`.
- Update the navbar in `base.html` with a Carousel link.  
(Ref: Lab manual)

## Technologies Used
- **Python:** 3.10+ (recommended 3.12)
- **Django:** 5.2.x (manual uses 5.2.10)
- **Bootstrap:** 5.3.8 (CDN)
- **Database:** SQLite (default)

---

## Prerequisite (One Environment Only)
Create **one** virtual environment at the repository root (not inside this folder), then install dependencies:

```bash
# From repository root (after git clone)
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate       # macOS/Linux

python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Project Location (inside the repo)
This lab project is located at:

```
LabActivity10_Django_Carousels/django_carousel_app/
```

The Django apps used:
- `pages` (Home + base template)
- `catalog` (Tables/Grids from Lab 9)
- `carousel` (NEW in Lab 10)

---

## Steps and Commands (Run Exactly)

### Step 1 — Go to the project folder
```bash
cd LabActivity10_Django_Carousels/django_carousel_app
```

### Step 2 — Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3 — Create admin user (for adding slides)
```bash
python manage.py createsuperuser
```

### Step 4 — Add sample slide data (Option A: Django shell)
```bash
python manage.py shell
```

Then paste:
```
or
https://miro.medium.com/v2/resize:fit:720/format:webp/1*j0gjLpN1aaHuRowTKgr6yQ.jpeg
```

```python
from carousel.models import Slide

Slide.objects.bulk_create([
    Slide(
        title="Welcome to Django",
        caption="Build powerful web applications with Python and Django.",
        image_url="https://miro.medium.com/v2/resize:fit:720/format:webp/1*j0gjLpN1aaHuRowTKgr6yQ.jpeg",
        order=1
    ),
    Slide(
        title="Bootstrap 5 Integration",
        caption="Responsive and mobile-first front-end styling made easy.",
        image_url="https://miro.medium.com/v2/resize:fit:720/format:webp/1*j0gjLpN1aaHuRowTKgr6yQ.jpeg"",
        order=2
    ),
    Slide(
        title="Lab Activity 10",
        caption="Creating dynamic carousels using Django models and templates.",
        image_url="https://miro.medium.com/v2/resize:fit:720/format:webp/1*j0gjLpN1aaHuRowTKgr6yQ.jpeg"",
        order=3
    ),
    Slide(
        title="Product Showcase",
        caption="Display products, announcements, and more with image sliders.",
        image_url="https://miro.medium.com/v2/resize:fit:720/format:webp/1*j0gjLpN1aaHuRowTKgr6yQ.jpeg"",
        order=4
    ),
])
print("Sample slides created:", Slide.objects.count())
```

Exit the shell:
```python
exit()
```

### Step 5 — Run server
```bash
python manage.py runserver
```

### Step 6 — Verify in browser
- Home: `http://127.0.0.1:8000/`
- Tables: `http://127.0.0.1:8000/catalog/products/table/`
- Grid: `http://127.0.0.1:8000/catalog/products/grid/`
- Carousel: `http://127.0.0.1:8000/carousel/` ✅

### Step 7 — Add slides using Admin (Option B)
- Open: `http://127.0.0.1:8000/admin/`
- Login with superuser
- Add **Slide** records (title, caption, image_url, order, is_active)

---

## Important Files (Code Reference)
- `carousel/models.py` → `Slide` model
- `carousel/admin.py` → admin registration
- `carousel/views.py` → `carousel_view`
- `carousel/urls.py` → app URL routing
- `carousel/templates/carousel/carousel.html` → Bootstrap carousel template
- `mysite/settings.py` → add `carousel` to `INSTALLED_APPS`
- `mysite/urls.py` → include `path("carousel/", include("carousel.urls"))`
- `pages/templates/pages/base.html` → navbar link to Carousel

---

## Expected Output
- A Bootstrap carousel that auto-slides and supports Prev/Next controls.
- Slides are loaded dynamically from the database (Django model + ORM).

## Conclusion
**Note:** Students should write the conclusion in their own words (three sentences only).

---

## Watermark
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025-26**  
Phone: **+91 6281487836**  
Email: **chaitanyamokkapati0@gmail.com**  
GitHub Repo: https://github.com/ChaituMokkapati/python_django_lab_activities_2025-26.git
