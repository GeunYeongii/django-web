from django.shortcuts import HttpResponse, get_object_or_404, redirect,render
import random
from .models import Coffee
from .forms import CoffeeForm


# Create your views here.
def index(request) :
    #return HttpResponse("Hello World!!")
    name = "Michael"
    number = random.randint(1,100)
    nums = [1,2,3,4,5]
    return render(request, 'index.html', {"my_num" : number, "my_name" : name, "my_list" : nums})

def coffee_view(request) :
    coffee_all = Coffee.objects.all()
    form = CoffeeForm()
    # objects.get() or objects.filter()... 으로 특정행만 가져오기도 가능
    return render(request,'coffee.html',{"coffee_list":coffee_all, "coffee_form":form}) 

def create(request) :
    # 만약 request가 POST라면 POST를 바탕으로 Form을 완성하고,
    # Form이 유효하면 -> 저장하라!
    if request.method == "POST" :
        print(request.POST)
        form = CoffeeForm(request.POST) # 완성된 Form 전송
        if form.is_valid() : # 채워진 Form이 유효한다면
            form.save() # Form내용을 Model저장한다.
            return redirect('/coffee')
    else :
        form = CoffeeForm()
    return render(request,'coffee.html', {'coffee_form':form})


def update(request,coffee_id) :
    coffee = Coffee.objects.get(id=coffee_id)
    form = CoffeeForm(request.GET)
    if form.is_valid() :
        coffee.name = form.cleaned_data['name']
        coffee.price = form.cleaned_data['price']
        form.save()
    return render(request,'coffee.html', {'coffee_form' : form})


def delete(request, coffee_id) :
    coffee = Coffee.objects.get(id=coffee_id)
    coffee.delete()
    return redirect('/coffee')