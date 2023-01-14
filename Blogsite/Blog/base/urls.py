from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('category/',views.category,name="category"),
    path('about/',views.about,name="about"),
    path('post/<int:pk>/',views.single_post,name="single_post"),
    path('category-posts/<int:pk>/',views.category_post,name="category_post"),
    path('blogs',views.blogs_page,name="blogs"),
    path('emailsub/',views.emailsub,name="email"),
    path('contactsub/',views.contact,name="contact"),

    
    
]