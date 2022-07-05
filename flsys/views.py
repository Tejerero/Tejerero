from django.shortcuts import render, redirect
from django.http import HttpResponse
from flsys.models import Registration,CookingClass,Schedule,CheckoutInfo,Email,Rating

def MainPage(request):
	reglist = Registration.objects.all()
	return render(request, 'mainpage.html')

def ViewList(request,rId):
	cuiReg =  Registration.objects.get(id=rId)
	if request.method=='POST':
		CookingClass.objects.create(regid=cuiReg,cuisine=request.POST['cuisine'])
		return redirect(f'/flsys/{cuiReg.id}/SchedPage/')
	else:
		return render(request, 'listpage.html',{'cuiReg':cuiReg})

def NewList(request):
	vfirstname = request.POST['firstname']
	vsurname = request.POST['surname']
	vnumber = request.POST['number']
	vemail = request.POST['email']
	newReg = Registration.objects.create(firstname=vfirstname,
		surname=vsurname,
		number=vnumber,
		email=vemail)
	#return redirect('/flsys/viewlist_url/')
	return redirect(f'/flsys/{newReg.id}/')

def AddList(request, cuiReg):
	newReg =  Registration.objects.get(id=cuiReg)
	
	return redirect(f'/flsys/{newReg.id}/')

def SchedPage(request,rId):
	cuiReg =  Registration.objects.get(id=rId)
	cuisineClass=CookingClass.objects.filter(regid=rId)
	print (cuisineClass)
	if request.method=='POST':
		Schedule.objects.create(regid=cuiReg, 
			date=request.POST['date'],
			time=request.POST['time'],
			mode=request.POST['mode'])
		return redirect(f'/flsys/{cuiReg.id}/CheckoutPage/')
	else:
		return render(request, 'schedpage.html',{'cuiReg':cuiReg,'cuiClass':cuisineClass})

def CheckoutPage(request, rId):
	cuiReg =  Registration.objects.get(id=rId)
	cuisineClass=CookingClass.objects.filter(regid=rId)
	print (cuisineClass)
	schedClass=Schedule.objects.filter(regid=rId)
	print (schedClass)
	if request.method=='POST':
		CheckoutInfo.objects.create(regid=cuiReg,
			tickets=request.POST['tickets'], 
			payment=request.POST['payment'])
		return redirect(f'/flsys/{cuiReg.id}/Review/')
	else:
		return render(request, 'checkoutpage.html',{'cuiReg':cuiReg,
			'cuiClass':cuisineClass,
			'cuiSched':schedClass})

def Review(request, rId):
	cuiReg =  Registration.objects.get(id=rId)
	cuisineClass = CookingClass.objects.filter(regid=rId)
	print (cuisineClass)
	schedClass = Schedule.objects.filter(regid=rId)
	print (schedClass)
	checkoutMod = CheckoutInfo.objects.filter(regid=rId)
	print (schedClass)
	return render(request, 'transactpage.html', {'cuiReg':cuiReg, 
		'cuisineClass':cuisineClass, 'schedClass':schedClass, 'checkoutMod':checkoutMod})

def delete(request, rId):
	cuiReg =  Registration.objects.get(id=rId)
	cuiReg.delete()
	return redirect(f'/flsys/{None}/Review/')

def Review2(request):
	return render(request, 'transactpage.html')

def edit(request, rId):
	cuiReg = Registration.objects.get(id=rId)
	cuisineClass = CookingClass.objects.filter(regid=rId)
	print (cuisineClass)
	schedClass = Schedule.objects.filter(regid=rId)
	print (schedClass)
	checkoutMod = CheckoutInfo.objects.filter(regid=rId)
	print (schedClass)
	return render(request,'edit.html', {'cuiReg':cuiReg, 'cuisineClass':cuisineClass, 
		'schedClass':schedClass, 'checkoutMod':checkoutMod})

def update(request, rId):
	cuiReg = Registration.objects.get(id=rId)
	cuiReg.firstname = request.POST['firstname']
	cuiReg.surname = request.POST['surname']
	cuiReg.number = request.POST['number']
	cuiReg.email = request.POST['email']
	cuiReg.save()
	cuisineClass = CookingClass.objects.get(regid=rId)
	cuisineClass.cuisine = request.POST['cuisine']
	cuisineClass.save()
	schedClass = Schedule.objects.get(regid=rId)
	# schedClass.date = request.POST['date']
	schedClass.time = request.POST['time']
	schedClass.mode = request.POST['mode']
	schedClass.save()
	checkoutMod = CheckoutInfo.objects.get(regid=rId)
	checkoutMod.tickets = request.POST['tickets']
	checkoutMod.payment = request.POST['payment']
	checkoutMod.save()
	return redirect(f'/flsys/{cuiReg.id}/Review/')

def ContactUs(request):
	contact = Email.objects.all()
	if request.method == 'POST':
		Email.objects.create(contact_name=request.POST['contact_name'],
			contact_email=request.POST['contact_email'],
			message=request.POST['message'])
		return redirect(f'/flsys/ContactUs/')
	else:
		return render(request, 'contact.html',{'contact':contact})

def Home(request):
	return render(request, 'home.html')

def Recipes(request):
	return render(request, 'recipes.html')

def Breakfast(request):
	return render(request, 'breakfast.html')

def Mains(request):
	return render(request, 'mains.html')

def Sweets(request):
	return render(request, 'sweets.html')

def Healthy(request):
	return render(request, 'healthy.html')

def BreakfastPancakes(request):
	return render(request, 'breakfast_pancakes.html')

def BreakfastGarlicRice(request):
	return render(request, 'breakfast_garlicrice.html')

def BreakfastFrenchToast(request):
	return render(request, 'breakfast_toast.html')

def ChickenAdobo(request):
	return render(request, 'mains_adobo.html')

def FilipinoSpringRolls(request):
	return render(request, 'mains_lumpia.html')

def ChickenAfritada(request):
	return render(request, 'mains_afritada.html')

def HomemadeDonuts(request):
	return render(request, 'sweets_donut.html')

def Muffins(request):
	return render(request, 'sweets_muffin.html')

def Cupcakes(request):
	return render(request, 'sweets_cupcakes.html')

def Sandwiches(request):
	return render(request, 'healthy_sandwich.html')

def Salad(request):
	return render(request, 'healthy_salad.html')

def Pinakbet(request):
	return render(request, 'healthy_pinakbet.html')

def RatePancake(request):
	ratePancake = Rating.objects.all()
	if request.method == 'POST':
		Rating.objects.create(rate_name=request.POST['rate_name'], recipe_name=request.POST['recipe_name'],
			rating=request.POST['rating'], rate_date=request.POST['rate_date'])
		return redirect(f'/flsys/RatePancake/')
	else:
		return render(request, 'rate.html',{'ratePancake':ratePancake})

def deleteRating(request, id):
	ratePancake =  Rating.objects.get(id=id)
	ratePancake.delete()
	return redirect('/flsys/RatePancake/')

def editRating(request, id):
	ratePancake =  Rating.objects.get(id=id)
	context = {'ratePancake':ratePancake}
	return render(request,'editRate.html', context)

def updateRating(request, id):
	ratePancake =  Rating.objects.get(id=id)
	ratePancake.rate_name = request.POST['rate_name']
	ratePancake.recipe_name = request.POST['recipe_name']
	ratePancake.rating = request.POST['rating']
	ratePancake.save()
	return redirect('/flsys/RatePancake/')





	# cuisineClass=CookingClass.objects.filter(regid=rId)
	# print (cuisineClass)
	# schedClass=Schedule.objects.filter(regid=rId)
	# print (schedClass)
	# checkoutReg = CheckoutInfo.objects.filter(regid=rId)
	# print(checkoutReg)
	# return render(request, 'transactpage.html',{'cuiReg':cuisineClass,
	# 		'cuiReg':cuisineClass,
	# 		'cuiReg':schedClass,
	# 		'cuiReg':checkoutReg})

	'''
	vregid = Registration.objects.create(firstname="Jessica",surname="Jung")
	vcuisine = request.POST['mcuisine']
	CookingClass.objects.create(regid=vregid,cuisine=vcuisine)
	return redirect(f'/flsys/{vregid.id}/')
	'''