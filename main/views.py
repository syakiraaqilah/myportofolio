from django.db.models import Case, When, Value, IntegerField, CharField
from main.models import Experience, Skill, Project
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, ExperienceForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied   
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_POST
from django.utils import timezone
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
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Syakira",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

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
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Syakira",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()
    
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "started_at": format_month_year(experience.started_at),
                "ended_at": format_month_year(experience.ended_at),
                "is_ongoing": experience.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

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

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only owner can add project."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project has been successfully added.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only owner can add experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience has been successfully added.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def format_month_year(value):
    if value is None:
        return None
    if timezone.is_aware(value):
        value = timezone.localtime(value)
    return value.strftime("%b %Y")
