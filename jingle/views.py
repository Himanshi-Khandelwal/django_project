from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from jingle.models import Category
from jingle.forms import CategoryForm
from jingle.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")



def index(request):
	context = RequestContext(request)
	category_list = Category.objects.order_by('-name')[:5]
	context_dic = {'boldmessage': "I am bold font from the context"}
	context_dict = {'categories': category_list}

	for category in category_list:
		category.url = category.name.replace(' ', '_')

	return render_to_response('index.html', context_dict, context)

def category(request, category_name_url):
	context = RequestContext(request)
	category_name = category_name_url.replace('_', ' ')
	context_dict = {'category_name': category_name}
	try:
		category = Category.objects.get(name=category_name)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render_to_response('category.html', context_dict, context)

def add_category(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = CategoryForm(request.POST)
 	 	if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()
	return render_to_response('add_category.html', {'form': form}, context)


def register(request):
	context = RequestContext(request)
	registered = False

	#profile = request.user.UserProfile
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()
			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()


	return render_to_response(
			'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context)


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/jingle/')
			else:
				return HttpResponse("Your Rango account is disabled.")

		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('login.html', {}, context)

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/jingle/')
