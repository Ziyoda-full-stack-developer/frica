from django.urls import path
from .views import computers, contact, index, mans_clothes, womans_clothes, komputerDetail, watchDetail, koylakDetail, womanforDetail, smallDetail

urlpatterns = [
    path('computers/', computers, name="computers"),
    path('contact/',  contact,   name="contact"),
    path('',    index,     name="index"),
    path('mans_clothes/', mans_clothes,  name="mans_clothes"),
    path('womans_clothes/', womans_clothes, name="womans_clothes"),
    path('komputer/<slug:komputer>', komputerDetail, name='komputerDetail'),
    path('watch/<slug:watch>/', watchDetail, name='watchDetail'),
    path('koylak/<slug:koylak>/', koylakDetail, name='koylakDetail'),
    path('womanfor/<slug:womanfor>/', womanforDetail, name='womanforDetail'),
    path('small/<slug:small>/', smallDetail, name='smallDetail')
]