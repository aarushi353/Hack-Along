from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
from userapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('users.urls'))
=======
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('users.urls')),
>>>>>>> 55372badcc0b8708ffd225ff84aa22ef8ae76018
]
