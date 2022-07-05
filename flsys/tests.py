from django.test import TestCase
#from flsys.views import MainPage
from flsys.models import Registration, CookingClass

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

class CreateListTest(TestCase):
	def test_responding_POST_request(self):
		resp = self.client.post('/flsys/newlist_url/', data={'firstname':'Taylor','surname':'Swift',
			'number':'09285764067','email':'taylor.swift@gmail.com'})
		self.assertEqual(Registration.objects.count(),1)
		newEntry = Registration.objects.first()
		self.assertEqual(newEntry.firstname, 'Taylor')

	def test_redirect_POST(self):
		resp = self.client.post('/flsys/newlist_url/', data={'firstname':'Taylor','surname':'Swift',
			'number':'09285764067','email':'taylor.swift@gmail.com'})
		self.assertEqual(Registration.objects.count(),1)
		newReg = Registration.objects.first()
		self.assertRedirects(resp,f'/flsys/{newReg.id}/')

class ViewTest(TestCase):
	def test_displays_for_each_reg(self):
		mregid1 = Registration.objects.create(firstname="Taylor",surname="Swift")
		CookingClass.objects.create(regid=mregid1, cuisine="italian")
		mregid2 = Registration.objects.create(firstname="Katy",surname="Perry")
		CookingClass.objects.create(regid=mregid2, cuisine="korean")
		resp = self.client.get(f'/flsys/{mregid1.id}/')
		self.assertContains(resp,'Italian')
		#self.assertNotContains(resp,'Korean')
		resp = self.client.get(f'/flsys/{mregid2.id}/')
		#self.assertNotContains(resp,'Italian')
		self.assertContains(resp,'Korean')

	def test_listview_uses_listpage(self):
		newReg = Registration.objects.create()
		resp = self.client.get(f'/flsys/{newReg.id}/')
		self.assertTemplateUsed(resp, 'listpage.html')

	def test_pass_list_to_template(self):
		reg1 = Registration.objects.create()
		passList = Registration.objects.create()
		reg2 = Registration.objects.create()
		response = self.client.get(f'/flsys/{passList.id}/')
		self.assertEqual(response.context['cuiReg'],passList)

class AddCuisineTest(TestCase):
	def xtest_add_POST_request_to_existing_Registrant(self):
		Reg111 = Registration.objects.create()
		exReg = Registration.objects.create()
		Reg222 = Registration.objects.create()
		self.client.post(f'/flsys/{exReg.id}/addList/',data={'cuisine':'Asian'})
		self.assertEqual(CookingClass.objects.count(), 1)
		newList = CookingClass.objects.first()
		self.assertEqual(newList.cuisine, 'Asian')
		self.assertEqual(newList.regid, exReg)

	def test_redirects_to_list_view(self):
		Reg111 =Registration.objects.create()
		exReg = Registration.objects.create()
		Reg222 = Registration.objects.create()
		Reg333 = Registration.objects.create()
		response = self.client.post(f'/flsys/{exReg.id}/addList/', data={'cuisine':'French'})
		self.assertRedirects(response, f'/flsys/{exReg.id}/')

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		newReg1 = Registration()
		newReg1.firstname = 'Oprah'
		newReg1.surname = 'Dioquino'
		newReg1.number = '09124565676'
		newReg1.email = 'oprah.dioquino@gsfe.tupcavite.edu.ph'
		newReg1.save()
		newReg2 = Registration()
		newReg2.firstname = 'Angela'
		newReg2.surname = 'Velasco'
		newReg2.number = '09678456378'
		newReg2.email = 'angela.dioquino@gsfe.tupcavite.edu.ph'
		newReg2.save()
		listItem = CookingClass()
		listItem.regid = newReg1 
		listItem.regid = newReg2
		listItem.baking = 'Baking'
		listItem.save()
		savedReg = Registration.objects.all()
		self.assertEqual(savedReg.count(), 2)
		savedReg1 = savedReg[0]
		savedReg2 = savedReg[1]
		self.assertEqual(savedReg1.firstname, 'Oprah')
		self.assertEqual(savedReg2.firstname, 'Angela')
		self.assertNotEqual(savedReg1.cuisines, listItem)
		self.assertNotEqual(savedReg2.cuisines, listItem)
		savedCookClass = CookingClass.objects.first()
		self.assertEqual(savedCookClass, listItem)



'''		listBaking = CookingClass(cuisine='Baking')
		listBaking.save()
		newReg1.cuisines.add(listBaking)
		newReg1.cuisines.all()
		listPastry = CookingClass(cuisine='Pastry')
		listPastry.save()
		newReg1.cuisines.add(listPastry)
		newReg1.cuisines.all()
#----------------------
		listAsian = CookingClass(cuisine='Asian')
		listAsian.save()
		newReg2 = Registration()
		newReg2.firstname = 'Steph'
		newReg2.surname = 'Camarinta'
		newReg2.number = '09878671243'
		newReg2.email = 'steph.camarinta@gsfe.tupcavite.edu.ph'
		newReg2.save()
		listAsian.regid.add(newReg2)
		listAsian.regid.all()
		newReg3 = Registration()
		newReg3.firstname = 'Angela'
		newReg3.surname = 'Velasco'
		newReg3.number = '09987123567'
		newReg3.email = 'angela.velasco@gsfe.tupcavite.edu.ph'
		newReg3.save()
		listAsian.regid.add(newReg3)
		listAsian.regid.all()
		'''
'''
		listItem1 = CookingClass()
		listItem1.regid.set() = newReg1 
		listItem1.baking = 'Baking'
		listItem1.save()
		listItem2 = CookingClass()
		listItem2.regid.set() = newReg1 
		listItem2.pastry = 'Pastry'
		listItem2.save()
		savedReg = Registration.objects.first()
		self.assertEqual(savedReg, newReg1)
		savedCookClass = CookingClass.objects.all()
		self.assertEqual(savedCookClass.count(), 2)
		savedCookClass1 = savedCookClass[0]
		savedCookClass2 = savedCookClass[1]
		self.assertEqual(savedCookClass1.cookclass, 'Baking')
		self.assertEqual(savedCookClass2.cookclass, 'Pastry')
		self.assertEqual(savedCookClass1.regid, newReg1)
		self.assertEqual(savedCookClass2.regid, newReg1)

		listItem3 = CookingClass()
		listItem3.asian = 'Asian'
		listItem3.save()
		newReg2 = Registration()
		newReg2.cuisines = listItem3
		newReg2.firstname = 'Steph'
		newReg2.surname = 'Camarinta'
		newReg2.number = '09878671243'
		newReg2.email = 'steph.camarinta@gsfe.tupcavite.edu.ph'
		newReg2.save()
		newReg3 = Registration()
		newReg3.cuisines = listItem3
		newReg3.firstname = 'Angela'
		newReg3.surname = 'Velasco'
		newReg3.number = '09987123567'
		newReg3.email = 'angela.velasco@gsfe.tupcavite.edu.ph'
		newReg3.save()
		savedCui = CookingClass.objects.first()
		self.assertEqual(savedCui, listItem3)
		savedNewReg = Registration.objects.all()
		self.assertEqual(savedNewReg.count(), 2)
		savedNewReg2 = savedNewReg[0]
		savedNewReg3 = savedNewReg[1]
		self.assertEqual(savedNewReg2.firstname, 'Steph')
		self.assertEqual(savedNewReg3.firstname, 'Pastry')
		self.assertEqual(savedNewReg2.cuisines, listItem3)
		self.assertEqual(savedNewReg3.cuisines, listItem3)

	'''
		



	#def test_saving_retrieving_list(self):
	#	entry1 = Registration()
	#	entry1.firstname = 'Oprah'
	#	entry1.surname = 'Dioquino'
	#	entry1.number = '09124565676'
	#	entry1.email = 'oprah.dioquino@gsfe.tupcavite.edu.ph'
	#	entry1.save()
	#	entry2 = Registration()
	#	entry2.firstname = 'Jennie'
	#	entry2.surname = 'Kim'
	#	entry2.number = '09123673867'
	#	entry2.email = 'jennie.kim@gsfe.tupcavite.edu.ph'
	#	entry2.save()
	#	items = Registration.objects.all()
	#	self.assertEqual(items.count(), 2)
	#	items1 = items[0]
	#	items2 = items[1]
	#	self.assertEqual(items1.firstname, 'Aprilyn')
	#	self.assertEqual(items2.firstname, 'Jennie')
