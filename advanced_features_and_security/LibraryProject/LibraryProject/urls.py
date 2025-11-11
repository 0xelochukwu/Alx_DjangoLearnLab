from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # ✅ include app urls
    path('', RedirectView.as_view(url='/relationship/')),     # optional redirect
]
