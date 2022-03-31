from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from activity.models import Activity
from activity.serializers import ActivitySerializer

class ActivityList(ListCreateAPIView):
    """
    Permite listar o crear payments.
    """
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.kwargs['user'], project=self.kwargs['project'])

class ActivityDetail(RetrieveUpdateAPIView):
    """
    Permite obtener o actualizar payments.
    """
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.kwargs['user'], project=self.kwargs['project'], pk=self.kwargs['pk'])
