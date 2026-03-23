from django.shortcuts import redirect, render


def home(request):
    context = {
        'saved_name': request.COOKIES.get('last_login_name', ''),
        'saved_theme': request.COOKIES.get('preferred_theme', 'light'),
    }
    return render(request, 'home.html', context)


def start_session(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        theme = request.POST.get('theme')

        request.session['username'] = username
        request.session['theme'] = theme
        request.session['visit_count'] = 0
        request.session['login_status'] = 'Active'
        request.session.set_expiry(300)

        response = redirect('dashboard')
        response.set_cookie('last_login_name', username, max_age=86400)
        response.set_cookie('preferred_theme', theme, max_age=86400)
        return response
    return redirect('home')


def dashboard(request):
    if 'username' not in request.session:
        return redirect('home')

    request.session['visit_count'] = request.session.get('visit_count', 0) + 1

    context = {
        'session_key': request.session.session_key,
        'username': request.session.get('username'),
        'theme': request.session.get('theme'),
        'visit_count': request.session.get('visit_count'),
        'login_status': request.session.get('login_status'),
        'cookie_name': request.COOKIES.get('last_login_name'),
        'cookie_theme': request.COOKIES.get('preferred_theme'),
    }
    return render(request, 'dashboard.html', context)


def clear_session(request):
    request.session.flush()
    return redirect('home')


def clear_cookies(request):
    response = redirect('home')
    response.delete_cookie('last_login_name')
    response.delete_cookie('preferred_theme')
    return response

# Create your views here.
