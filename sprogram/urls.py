from django.urls import path
from .views import ProgramStudiListAPIView

urlpatterns = [
    # URL: /api/akademik/program-studi/
    path('', ProgramStudiListAPIView.as_view(), name='program-studi-list-api'),
]