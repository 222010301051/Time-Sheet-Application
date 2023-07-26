from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def att(request):
    return render(request,"mainpage.html")

def dash(request,pk):
    st=Employees.objects.get(id=pk)
    return render(request,"dashboard.html")

def login_val(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username,"***********%%%%%%%%%%%%%%%%%")
        # Check if the user exists in the model

        #import pdb;pdb.set_trace()
        try:
            user = Employees.objects.get(username=username)
        except Employees.DoesNotExist:
            return render(request, 'mainpage.html', {'error': 'Invalid username or password'})

        # Verify the password
        if user.password != password:
            return render(request, 'mainpage.html', {'error': 'Invalid username or password'})
        request.session['username'] = username
        return redirect('/dashboard/{0}'.format(user.id))

        # If the username and password match, redirect to another webpage
    else:
        return render(request, 'mainpage.html')

def submit_attendance(request):
    form_submitted=False
    if request.method == 'POST':
        username = request.session.get('username')
        try:
            employee = Employees.objects.get(username=username)
        except Employees.DoesNotExist:
            return render(request, 'mainpage.html', {'error': 'Invalid username'})

            # Retrieve the first name of the user
        first_name = employee.firstname
        print(first_name)
        name=first_name
        date = request.POST.get('date')
        shift = request.POST.get('shift')
        project_type = request.POST.get('project-type')
        login_time = request.POST.get('login-time')

        request.session['attendance_name'] = name
        form_submitted = True
        Attendance.objects.create(name=name,date=date,shift=shift,project_type=project_type,login_time=login_time)
        return render(request,'dashboard.html',{'form_submitted': form_submitted})

        # Create a new instance of the Attendance model
        # attendance = Attendance(
        #     date=date,
        #     shift=shift,
        #     project_type=project_type,
        #     login_time=login_time
        # )
        #
        # # Save the instance to the database
        # attendance.save()
        return redirect('dashboard')  # Redirect to the dashboard or any other page

    return render(request, 'dashboard.html')

def attendance_table(request):
    # stid = int([i for i in request.META.get('HTTP_REFERER').split("/") if i][-1])
    # uname = Employees.objects.get(id=stid).username
    # print(uname)
    name = request.session.get('attendance_name')
    attendance = Attendance.objects.filter(name=name)
    return render(request, 'attendance_data.html', {'attendance': attendance})