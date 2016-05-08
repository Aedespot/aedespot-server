from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from aedespot.core.models import Report 


class ReportSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Report


class ReportViewSet(viewsets.ModelViewSet):
	queryset = Report.objects.all()
	serializer_class = ReportSerializer

	http_method_names = ['post']


router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)