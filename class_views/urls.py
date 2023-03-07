from django.urls import path
from .views import NewView, TutorCreate, TutorList, TutorDetail, TutorUpdate

app_name = 'class_views'

urlpatterns = [
    path('about/', NewView.as_view(), name='about'),
    path('tutor/create/', TutorCreate.as_view(), name='tutor_create'),
    path('tutor/list/', TutorList.as_view(), name='tutor_list'),
    path('tutor/<int:pk>/', TutorDetail.as_view(), name='tutor_detail'),
    path('tutor/<int:pk>/update/', TutorUpdate.as_view(), name='tutor_update'),
    # other paths
]
