from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsModerator(BasePermission):
    """
    Модератор:
    - is_staff=True
    - может читать, изменять и удалять чужие продукты
    - не может создавать продукты (POST запрещён)
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if not request.user.is_staff:
            return False

        # Запрещаем POST
        if request.method == "POST":
            return False

        return True

    def has_object_permission(self, request, view, obj):
        # Модератор может редактировать/удалять чужие продукты
        if request.method in SAFE_METHODS:
            return True
        return True
