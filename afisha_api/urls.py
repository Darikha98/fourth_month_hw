
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/movies/', views.film_list_view),
    path('api/v1/movies/<int:id>/', views.film_detail_view),
]
