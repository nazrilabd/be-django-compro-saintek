from django.urls import path
from .views import HeaderContentDetailAPIView, HeaderContentListAPIView

urlpatterns = [
    # 1. URL List (GET semua postingan)
    path('', HeaderContentListAPIView.as_view(), name='headercontent-list-api'),
    
    # 2. URL Detail (GET satu postingan berdasarkan ID)
    # <int:pk> menunjukkan bahwa bagian ini adalah Primary Key (ID) dan harus berupa integer
    path('<int:pk>/', HeaderContentDetailAPIView.as_view(), name='headercontent-detail-api'), 
]