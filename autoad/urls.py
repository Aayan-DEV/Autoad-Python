from django.contrib import admin
from django.urls import path
from autoadapp.views import index, contact, about, pricing, privicypolicy, terms, signup, login

urlpatterns = [
    path("", index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('pricing/', pricing, name='pricing'),
    path('privicy-policy/', privicypolicy, name='privicy-policy'),
    path('terms-and-conditions/', terms, name='terms-and-conditions'),
    path('login', login, name='login'),
    path('sign-up', signup, name='sign-up'),
    path('admin/', admin.site.urls),

]
