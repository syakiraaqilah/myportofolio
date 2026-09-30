from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project's name",
            "description": "Project's Description",
            "tech_stack": "Technology Used",
            "project_url": "Project's URL",
            "project_image_url": "Project's Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    class Meta: 
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience's name",
            "description": "Experience's Description",
            "category": "Experience's Category",
            "thumbnail": "Documentation",
            "started_at": "Start Date",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs = {
                    "placeholder": "Enter your experience",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs = {
                    "placeholder": "Describe your contribution",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date"
                },
                format="%Y-%m-%d"
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date"
                },
                format="%Y-%m-%d"
            ),
        }

        