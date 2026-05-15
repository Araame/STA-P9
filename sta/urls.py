from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import NoteCreateView, NoteListView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),

    path('', views.home, name='home' ),
    path('/notes', NoteListView.as_view(), name='list_notes'),
    path('/add/', NoteCreateView.as_view(), name='add'),
    path('/<int:pk>/modify/', NoteUpdateView.as_view(), name='modify'),
    path('/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete'),
  

]