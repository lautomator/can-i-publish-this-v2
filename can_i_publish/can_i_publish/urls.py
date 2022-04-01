from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('libel.urls')),
    path('libel/', include('libel.urls')),
    path('admin/', admin.site.urls),
]
