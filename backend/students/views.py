from rest_framework.views import APIView
from rest_framework.response import Response
from features.permissions import FeaturePermission

class GradesPermission(FeaturePermission):
    feature_name = 'grades'

class StudentGradesView(APIView):
    permission_classes = [GradesPermission]

    def get(self, request, id):
        return Response({"grades": []})