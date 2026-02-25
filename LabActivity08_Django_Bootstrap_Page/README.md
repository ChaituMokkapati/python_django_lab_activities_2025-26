# Lab Activity 8 — Django Bootstrap Page

## Aim
Create a Django page and apply **Bootstrap 5** styling using template inheritance (`base.html` → `home.html`).

## Install Requirements (one-time, at repo root)
```bash
pip install -r requirements.txt
```

## Steps and Commands (after cloning)
```bash
cd LabActivity08_Django_Bootstrap_Page/django_bootstrap_lab

python manage.py migrate
python manage.py runserver
```

## Test in Browser
- http://127.0.0.1:8000/

## Files to observe
- `pages/templates/pages/base.html` (Bootstrap CDN + navbar)
- `pages/templates/pages/home.html` (extends base)
- `pages/static/pages/custom.css` (optional styling)

---
**Watermark (do not remove):**  

## Watermark
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025-26**  
Phone: **+91 6281487836**  
Email: **chaitanyamokkapati0@gmail.com**  
GitHub Repo: https://github.com/ChaituMokkapati/python_django_lab_activities_2025-26.git
