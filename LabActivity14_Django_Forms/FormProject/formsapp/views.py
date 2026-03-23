from django.shortcuts import render

from .forms import StudentForm


def student_form_view(request):
    submitted_data = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
    else:
        form = StudentForm()

    return render(request, 'formsapp/student_form.html', {
        'form': form,
        'submitted_data': submitted_data
    })

# Create your views here.
