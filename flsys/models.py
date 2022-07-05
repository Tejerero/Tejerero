from django.db import models

class Registration(models.Model):
	firstname = models.CharField('Firstname', max_length=20)
	surname = models.CharField('Surname', max_length=20)
	number = models.CharField('Phone Number', max_length=11)
	email = models.EmailField('Client Email', default="")

	def __str__(self):
		return self.firstname + "" + self.surname

	class meta:
		db_table = "registration"
		verbose_name = 'Class Registration'

class CookingClass(models.Model):
	regid = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE, related_name='cuisines')
	cuisine = models.CharField(max_length=100)

	class meta:
		db_table = "cookclass"
		verbose_name = 'Class Cuisine'

class Schedule(models.Model):
	regid = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)
	date = models.DateField('Scheduled Date', auto_now_add = True)
	time = models.CharField('Scheduled Time', max_length=50)
	mode = models.CharField('Mode of Class', max_length=100)

	class meta:
		db_table = "sched"
		verbose_name = 'Class Schedule'

class CheckoutInfo(models.Model):
	regid = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)
	tickets = models.IntegerField('Number of Tickets', blank = True, null = True)
	payment = models.CharField('Payment Method',max_length=100)

	class meta:
		db_table = "checkoutinfo"
		verbose_name = 'Class Checkout Info'

class Email(models.Model):
	contact_name = models.CharField('Name', max_length=100)
	contact_email = models.EmailField('Email', default="")
	message = models.TextField('Message', default="")

class Rating(models.Model):
	rate_name = models.CharField('Name', max_length=100, default=None)
	recipe_name = models.CharField('Recipe Name', max_length=100)
	rate_date = models.DateField('Date', auto_now_add = True)
	rating = models.CharField('Rating', max_length=5)
