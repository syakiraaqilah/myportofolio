from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Syakira",
        "npm": "2506541622",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A CS student who navigates the tech world line by line, constantly"
            " on an endless quest to master new tech. Fueled by curiosity,"
            " driven by code, and always ready to debug any challenge."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Syakira",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
