from django.contrib import admin
from beauty.models import contact,feedback,appointment, category,service, FAQs, career, Product
# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
	list_display=('firstname','lastname','phone','city',)
	
@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
	list_display=('experience','name','email','phone','message',)

	
@admin.register(appointment)
class appointmentAdmin(admin.ModelAdmin):
	list_display=('name','email','date','time','appointmentfor','appointmentplace',)
	
	
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
	pass

@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
	pass

@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
	pass
	
@admin.register(career)
class careerAdmin(admin.ModelAdmin):
	list_display=('name','email','gender','address','phone','sentfile',)


@admin.register(Product)	
class ProductAdmin(admin.ModelAdmin):
    pass
   # prepopulated_fields = {'slug': ('name',)}


#admin.site.register(Product, ProductAdmin)
