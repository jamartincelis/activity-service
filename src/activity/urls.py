from django.urls import path
from activity.views import ActivityList, ActivityDetail

urlpatterns = [
    path('', ActivityList.as_view(), name="list_create"),
    path('<str:pk>/', ActivityDetail.as_view(), name="detail")
]
