from django.contrib import admin
from django.urls import path
from cars import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list),
    path('cars/<int:id>', views.car_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)