# Lab Activity 19 - Deployment of Django Website on Railway Using GitHub

Prepared until the account-required steps.

Local preparation completed:
- `requirements.txt`
- `.python-version`
- `.gitignore`
- production-ready `AuthSite/settings.py`

Run locally:

```bash
cd LabActivity19_Placeholder/AuthSite
python manage.py check
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Account-required steps you must do:

```bash
git init
git add .
git commit -m "Ready for Railway deployment"
git branch -M main
git remote add origin https://github.com/your-username/authsite.git
git push -u origin main
```

Railway settings from the manual:
- Start Command: `gunicorn AuthSite.wsgi --bind 0.0.0.0:$PORT`
- Pre-Deploy Command: `python manage.py migrate`
