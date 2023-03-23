from django.contrib import admin
from django.urls import path
from crud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StudentView.as_view(),name='home'),
    path('insert/',StudentFormView.as_view(),name='insert'),
    path('<pk>/delete/',DeleteStudentView.as_view(),name='delete'),
    path('<pk>/update/',StudentEditView.as_view(),name='edit'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',SignUpView.as_view(),name='register'),
]
