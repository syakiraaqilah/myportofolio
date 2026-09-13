from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField, CharField
from main.models import Experience, Skill

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

def show_skills(request):
    category_order = Case(
        When(category='programming', then=Value(0)),
        When(category='dev_tools', then=Value(1)),
        When(category='design_editing', then=Value(2)),
        output_field=IntegerField(),
    )

    category_label = Case(
        When(category='programming', then=Value('Programming & Web')),
        When(category='design_editing', then=Value('Design & Editing')),
        When(category='dev_tools', then=Value('Dev Tools')),
        output_field=CharField(),
    )

    skills_list = Skill.objects.annotate(
        category_order=category_order,
        category_label=category_label,
    ).order_by('category_order', 'name')

    context = {
        "name": "Syakira",
        "skills_list": skills_list,
    }
    return render(request, "skills.html", context)
