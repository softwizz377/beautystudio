from django.urls import path, include
from beauty import views


app_name="beauty"
urlpatterns = [
     path('home',views.Homepageview.as_view()),
     path('about',views.Aboutpageview.as_view()),
	 path('services',views.Servicespageview.as_view()),
     path('gallery',views.Gallerypageview.as_view()),
	 path('blog',views.Blogpageview.as_view()),
	 path('Product',views.product_list),
	 path('offers',views.Offerspageview.as_view()),
	 path('contact',views.Contactpageview.as_view()),
	 path('insertcontact',views.contact),
	 path('appointment',views.Appointmentpageview.as_view()),
	 path('insertappointment',views.appointment),
	 path('feedback',views.Feedbackpageview.as_view()),
	 path('insertfeedback',views.feedback),
	 path('natural',views.Naturalpageview.as_view()),
	 path('mehndi',views.Mehndipageview.as_view()),
	 path('hair',views.Hairpageview.as_view()),
	 path('pedicure',views.Pedicurepageview.as_view()),
	 path('bridal',views.Bridalpageview.as_view()),
   	 path('servicedetail/<int:id>',views.servicedetail),
	 path('FAQs/',views.FAQspageview.as_view()),
	 path('servicedetail/<int:id>',views.servicedetail),
	 path('career',views.Careerpageview.as_view()),
	 path('insertcareer',views.career),
	 path('cartdetail/',views.cartdetailview.as_view()),
	 path('detail/',views.cartdetailview.as_view()),

	]
