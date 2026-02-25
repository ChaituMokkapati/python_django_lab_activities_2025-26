# Lab Activity 6 — “Hello World” using Django

## Aim
Create a basic Django application that displays “Hello World!” in a browser.

## Install Requirements (one-time, at repo root)
```bash
pip install -r requirements.txt
```

## Steps and Commands (after cloning)

```bash
cd LabActivity06_Django_Hello_World/helloworld_project

# Setup DB tables
python manage.py migrate

# Start server
python manage.py runserver
```

## Test in Browser
Open:
- http://127.0.0.1:8000/

## Project Notes
- The view is in `hello_app/views.py`
- App URLs are in `hello_app/urls.py`
- Project URLs include the app URLs in `helloworld_project/urls.py`

---
**Watermark (do not remove):**  

## Watermark
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025-26**  
Phone: **+91 6281487836**  
Email: **chaitanyamokkapati0@gmail.com**  
GitHub Repo: https://github.com/ChaituMokkapati/python_django_lab_activities_2025-26.git
