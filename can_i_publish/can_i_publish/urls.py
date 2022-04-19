from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('libel/', include('libel.urls')),
    path('admin/', admin.site.urls),
    # default to libel, for now
    path('', include('libel.urls')),
]
