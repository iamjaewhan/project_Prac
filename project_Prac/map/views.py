from django.shortcuts import render

# Create your views here.

def showmap(request):
    home_address="경기도 화성시 동탄대로 6길 20"
    return render(request,'map_page.html',{'home_address':home_address})