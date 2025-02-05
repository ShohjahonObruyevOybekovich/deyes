from rest_framework import permissions

from accounts.models import UserRole


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            admin_role = UserRole.objects.get(user=request.user).role.name

        except UserRole.DoesNotExist:
            return False
        return admin_role.lower() == 'admin'


