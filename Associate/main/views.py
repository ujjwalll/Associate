from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import csv
import pandas

# Create your views here.
def homepage(request):
	return render(request,"Home.html")

def login(request):
	if request.method == 'POST':
		data = pandas.read_csv('register.csv')
		user = request.POST.get('username')
		passs = request.POST.get('password')
		data1 = pandas.read_csv('profile.csv')
		names = data.email.tolist()
		password = data.password.tolist()
		first_name = data1.first_name.tolist()
		last_name = data1.last_name.tolist()
		email = data1.email.tolist()
		phone = data1.phone.tolist()
		country = data1.country.tolist()
		linkedin = data1.linkedin.tolist()
		telegram = data1.telegram.tolist()
		github = data1.github.tolist()
		roll = data1.roll.tolist()
		branch = data1.branch.tolist()
		batch = data1.batch.tolist()
		inter1 = data1.inter1.tolist()
		inter2 = data1.inter2.tolist()
		inter3 = data1.inter3.tolist()
		about = data1.about.tolist()
		for i in range(len(names)):
			if(names[i]==user):
				if(passs==password[i]):
					context={}
					context['fName'] = first_name[0]
					context['lName'] = last_name[0]
					context['email'] = email[0]
					context['phone'] = phone[0]
					context['country'] = country[0]
					context['linkedin'] = linkedin[0]
					context['telegram'] = telegram[0]
					context['github'] = github[0]
					context['roll'] = roll[0]
					context['branch'] = branch[0]
					context['batch'] = batch[0]
					context['inter1'] = inter1[0]
					context['inter2'] = inter2[0]
					context['inter3'] = inter3[0]
					context['about'] = about[0]
					print(context)
					return render(request,"profile.html",context)			
	return render(request,"login.html")

def register(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(name)
		print(email)
		row = [name, email, password]
		with open('register.csv','a') as fd:
			f = csv.writer(fd)
			f.writerow(row)	
		fd.close()
		return redirect('http://127.0.0.1:8000/detail/')
	return render(request,"register.html")

def transition(request):
	return render(request,"transition.html")

def detail(request):
	if request.method=='POST':
		Image=request.FILES['IMAGE']
		Im = FileSystemStorage()
		Im.save(Image.name, Image)
		print(Image.name)
		print(Image.size)
		Uploaded_CV=request.FILES['document']
		UC = FileSystemStorage()
		UC.save(Uploaded_CV.name, Uploaded_CV)
		print(Uploaded_CV.name)
		print(Uploaded_CV.size)
		first_name = request.POST.get('FirstNAME')
		last_name = request.POST.get('LastNAME')
		email = request.POST.get('Email')
		phone = request.POST.get('Phone')
		country = request.POST.get('country')
		linkedin = request.POST.get('Linkedin')
		telegram = request.POST.get('Telegram')
		github = request.POST.get('Github')
		roll = request.POST.get('roll')
		batch = request.POST.get('batch')
		branch = request.POST.get('branch')
		inter1 = request.POST.get('inter1')
		inter2 = request.POST.get('inter2')
		inter3 = request.POST.get('inter3')
		about = request.POST.get('about')
		print(email)
		row = [first_name,last_name,email,phone,country,linkedin,telegram,github,roll,batch,branch,inter1, inter2, inter3, about]
		with open('profile.csv','a') as fd:	
			f = csv.writer(fd)
			f.writerow(row)
		fd.close()
		return redirect('http://127.0.0.1:8000/avatar/')
	return render(request,"detail.html")

def avatar(request):
	return render(request,"avatar.html")

def profile(request):
	return render(request,"profile.html")
