from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
from django.http import HttpResponse
from CRUDOperation.form import Empforms
def showemp(request):
    showall = EmpModel.objects.all()
    return render(request, 'index.html', {"data": showall})

from django.shortcuts import render, redirect
from CRUDOperation.models import EmpModel
from django.contrib import messages

def Insertemp(request):
    if request.method == "POST":
        if (
            request.POST.get('empname') and
            request.POST.get('email') and
            request.POST.get('occupation') and
            request.POST.get('mobile_no') and
            request.POST.get('salary') and
            request.POST.get('gender')
        ):
            saverecord = EmpModel(
                empname=request.POST.get('empname'),
                email=request.POST.get('email'),
                occupation=request.POST.get('occupation'),
                mobile_no=request.POST.get('mobile_no'),
                salary=request.POST.get('salary'),
                gender=request.POST.get('gender')
            )
            saverecord.save()
            messages.success(request, 'Employee ' + saverecord.empname + ' is saved successfully')
            return redirect('showemp')  # Redirect to another view
        else:
            messages.error(request, 'Invalid form data. Please fill in all fields.')
    return render(request, 'Insert.html')
def Editemp(request,id):
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'Edit.html',{"EmpModel":editempobj})
from django.shortcuts import render, redirect
from CRUDOperation.models import EmpModel


def updateemp(request, id):
    Updateemp = EmpModel.objects.get(id=id)
    form = Empforms(request.POST, instance=Updateemp)

    if request.method == 'POST':
        form = Empforms(request.POST, instance=Updateemp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully...')
            return render(request, 'Edit.html', {"EmpModel": Updateemp})

    form = Empforms(instance=Updateemp)  # Create a form with the instance data for GET requests
    return render(request, 'Edit.html', {"EmpModel": Updateemp})

def Delemp(request, id):
    delemployee = EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata = EmpModel.objects.all()
    return render(request, 'index.html', {"data": showdata})




