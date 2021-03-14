from django.shortcuts import render,redirect
from testapp.models import Library
from .forms import SForm


# Create your views here.

def fetch_details(request):
    student_list=Library.objects.all()
    my_dict={"student_list":student_list}
    return render(request,"fetch.html",my_dict)


def insert_details(request):
    form=SForm()

    if request.method=="POST":
        form=SForm(request.POST)
    
        if form.is_valid():
            form.save()
        return redirect("home")

    my_dict={"form":form}
    return render(request,'insert.html',my_dict)


def delete_details(request,id):
    student=Library.objects.get(id=id)
    student.delete()
    return redirect("home")



def update_details(request,id):
    student=Library.objects.get(id=id)

    if request.method=="POST":
        form=SForm(request.POST,instance=student)
    
        if form.is_valid():
            form.save()
        return redirect("home")  
    my_dict={"student":student}
    return render(request,'update.html',my_dict)