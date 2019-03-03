from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views import generic

from EntrepriseManager.models import Entreprise


def index(request):
    return HttpResponse("Vous êtes sur une page WEB !")

"""class ListEmployeView(generic.ListView):
    template_name = "EntrepriseManager/employe_list.html"
    context_object_name = 'employes'

    def get_queryset(self):
        return Employe.objects.all()

class ViewEmployeView(generic.DetailView):
    template_name = 'EntrepriseManager/employe_details.html'
    model = Employe


def employe_create(request):
    entreprises = Entreprise.objects.all()
    if 'nom' in request.POST:
        try:
            entreprise = Entreprise.objects.get(id=request.POST['entreprise'])
            employe = Employe.objects.create(nom=request.POST['nom'],entreprise=entreprise)
        except (Entreprise.DoesNotExist):
            context = {
                'errormessage': "L'entreprise que vous avez selectionné n'existe pas !",
                'entreprises': entreprises
            }
            return render(request,"EntrepriseManager/employe_create.html",context=context)
        except (KeyError):
            context = {
                'errormessage': "Veuillez remplir tout les champs !",
                'entreprises': entreprises
            }
            return render(request, "EntrepriseManager/employe_create.html", context=context)
        return HttpResponseRedirect(reverse('employe',args=(employe.id,)))

    context = {
        'errormessage': "AH",
        'entreprises': entreprises
    }
    return render(request,"EntrepriseManager/employe_create.html",context=context)

"""

def view_entreprise(request,id):
    entreprise = get_object_or_404(Entreprise,pk=id)
    context = {
        'entreprise':entreprise
    }
    return render(request,'EntrepriseManager/entreprise_details.html',context=context)