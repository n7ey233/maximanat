"""
maximanat.pythonanywhere.com
vlad911as123

steps to deploy:
add allowed url to settings
git clone
add virtualenv
start virtualenv
pip upgrade
install django
install requests
pythonanywhere:
    add virualenv
    add wsgi
"""

from django.shortcuts import render

from .models import *
from .forms import *
import requests

def send_notification_telegram(text):
    telegram_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg' #token telegi
    #moi id telegi '405347178'
    #id telegi antona '548383851'
    chat_id = '405347178' #id v telege dlya otpravki
    url = "https://api.telegram.org/bot"+telegram_token+"/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.get(url,headers={'Content-Type': 'application/json' }, json=data)

def main(request):
    #if nothing
    page_data = dict()
    return_page = 'app/main.html'
    if request.GET.get('q', '') != '':#if not nothing
        q = request.GET.get('q').lower()
        if q == 'about':
            return_page = 'app/about.html'
        elif q == 'services':
            return_page = 'app/services.html'
        elif q == 'contact':
            return_page = 'app/contact.html'
        elif q == 'product_list':
            return_page = 'app/product_list.html'
            page_data['categories'] = category.objects.all()
            try:
                current_category = category.objects.get(name = request.GET.get('cat', ''))
                page_data['current_category'] = current_category
                page_data['products'] = product.objects.filter(category = current_category)
            except:
                page_data['products'] = product.objects.all()
        page_data['nav_bar'] = q
    #tut tol'ko otobrazhaem vse posti iz lichnogo dnevnika
    return render(request, return_page, page_data)
def product_view(request):
    return_page = 'app/404.html'
    page_data = dict()
    if request.GET.get('q', '') != '':#if not nothing
        try:
            obj = product.objects.get(pk=request.GET.get('q', ''))
            page_data['obj'] = obj 
            page_data['categories'] = category.objects.all()
            return_page = 'app/product_view.html'
        except: None
    return render(request, return_page, page_data)
def request_contact(request):
    if request.method == 'POST':
        try:
            try:
                text = 'Поступила заявка\n'
                text+= '\nИмя: '+str(request.POST['product_name'])
            except:
                text = 'Пришло обращение. \n'
            text+= '\nИмя: '+str(request.POST['name'])
            text+= '\nНомер: '+str(request.POST['phone'])
            text+= '\nПочта: '+str(request.POST['email'])
            text+= '\nСообщение: '+str(request.POST['message'])
            print(request.POST)
            send_notification_telegram(text)
        except: None
        return render(request, 'app/thanks.html', {})
    else:
        return render(request, 'app/404.html', {})





'''
vibrat' kak budet viglyadet' main
teksta dlya main
teksta dlya about
teksta dlya services
teksta dlya contacts
teksta dlya 404
teksta dlya thanks
цветовая палитра? могу белую или серую захуярить
список категорий
список продукции разделенной по категориям
как будет дополняться информация о товаре? эксель или мб вручную добавляется единицы товара?
редактируются ли категории? категории с подкатегориями?
нужно ли редактирование какой-либо информации на сайте? к примеру продукция или какие-либо текста?
нотификация в тг только для отправки обращения?


slugify product url ?q=
contact notify
'''