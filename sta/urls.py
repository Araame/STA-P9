from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import HomeView, NoteCreateView, NoteListView, NoteDeleteView, NoteUpdateView, AllNotesListView, NoteDetailView

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),

    path('', HomeView.as_view(), name='home' ),
    path('/notes', NoteListView.as_view(), name='list_notes'),
    path('/notes/all', AllNotesListView.as_view(), name='all_notes'),
    path('<int:pk>/detail', NoteDetailView.as_view(), name='detail'),
    path('/add/', NoteCreateView.as_view(), name='add'),
    path('/<int:pk>/modify/', NoteUpdateView.as_view(), name='modify'),
    path('/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete'),
    path('/summarize/',views.week_summarize, name='week_summarize' ),
]