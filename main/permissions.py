from rest_framework.permissions import BasePermission, SAFE_METHODS
from main.utils import is_editor

edit_perm = None

class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects and experiences."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )

class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Only the portfolio owner or an editor can change projects and experiences."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and is_editor(request.user)
        )

