from django.urls import path
from .views import LeagueListView, LeagueDetailView, LeagueCreateView, LeagueUpdateView, LeagueDeleteView
from . import views


urlpatterns = [
    path('', LeagueListView.as_view(), name='tracker-home'),
    path('league/<int:pk>/', LeagueDetailView.as_view(), name='league-detail'),
    path('league/new/', LeagueCreateView.as_view(), name='league-create'),	
    path('league/<int:pk>/update', LeagueUpdateView.as_view(), name='league-update'),
    path('league/<int:pk>/delete', LeagueDeleteView.as_view(), name='league-delete'),
    path('about/', views.about, name='tracker-about')
]