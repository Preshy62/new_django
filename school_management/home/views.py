from django.shortcuts import render


def about(request):
    return render(request, "about.html")


def student(request):
    context = {
        "name": "Grace",
        "department": "Computer Science"
    }
    return render(request, "student.html", context)

# Create your views here.
