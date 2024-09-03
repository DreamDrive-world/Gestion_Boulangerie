from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from .models import *

# HYOFANG LUY MARSHALL
# DJOMATCHOUA WAMENI Ange Manuela
# 
# DJEUMO LEUNA Jemima


def index(request):
    
    Client_liste = Client.objects.all()
    
    context = {
        "Client_liste" : Client_liste
    }
    
    return render(request, 'home.html',context)


# Client----------------------------------------------------------------------

def add_client(request):
    if request.method=='POST':
        try:
            with transaction.atomic():
                name = request.POST['name']
                address = request.POST['address']
                ville = request.POST['ville']
                Client1 = Client(nom_cli= name, adr_cli= address, ville_cli=ville)
                Client1.save()
                messages.info(request, "Client crée avec success")
        except:
            # En cas d'erreur, le rollback se fait automatiquement
            messages.error(request, "Erreur lors de la création du client")
    else:
        pass
    
    Client_liste = Client.objects.all()
    
    context = {
        "Client_liste" : Client_liste
    }
    
    return render(request, 'clients.html',context)




def delete_client(request, myid):
    client = Client.objects.get(id_cli = myid)
    client.delete()
    messages.info(request, "Client supprimé avec success")
    return redirect(page_Client)


def edit_client(request, myid):
    client = Client.objects.get(id_cli = myid)
    Client_liste = Client.objects.all()
    context = { 
        "client" : client,
        "Client_liste" : Client_liste
    }
    

    return render(request, 'clients.html',context)


def update_client(request, myid):
    client = Client.objects.get(id_cli = myid)
    client.nom_cli = request.POST['name']
    client.ville_cli = request.POST['ville']
    client.adr_cli = request.POST['address']
    client.save()
    
    messages.info(request, "Client modifier avec success")
    return redirect(page_Client)


def page_Client(request):
    Client_liste = Client.objects.all()
    
    context = {
        "Client_liste" : Client_liste
    }
    
    return render(request, 'clients.html',context)






# Melange----------------------------------------------------------------------

def page_Melanges(request):  
    melange_liste = Melange.objects.all()
    context = {
        "melange_liste" : melange_liste
    }
    
    return render(request, 'Melanges.html',context)


def add_melange(request):
    if request.method=='POST':
        try:
            with transaction.atomic():
                desc = request.POST['description']
                melange = Melange(description= desc)
                melange.save()
                messages.info(request, "melange crée avec success")
        except:
            # En cas d'erreur, le rollback se fait automatiquement
            messages.error(request, "Erreur lors de la création du melange")
    else:
        pass
    
    melange_liste = Melange.objects.all()
    
    context = {
        "melange_liste" : melange_liste
    }
    
    return render(request, 'Melanges.html',context)

def delete_melange(request, myid):
    melange = Melange.objects.get(id_melange = myid)
    melange.delete()
    messages.info(request, "melange supprimé avec success")
    return redirect(page_Melanges)


def edit_melange(request, myid):
    melange = Melange.objects.get(id_melange = myid)
    melange_liste = Melange.objects.all()
    context = { 
        "melange" : melange,
        "melange_liste" : melange_liste
    }
    

    return render(request, 'Melanges.html',context)


def update_melange(request, myid):
    melange = Melange.objects.get(id_melange = myid)
    melange.description = request.POST['description']
    melange.save()
    
    messages.info(request, "melange modifier avec success")
    return redirect(page_Melanges)


# Pains----------------------------------------------------------------

def page_Pains(request):  
    melange_liste = Melange.objects.all()
    pain_liste = Pain.objects.all()
    
    context = {
        "pain_liste" : pain_liste,
        "melange_liste" : melange_liste
    }
    
    return render(request, 'Pains.html',context)


def add_pain(request):
    if request.method=='POST':
        try:
            with transaction.atomic():
                desc = request.POST['description']
                prix_pain = request.POST['prix_pain_ht']
                id_melange1 = request.POST['melange']
                melange_bon = Melange.objects.get(id_melange = id_melange1)
                pain = Pain(description= desc, prix_pain_ht= prix_pain, melange=melange_bon)
                pain.save()
                messages.info(request, "Pain crée avec success")
        except:
            # En cas d'erreur, le rollback se fait automatiquement
            messages.error(request, "Erreur lors de la création du Pain")
    else:
        pass
    
    pain_liste = Pain.objects.all()
    
    context = {
        "pain_liste" : pain_liste
    }
    
    return render(request, 'Pains.html',context)

def delete_pain(request, myid):
    pain = Pain.objects.get(id_pain = myid)
    pain.delete()
    messages.info(request, "Pain supprimé avec success")
    return redirect(page_Pains)


def edit_pain(request, myid):
    pain = Pain.objects.get(id_pain = myid)
    pain_liste = Pain.objects.all()
    context = { 
        "pain" : pain,
        "pain_liste" : pain_liste
    }
    

    return render(request, 'Pains.html',context)


def update_pain(request, myid):
    pain = Pain.objects.get(id_pain = myid)
    pain.description = request.POST['description']
    pain.save()
    
    messages.info(request, "pain modifier avec success")
    return redirect(page_Pains)


# Commande ------------------------------------------------------------------

def page_Commande(request):  
    pain_liste = Pain.objects.all()
    clients_liste = Client.objects.all()
    commande_liste = Livraison.objects.all()
    
    context = {
        "pain_liste" : pain_liste,
        "clients_liste" : clients_liste,
        "commande_liste" :commande_liste
    }
    
    return render(request, 'Commandes.html',context)


def add_commande(request):
    if request.method=='POST':
        try:
            with transaction.atomic():
                quantite = request.POST['quantite']
                date_livraison1 = request.POST['date_livraison']
                id_client = request.POST['client']
                id_pain1 = request.POST['pain']
                client_bon = Client.objects.get(id_cli = id_client)
                Pain_bon = Pain.objects.get(id_pain = id_pain1)
                livraison = Livraison(client= client_bon, pain= Pain_bon, nombre_pains=quantite, date_livraison=date_livraison1)
                livraison.save()
                messages.info(request, "Commande crée avec success")
        except:
            # En cas d'erreur, le rollback se fait automatiquement
            messages.error(request, "Erreur lors de la création de la commande")
    else:
        pass
    
    commande_liste = Livraison.objects.all()
    pain_liste = Pain.objects.all()
    clients_liste = Client.objects.all()
    
    context = {
        "commande_liste" : commande_liste,
        "clients_liste" : clients_liste,
        "pain_liste" : pain_liste
    }
    
    return render(request, 'Commandes.html',context)

def delete_commande(request, myid):
    commande = Livraison.objects.get(id = myid)
    commande.delete()
    messages.info(request, "commande supprimé avec success")
    return redirect(page_Commande)


def edit_commande(request, myid):
    commande = Livraison.objects.get(id = myid)
    commande_liste = commande.objects.all()
    context = { 
        "commande" : commande,
        "commande_liste" : commande_liste
    }
    

    return render(request, 'Commandes.html',context)


# def update_commande(request, myid):
#     commande = Livraison.objects.get(id = myid)
#     commande.nombre_pains = request.POST['quantite']
#     date_livraison1 = request.POST['date_livraison']
#     commande.save()
    
#     messages.info(request, "commande modifiée avec success")
#     return redirect(page_Commande)


# Approvisionnement------------------------------------------------------------


def page_Approvisionnement(request):  
    Approvisionnement_liste = Approvisionnement.objects.all()
    Approvisionnement_listeU = Approvisionnement.objects.values('semaine_appro').distinct()
    
    melange_liste = Melange.objects.all()
    
    context = {
        "Approvisionnement_liste" : Approvisionnement_liste,
        "Approvisionnement_listeU" : Approvisionnement_listeU,
        "melange_liste" : melange_liste,
    }
    
    return render(request, 'Approvisionnements.html',context)



def add_approvisionnement(request):
    if request.method=='POST':
        try:
            with transaction.atomic():
                quantite = request.POST['quantite']
                date_livraison1 = request.POST['date_livraison']
                date_obj = datetime.strptime(date_livraison1, '%Y-%m-%d')
                week_number = date_obj.isocalendar()[1]
                id_melange1 = request.POST['melange']
                melange_bon = Melange.objects.get(id_melange = id_melange1)
                approvisionnement = Approvisionnement(melange= melange_bon, semaine_appro= week_number, quantite_melange=quantite)
                approvisionnement.save()
                messages.info(request, "Approvisionnement crée avec success")
        except:
            # En cas d'erreur, le rollback se fait automatiquement
            messages.error(request, "Erreur lors de la création de l'Approvisionnement")
    else:
        pass
    
    Approvisionnement_liste = Approvisionnement.objects.all()
    Approvisionnement_listeU = Approvisionnement.objects.values('semaine_appro').distinct()
    melange_liste = Melange.objects.all()
    
    context = {
        "Approvisionnement_liste" : Approvisionnement_liste,
        "Approvisionnement_listeU" : Approvisionnement_listeU,
         "melange_liste" : melange_liste,
    }
    
    return render(request, 'Approvisionnements.html',context)



def delete_approvisionnement(request, myid):
    approvisionnement = Approvisionnement.objects.get(id = myid)
    approvisionnement.delete()
    messages.info(request, "Approvisionnement supprimé avec success")
    return redirect(page_Approvisionnement)



# Facture------------------------------------------------------------------


def page_Facture(request):  
    commande_liste = Livraison.objects.all()

    context = {
        "commande_liste" : commande_liste,
    }
    
    return render(request, 'factures.html',context)