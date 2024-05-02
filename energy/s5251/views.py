from django.http import JsonResponse
from rest_framework import serializers, viewsets

class PQCurveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQCurve
        fields = ['voltage', 'capacity', 'pf_droop']

class PQCurveViewSet(viewsets.ModelViewSet):
    queryset = PQCurve.objects.all()
    serializer_class = PQCurveSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"item": "created"})