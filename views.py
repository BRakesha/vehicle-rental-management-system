from django.shortcuts import render,redirect
from .data import *
from .models import CarModel

# Create your views here.

def home(request):
    data=CarModel.objects.all()
    return render(request,'home.html',{'data':data})


def admin_dash(request):
    data=CarModel.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        brand=request.POST['brand']
        price_per_day=request.POST['price_per_day']
        fuel_type=request.POST['fuel_type']
        seats=request.POST['seats']
        transmission=request.POST['transmission']
        image=request.POST['image'] 
        availability = request.POST.get('availability') == 'on'
        CarModel.objects.create(name=name,
                                brand=brand,
                                price_per_day=price_per_day,
                                fuel_type=fuel_type,
                                transmission=transmission,
                                image=image,
                                seats=seats,
                                availability=availability)
        return redirect('home')
    return render(request,'adhome.html',{'data':data})

def delete(request,id):
    data=CarModel.objects.get(id=id)
    data.delete()
    return redirect('admin')

def edit(request,id):
    data=CarModel.objects.get(id=id)
    if request.method == 'POST':
        data.name=request.POST['name']
        data.brand=request.POST['brand']
        data.price_per_day=request.POST['price_per_day']
        data.fuel_type=request.POST['fuel_type']
        data.seats=request.POST['seats']
        data.transmission=request.POST['transmission']

        print(request.POST['availability'])

        if request.POST['availability'] == 'True':
            data.availability=True
        else:
            data.availability=False
        data.save()
        return redirect('admin')
    return render(request,'edit.html',{'data':data})

def aval(request):
    data=CarModel.objects.filter(availability=True)
    return render(request,'aval.html',{'data':data})

def book(request,id):
    data=CarModel.objects.get(id=id)
    data.availability=False
    data.save()
    return redirect('home')

def search(request):
    if request.method=='POST':
        if request.POST['name']:
            name=request.POST['name']
            seats=request.POST['seats']
            data=CarModel.objects.filter(name=name,seats=seats)
            return render(request,'search.html',{'data':data})
    return render(request,'search.html')



def insert(data):
    for car in data:
        CarModel.objects.create(name=car['name'],
                                brand=car['brand'],
                                price_per_day=car['price_per_day'],
                                fuel_type=car['fuel_type'],
                                transmission=car['transmission'],
                                image=car['image'],
                                seats=car['seats'],
                                availability=car['availability'])

# insert(vehicles)

