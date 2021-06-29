from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('specs/', views.specs_index, name='specs_index'),
    path('specs/<int:spec_id>/', views.specs_show, name='specs_show'),
    path('specs/create/', views.SpecCreate.as_view(), name='specs_create'),
    path('specs/<int:pk>/update/', views.SpecUpdate.as_view(), name='specs_update'),
    path('specs/<int:pk>/delete/', views.SpecDelete.as_view(), name='specs_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('gear/', views.gear_index, name='gear_index'),
    path('gear/<int:gear_id>', views.gear_show, name='gear_show'),
    path('gear/create/', views.GearCreate.as_view(), name='gear_create'),
    path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name='gear_update'),
    path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name='gear_delete'),
    path('search/', views.search, name='search' ),
    path('results/', views.results, name='results'),
]