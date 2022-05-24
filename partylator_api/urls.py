
from django.contrib import admin
from django.urls import path, include

api = [
    path('auth/', include('auth.urls')),
    # path('core/', include('core.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api))
]
