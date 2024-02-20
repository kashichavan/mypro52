from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel
# Create your views here.
def home(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        print(request.POST)
        if form.is_valid():

            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            StudentModel.objects.create(name=name,age=age)
    f=StudentForm()
    return render(request,'home.html',context={'form':f})

