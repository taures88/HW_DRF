from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    info = "не модератор!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.moderator:
            return True
        return False


class IsBuyer(BasePermission):
    info = 'не владелец!'

    def has_object_permission(self, request, view, obj):
        if obj.buyer == request.user or request.user.is_superuser:
            return True
        return False