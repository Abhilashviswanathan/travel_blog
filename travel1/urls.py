from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),  
    path('blog/', views.blog_list, name='blog'),  
    path('contact/', views.contact, name='contact'),    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('addblog/', views.addblog, name='addblog'),
    path('delete/<int:id>/', views.delete, name='delete'),  
    path('blog_details/<int:id>/', views.blog_detials, name='blog_details'),
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('edit/<int:id>/addblog', views.edit, name='edit'),  
    path('profile/edit/', views.edit_profile, name='edit_profile'), 
] 

