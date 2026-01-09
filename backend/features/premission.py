from rest_framework.permissions import BasePermission
from .services import is_feature_allowed

class FeaturePermission(BasePermission):
    feature_name = None

    def has_permission(self, request, view):
        if not self.feature_name:
            return True
        return is_feature_allowed(request.user, self.feature_name)