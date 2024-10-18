from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class Viewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.groups.filter(name='Viewer').exists():
            return True
        raise PermissionDenied(detail="Vous n'avez pas les permissions nécessaires pour modifier ces données.")
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.utilisateur == request.user
