from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def student_list_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    students = Student.objects.all().order_by("-id")
    return render(request, "records/student_list.html", {
        'form': form,
        'students': students,
    })

# Create your views here.
