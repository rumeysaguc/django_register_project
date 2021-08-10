from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404




def main(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, "index.html")

def site(request):
    site_info = SiteInfo.objects.all().last()
    return {'site_info': site_info}

def menu(request):
    header_menu_list = Menu.objects.filter(menu_location_id=1).translate(
        request.LANGUAGE_CODE).order_by('alignment')
    footer_menu_list = Menu.objects.filter(menu_location_id=2).translate(
        request.LANGUAGE_CODE).order_by('alignment')
    return {'header_menu_list': header_menu_list, 'footer_menu_list': footer_menu_list, }

def test(request):
    return render(request, "apps/competitions/competition_details.html")
