from django.urls import path, include

urlpatterns = [
    path('comptes/', include('django.contrib.auth.urls'))    
]