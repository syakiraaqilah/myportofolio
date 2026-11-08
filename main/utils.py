from django.utils import timezone

def format_month_year(value):
    if value is None:
        return None
    if timezone.is_aware(value):
        value = timezone.localtime(value)
    return value.strftime("%b %Y")
    