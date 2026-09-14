from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Skill


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
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, self.experience.started_at.strftime("%b %Y"))
        self.assertContains(response, "Present")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_completed_experience_page_displays_end_date(self):
        self.experience.started_at = timezone.make_aware(datetime(2025, 1, 15, 9, 0))
        self.experience.ended_at = timezone.make_aware(datetime(2025, 6, 30, 17, 0))
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Jan 2025 -")
        self.assertContains(response, "Jun 2025")
        self.assertNotContains(response, "Present")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

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
