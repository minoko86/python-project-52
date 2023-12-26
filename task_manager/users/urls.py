from django.urls import path, include

from task_manager.users import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.UsersShow.as_view(), name='users'),
    path('create/', views.UserRegister.as_view(), name='registration'),
    path('<int:pk>/update/', views.UserEdit.as_view(), name='edit'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='delete'),
]
