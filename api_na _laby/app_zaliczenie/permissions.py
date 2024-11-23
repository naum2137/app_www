from rest_framework.permissions import BasePermission

class IsAdminGroup(BasePermission):
    """
    Uprawnienie sprawdzające, czy użytkownik należy do grupy Admin.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()


class IsUserGroup(BasePermission):
    """
    Uprawnienie sprawdzające, czy użytkownik należy do grupy User.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='User').exists()
