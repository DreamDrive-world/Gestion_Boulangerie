"""
URL configuration for GesBoulangerie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
{% comment %}  HYOFANG LUY MARSHALL
 DJOMATCHOUA WAMENI Ange Manuela
 
 DJEUMO LEUNA Jemima {% endcomment %}
 """
 
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from  GestionBoulangerie.views import *  


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",index, name="index"),
    
    path("client",page_Client, name="page_Client"),
    
    path("Melanges",page_Melanges, name="page_Melanges"),
    
    path("Pains",page_Pains, name="page_Pains"),
    
    path("Commandes",page_Commande, name="page_Commande"),
    
    path("Factures",page_Facture, name="page_Facture"),
    
    path("Approvisionnement",page_Approvisionnement, name="page_Approvisionnement"),
    
    path("ajout_client",add_client, name="add_client"),
    
    path("supprimer_client/<int:myid>",delete_client, name="delete_client"),
    
    path("modifier_client/<int:myid>",edit_client, name="edit_client"),
    
    path("update_client/<int:myid>",update_client, name="update_client"),
    
    path("ajout_melange",add_melange, name="add_melange"),
    
    path("supprimer_melange/<int:myid>",delete_melange, name="delete_melange"),
    
    path("modifier_melange/<int:myid>",edit_melange, name="edit_melange"),
    
    path("update_melange/<int:myid>",update_melange, name="update_melange"),
    
    path("ajout_pain",add_pain, name="add_pain"),
    
    path("supprimer_pain/<int:myid>",delete_pain, name="delete_pain"),
    
    path("modifier_pain/<int:myid>",edit_pain, name="edit_pain"),
    
    path("update_pain/<int:myid>",update_pain, name="update_pain"),
    
    path("ajout_commande",add_commande, name="add_commande"),
    
    path("supprimer_commande/<int:myid>",delete_commande, name="delete_commande"),
    
    path("modifier_commande/<int:myid>",edit_commande, name="edit_commande"),
    
    path("ajout_approvionnement",add_approvisionnement, name="add_approvisionnement"),
    
    path("supprimer_approvisionnement/<int:myid>",delete_approvisionnement, name="delete_approvisionnement")
    
    # path("update_commande/<int:myid>",update_commande, name="update_commande"),
]
