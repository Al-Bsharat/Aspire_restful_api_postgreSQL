from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        if request.user.is_superuser:
            return True
        return True if request.method in permissions.SAFE_METHODS else obj.id == request.user.id
