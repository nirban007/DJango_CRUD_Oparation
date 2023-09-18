from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
def showemp(request):
    showall = EmpModel.objects.all()
    return render(request, 'index.html', {"data": showall})

def Insertemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and  request.POST.get('email') and  request.POST.get('occupation') and  request.POST.get('mobile_no') and  request.POST.get('salary') and  request.POST.get('gender'):
            saverecord = EmpModel
            saverecord.empname = request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.mobile_no = request.POST.get('mobile_no')
            saverecord.salary = request.POST.get('salary')
            saverecord.gender = request.POST.get('gender')
            messages.success(request, 'Employee'+saverecord.empname+' Is saved successfully')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')
        
        