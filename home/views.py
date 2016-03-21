from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import ContactForm
from django.core.mail import send_mail
from .models import Home, Book

import datetime
def index(request):
	latest_question_list = {'title': 'Welcome to University Portal'}
	return render(request,'home/index.html',latest_question_list)
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> Its now %s </br> </body></html>" % now
	return HttpResponse(html)
def demo(request):
	values = request.META.items()
	values = sorted(values)
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

# For Search form and Response of search Request
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request,'home/search_results.html',{'books':books, 'query':q})
	return render(request, 'home/search_form.html', {'errors': errors})
# For Contact Form implemented in forms.py
def contact(request):
	if request.method =='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks')
	else:
		form = ContactForm()
	return render(request, 'home/contact_form.html',{'form':form })
