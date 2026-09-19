from django.urls import path

from main.views import show_main, show_experience, show_skills, \
    create_project, show_projects, get_projects_json, delete_project, edit_project, \
    create_experience, get_experiences_json, delete_experience, edit_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path('projects/<uuid:project_id>/edit/', edit_project, name='edit_project'),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experiences_json, name="get_experiences_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path('experience/<uuid:experience_id>/edit/', edit_experience, name='edit_experience'),
    
]