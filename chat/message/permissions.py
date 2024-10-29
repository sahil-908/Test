from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    """
    Custom permission to only allow super admins to change or assign user permissions.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a superuser
        return request.user and request.user.is_authenticated and request.user.is_superuser
