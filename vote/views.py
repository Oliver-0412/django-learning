from django.shortcuts import render
#from django.http import HttpResponse
from vote.models import Subject,Teacher
from django.shortcuts import redirect

# Create your views here.
def show_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})
def show_teachers(request):
    """显示指定学科的老师"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')