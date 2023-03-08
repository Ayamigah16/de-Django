from django.urls import path
from .views import NewView, TutorCreate, TutorList, TutorDetail, TutorUpdate, TutorDeleteView

app_name = 'class_views'

urlpatterns = [
    path('about/', NewView.as_view(), name='about'),
    path('tutor/create/', TutorCreate.as_view(), name='tutor-create'),
    path('tutor/list/', TutorList.as_view(), name='tutor-list'),
    path('tutor/<int:pk>/', TutorDetail.as_view(), name='tutor-detail'),
    path('tutor/<int:pk>/update/', TutorUpdate.as_view(), name='tutor-update'),
    path('tutor/<int:pk>/delete/', TutorDeleteView.as_view(), name='tutor-delete')
    # other paths
]
