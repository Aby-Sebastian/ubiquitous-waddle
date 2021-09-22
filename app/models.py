from django.db import models

# Create your models here.
class Customer(models.Model):
	created = models.DateTimeField(auto_now=True)
	last_updated = models.DateTimeField(auto_now_add=True)
	url = models.CharField(max_length=150)
	short_url = models.CharField(max_length=20, unique=True)
	clicks = models.PositiveIntegerField(blank=True, null=True)
	total_clicks = models.IntegerField(default=0, blank=True, null=True)
	titles = models.CharField(max_length=200,default="No title found", blank=True, null=True)
	# qr_code = models.ImageField(upload_to='QR_codes',default='../static/images/young-man-avatar.jpg')
	

	def __str__(self):
		return self.short_url
	
	def increment_count(self):
		self.total_clicks+=1
		return self.total_clicks