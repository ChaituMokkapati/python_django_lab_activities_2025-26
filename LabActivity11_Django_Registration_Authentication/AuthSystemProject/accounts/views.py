from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("register")
        messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"register_form": form})

# Create your views here.
