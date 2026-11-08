from django.utils import timezone
EDITOR_GROUP = "Editor"

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name=EDITOR_GROUP).exists()

def can_edit_content(user):
    return user.is_authenticated and (user.is_superuser or is_editor(user))

def format_month_year(value):
    if value is None:
        return None
    if timezone.is_aware(value):
        value = timezone.localtime(value)
    return value.strftime("%b %Y")
    