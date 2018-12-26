from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    #main^ main
    url(r'^$', views.main, name='main'),
    #product
    url(r'^product_view$', views.product_view, name='product_view'),
    #request_contact
    url(r'^request_contact$', views.request_contact, name='request_contact'),
    #sozdaniye abonenta
    #url(r'^abonent/create$', views.abonent_create, name='abonent_create'),
    #prosmotr
    #url(r'^abonent/view$', views.abonent_view, name='abonent_view'),
    #redaktirovaniye
    #url(r'^abonent/edit$', views.abonent_edit, name='abonent_edit'),
    #poisk abonenta
    #url(r'^abonent/search$', views.abonent_search, name='abonent_search'),

    #dobavleniye remarki
    #url(r'^add_remark$', views.add_remark, name='add_remark'),
    #dobavleniye excel fila
    #url(r'^add_excel$', views.add_excel, name='add_excel'),
    #url(r'^receive_data$', views.receive_data, name='receive_data'),
]