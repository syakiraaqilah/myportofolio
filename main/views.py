from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField, CharField
from main.models import Experience, Skill, Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, ExperienceForm

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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project has been successfully added.")
        return redirect("main:show_projects")

    context = {
        "name": "Syakira",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Syakira",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been successfully deleted.")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been saved.")
            return redirect('main:show_projects')
    else:
        form = ProjectForm(instance=project)

    context = {
        "name": "Syakira",
        "form": form, 
        "project": project
        }
    return render(request, "projects_form.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Experience has been successfully added.")
        return redirect("main:show_experience")

    context = {
        "name": "Syakira",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Syakira",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has been successfully deleted.")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been saved.")
            return redirect('main:show_experience')
    else:
        form = ExperienceForm(instance=experience)

    context = {
        "name": "Syakira",
        "form": form, 
        "experience": experience
        }
    return render(request, "experience_form.html", context)