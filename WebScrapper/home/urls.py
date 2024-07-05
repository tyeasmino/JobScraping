from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    # path("about_us", views.about_us, name='about_us'),  
    path("about_site", views.about_site, name='about_site'),
    path("faq", views.faq, name='faq'),
    # path("contact", views.contact, name='contact'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),   
    path("logout", views.logoutUser, name='logout'), 
]    