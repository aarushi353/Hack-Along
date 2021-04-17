from django.contrib import admin
from django.urls import path,include
from userapp import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('users.urls'))
]