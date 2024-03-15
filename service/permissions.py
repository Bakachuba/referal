from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить доступ только владельцу объекта.
        return obj.user == request.user
