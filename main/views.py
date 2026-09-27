from django.db.models import Case, When, Value, IntegerField, CharField
from main.models import Experience, Skill, Project
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, ExperienceForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied   
from django.contrib.auth.decorators import permission_required
import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session yet / Cookie not found')
    context = {
        "name": "Syakira",
        "npm": "2506541622",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A CS student who navigates the tech world line by line, constantly"
            " on an endless quest to master new tech. Fueled by curiosity,"
            " driven by code, and always ready to debug any challenge."
        ),
        "last_login": last_login,
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")

def delete_project(request, project_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been successfully deleted.")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@permission_required("main.edit_project", login_url="/login/", raise_exception=True)
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
                raise PermissionDenied
    
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

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(experiences_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
                raise PermissionDenied
    
    experience = get_object_or_404(Experience, id=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has been successfully deleted.")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@permission_required("main.edit_experience", login_url="/login/", raise_exception=True)
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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Syakira",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response


    context = {
        "name": "Syakira",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

