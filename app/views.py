from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages # Messages framework
from .forms import CustomLinkForm
from .models import *

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = CustomLinkForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Form submitted successfully')
			return reverse('index')
		else:
			messages.error(request, "Form is invalid.")
	else:
		form = CustomLinkForm()
	data = Customer.objects.all()
	context = {
		'form': form,
		'data': data,
		}
	return render(request,'index.html', context)


def uid():
     uid = str(uuid.uuid4())[:5]
     return uid

def go(request,pk):
    # try:
    #     url_details=Links.objects.get(short_url=pk)
    # except :
    #     print('DoesNotExist')
    obj = get_object_or_404(Customer, short_url=pk)
    return redirect(obj.url)


def save_data(request):
	if request.method == 'POST':
		lid = request.POST.get('sid')
		if lid == '':
			form = CustomLinkForm(request.POST)
		else:
			sid = Customer.objects.get(pk=lid)
			form = CustomLinkForm(request.POST, instance=sid)

		#uid = str(uuid.uuid4())[:5]
		# print("here-----------------",lid)

		short_url = request.POST['short_url']
		if short_url == '':
			short_url = uid()
			if Customer.objects.filter(short_url=short_url).exists():
				short_url=uid()
		print(form.errors)
		if form.is_valid():
			lid = request.POST.get('sid')
			value=request.POST['url']
			print(lid,value,short_url,sep=" ")
			print("----------------------Start--------------------------")
			# title = scrape_title(value)
			
			
			expiration = timezone.now() + timezone.timedelta(days=30)
			try:
				title_data = title_parser(value)
			except :
				title_data = "No page title available"

			# QR code generator
		    # if request.method == "POST":
			# factory = qrcode.image.svg.SvgImage
			'''
			url_to_QR = f"localhost:8000/page/{short_url}"
			img = qrcode.make(url_to_QR)'''
			# stream = BytesIO()
			'''img.save(f"./media/QR_codes/{short_url}.png")'''

			# svg = stream.getvalue().decode()

			if lid == '':
				print('yes')
				custom_url = Customer(url=value,short_url=short_url, titles=title_data)
			else:
				print('no')

				custom_url = Customer(id=lid,url=value,short_url=short_url, titles=title_data)
			custom_url.save()
			cust = Customer.objects.values().order_by('-id')
			# print(cust)
			customer_values = list(cust)
			return JsonResponse({'status': 'save', 'customer_values':customer_values})
		else:
			return JsonResponse({'status': 0})
