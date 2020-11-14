from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import assignment_dates, homework

def get(request):
    dates = assignment_dates.objects.all()
    tasks = homework.objects.all()
    return render(request, 'distant/tasks.html', {'tasks': tasks, 'dates': dates})

def get_info(request):
    return render(request, 'distant/info.html', {})

def test(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            mail = form.cleaned_data['email']
            send_mail(subject, content, 'milovanovv1@mail.ru', [mail],)
            messages.success(request, 'Письмо отправлено!')

            return redirect('test')
        else:
            messages.success(request, 'Письмо не отправлено!')
    else:
        form = SendForm()

    return render(request,'distant/test.html', {'form':form,})

def happy(request):
    return render(request, 'distant/happy.html')