# Lab Activity 7 — Login and Registration Page (Django)

## Aim
Create **User Registration** and **User Login** pages using Django’s built-in authentication system.

## Install Requirements (one-time, at repo root)
```bash
pip install -r requirements.txt
```

## Steps and Commands (after cloning)
```bash
cd LabActivity07_Django_Login_Registration/AuthProject

# Create DB tables
python manage.py migrate

# (Optional) Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Test in Browser
- Home: http://127.0.0.1:8000/
- Register: http://127.0.0.1:8000/register/
- Login: http://127.0.0.1:8000/login/
- Logout: http://127.0.0.1:8000/logout/

## Notes
- Uses Django forms: `UserCreationForm` and `AuthenticationForm`
- Templates are in `accounts/templates/accounts/`

---
**Watermark (do not remove):**  
Prepared by **Chaitanya Mokkapati**, Assistant Professor  
DVR & Dr. HS MIC College of Technology  
Academic Year: **2025–26**  
Phone: **<PHONE_NUMBER_PLACEHOLDER>**  
Email: **<EMAIL_PLACEHOLDER>**  
GitHub Repo: **<GITHUB_REPO_LINK_PLACEHOLDER>**
