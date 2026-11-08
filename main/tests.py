from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project, Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=timezone.now(),
        )

        self.skill = Skill.objects.create(
            name="Python",
            category="programming",
            icon_url="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
        )
  
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')


    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_dates_in_model(self):
        started_at = timezone.make_aware(datetime(2025, 1, 15, 9, 0))
        ended_at = timezone.make_aware(datetime(2025, 6, 30, 17, 0))
        self.experience.started_at = started_at
        self.experience.ended_at = ended_at
        self.experience.save()

        self.assertEqual(self.experience.started_at, started_at)
        self.assertEqual(self.experience.ended_at, ended_at)
        self.assertFalse(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, "BASE_EXPERIENCES_ENDPOINT")
        self.assertContains(response, "PATCH")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experiences have been added yet")

    def test_experience_search_query_is_rendered(self):
        response = self.client.get(reverse("main:show_experience"), {"title": "Assistant"})
        self.assertEqual(response.context["title_query"], "Assistant")
        self.assertContains(response, 'value="Assistant"')

    def test_project_page_and_empty_state(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, "BASE_PROJECTS_ENDPOINT")
        self.assertContains(response, "No projects have been added yet")

    def test_owner_sees_add_and_edit_modals(self):
        owner = User.objects.create_superuser(username="owner", password="test-password", email="owner@example.com")
        self.client.force_login(owner)
        project_response = self.client.get(reverse("main:show_projects"))
        experience_response = self.client.get(reverse("main:show_experience"))
        self.assertContains(project_response, "add-project-modal")
        self.assertContains(project_response, "edit-project-modal")
        self.assertContains(experience_response, "add-experience-modal")
        self.assertContains(experience_response, "edit-experience-modal")

    def test_project_search_query_is_rendered(self):
        response = self.client.get(reverse("main:show_projects"), {"title": "Portfolio"})
        self.assertEqual(response.context["title_query"], "Portfolio")
        self.assertContains(response, 'value="Portfolio"')

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(self.skill.category, "programming")
        self.assertEqual(self.skill.icon_url, "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg")

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skills"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")
        self.assertContains(response, self.skill.name)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))
        self.assertContains(response, "Belum ada skill yang ditambahkan.")

    def test_project_model(self):
        project = Project.objects.create(title="Portfolio", description="Site", tech_stack="Django")
        self.assertEqual(str(project), "Portfolio")
