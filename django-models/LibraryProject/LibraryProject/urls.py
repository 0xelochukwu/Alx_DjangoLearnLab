from django.contrib import admin
from django.urls import path, include
from relationship_app import views  # import your home view

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]
