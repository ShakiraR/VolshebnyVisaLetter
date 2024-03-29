from django.urls import include, path, re_path
from django.contrib import admin
from generateletter import views

app_name = 'Volshebny_visa_letter'

urlpatterns = [
    path("", views.list_view.as_view(), name="view_visa_letter"),
   # path("list", views.list_view.as_view(), name="list"),
    path("list_copy", views.list_view_copy.as_view(), name="listcopy"),
    # path("users", views.users, name="users"),
    path("reports", views.reports, name="reports"),
    path("visa_letter_form_submit", views.visa_letter_form_submit, name="visa_letter_form_submit"),
    path("generate_visa_letter", views.visagenerateform, name="generate_visa_letter"),
    path("russian_visa/<int:pk>", views.gen_rus_visa.as_view(), name="gen_rus_visa"),
    path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),
    path("english_voucher/<int:pk>", views.gen_eng_voucher.as_view(), name="gen_eng_voucher"),
    path("russian_voucher/<int:pk>", views.gen_rus_voucher.as_view(), name="gen_rus_voucher"),
    re_path(r'^visa_letters/(?P<visa_letter_id>\d+)/$',views.visa_letter_detail,name='visa'),
]

admin.site.index_title = "Welcome, Lets Manage Visa Letters and Vouchers With Ease"
admin.site.site_header = "Volshebny Admin"
admin.site.site_title = "Volshebny Admin Portal"