from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Project, Experience

def clean_plain_text(value, label):
    cleaned = strip_tags(value).strip()
    if not cleaned:
        raise ValidationError(f"{label} cannot be empty or only contain HTML tags.")
    return cleaned

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
                    "placeholder": "Tell us about your project",
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
                    "placeholder": "https://github.com/username/project",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        return clean_plain_text(self.cleaned_data["title"], "Project's name")

    def clean_tech_stack(self):
        return clean_plain_text(self.cleaned_data["tech_stack"], "Technology used")

    def clean_description(self):
        return clean_plain_text(self.cleaned_data["description"], "Description")

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

    def clean_title(self):
        return clean_plain_text(self.cleaned_data["title"], "Experience's name")

    def clean_description(self):
        return clean_plain_text(self.cleaned_data["description"], "Description")

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

    def clean(self):
        cleaned = super().clean()
        started_at, ended_at = cleaned.get("started_at"), cleaned.get("ended_at")
        if started_at and ended_at and ended_at < started_at:
            self.add_error("ended_at", "End date cannot be earlier than the start date.")
        return cleaned