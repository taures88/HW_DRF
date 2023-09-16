from rest_framework.permissions import BasePermission

from users.models import UserRoles


"""класс проверки входа модератора"""


class IsModerator(BasePermission):
    info = "не модератор!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.moderator:
            return True
        return False


"""класс проверки входа владельца(пользователя)"""


class IsBuyer(BasePermission):
    info = 'не владелец!'

    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user or request.user.is_superuser