
from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('entries/', views.EntryListView.as_view(), name='entry_list'),
    path('entries/new/', views.EntryCreateView.as_view(), name='entry_create'),
    path('entries/<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
    path('entries/<int:pk>/edit/', views.EntryUpdateView.as_view(), name='entry_edit'),
    path('entries/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
