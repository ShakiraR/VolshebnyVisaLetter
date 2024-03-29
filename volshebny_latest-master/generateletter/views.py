from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from generateletter.models import Visaletters,Organization
from django.urls import reverse_lazy, reverse


#from translate import Translator

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)

# def users(request):
#     user_list = CustomUser.objects.all()
#     user_dict = {'userlist':user_list}
#     return render(request,'generateletter/users.html', user_dict)

@method_decorator(login_required, name='dispatch')
class list_view(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/view_visa_letter.html"
    #template_name = "generateletter/list.html"

@method_decorator(login_required, name='dispatch')
class list_view_copy(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/list_copy.html"

class gen_eng_visa(DetailView):
    model = Visaletters
    context_object_name = "detail_visa"
    template_name = "generateletter/gen_eng_visa.html"

class gen_rus_visa(DetailView):
    model = Visaletters
    context_object_name = "russian_visa"
    template_name = "generateletter/gen_rus_visa.html"

class gen_eng_voucher(DetailView):
    model = Visaletters
    context_object_name = "english_voucher"
    template_name = "generateletter/gen_eng_voucher.html"

class gen_rus_voucher(DetailView):
    model = Visaletters
    context_object_name = "russian_voucher"
    template_name = "generateletter/gen_rus_voucher.html"

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'generateletter/error_500.html', data)

def reports(request):
    data = { }
    return render(request, 'generateletter/reports.html', data)

# def generate_visa_letter(request):
#     data = { }
#     return render(request, 'generateletter/generate_visa_letter.html', data)    


def visa_letter_detail(request,visa_letter_id):
    translator= Translator(to_lang="ru")
    russian_visa = Visaletters.objects.get(pk=int(visa_letter_id))
    russian = {'Country': translator.translate(russian_visa.Country.name),
               'Routes_and_Places': translator.translate(russian_visa.Routes_and_Places),
               'hotels': translator.translate(russian_visa.hotels),
               }
    return render(request, 'generateletter/russian_visaletter.html', { 'russian_visa': russian_visa,'russian': russian })

def visagenerateform(request):
    OName=Organization.objects.all()
    
    data={'OName': OName}
    return render(request, 'generateletter/generate_visa_letter.html', data )     


def visa_letter_form_submit(request):
    if request.method == "POST":
          Name_of_Organization= Organization.objects.get(pk=request.POST['OrganizationName'])
          multiplicity=request.POST['multiplicity']
          no_passengers=request.POST['no_of_passenger']
          Country=request.POST['Country']
          entry_from = request.POST['entry_from']
          departure_to = request.POST['departure_to']
          Tourism = request.POST['Tourism']
          Visa_Letter_Number =request.POST['Visa_Letter_Number'] 
          Date_of_letter = request.POST['Date_of_letter']
          Routes_and_Places = request.POST['Routes_and_Places']
          hotels = request.POST['hotels']
          Payment_status = request.POST['Payment_status']
          amount = request.POST['amount']
          firstname_1 = request.POST['firstname_1']
          lastname_1 =request.POST['lastname_1']
          Passport_Number_1 = request.POST['Passport_Number_1']
          Date_Of_Birth_1 = request.POST['Date_Of_Birth_1']
          Sex_1 = request.POST['Sex_1']
          firstname_2 = request.POST['firstname_2']
          lastname_2 =request.POST['lastname_2']
          Passport_Number_2 = request.POST['Passport_Number_2']
          Date_Of_Birth_2 = request.POST['Date_Of_Birth_2']
          Sex_2 = request.POST['Sex_2']
          firstname_3 = request.POST['firstname_3']
          lastname_3 =request.POST['lastname_3']
          Passport_Number_3 = request.POST['Passport_Number_3']
          Date_Of_Birth_3 = request.POST['Date_Of_Birth_3']
          Sex_3 = request.POST['Sex_3']
          visaletter=Visaletters.objects.create(Organization_Details = Name_of_Organization,
                                                multiplicity = multiplicity, no_passengers=no_passengers, Country=Country, entry_from= entry_from,
                                                departure_to=departure_to,
                                                Tourism=Tourism,
                                                Visa_Letter_Number=Visa_Letter_Number,
                                                Date_of_letter = Date_of_letter,
                                                Routes_and_Places=Routes_and_Places,
                                                hotels=hotels,
                                                Payment_status=Payment_status,
                                                amount=amount,firstname_1=firstname_1,
                                                lastname_1=lastname_1,
                                                Passport_Number_1=Passport_Number_1,
                                                Date_Of_Birth_1 = Date_Of_Birth_1,
                                                Sex_1 = Sex_1,
                                                firstname_2=firstname_2,
                                                lastname_2=lastname_2,
                                                Passport_Number_2=Passport_Number_2,
                                                Date_Of_Birth_2=Date_Of_Birth_2,
                                                Sex_2=Sex_2,
                                                firstname_3=firstname_3,
                                                lastname_3=lastname_3,
                                                Passport_Number_3=Passport_Number_3,
                                                Date_Of_Birth_3=Date_Of_Birth_3,
                                                Sex_3=Sex_3)
                                            

    #return render(request, 'generateletter/generate_visa_letter.html') 
    return HttpResponseRedirect(reverse('Volshebny_visa_letter:generate_visa_letter'))                                           

