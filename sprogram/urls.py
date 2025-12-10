from django.urls import path
from .views import ProgramStudiListAPIView,ProgramStudyDetailAPIView

urlpatterns = [
    # URL: /api/akademik/program-studi/
    path('', ProgramStudiListAPIView.as_view(), name='program-studi-list-api'),
    path('<int:pk>/', ProgramStudyDetailAPIView.as_view(), name='program-study-detail-api'), 
]