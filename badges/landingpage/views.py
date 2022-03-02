import email
from django.shortcuts import redirect, render
from landingpage.models import Badge, Student
import datetime

# Create your views here.
def home(request):
    return render(request,'index.html')

def show_badges(request):
    #new_id = User.objects.order_by('id').last().id+1
    year = str(datetime.date.today().year%100)
    #username = f'{year}MLU{new_id:0004}'
    if request.method == 'POST':
        
        badge_name = request.POST['badge_name']
        badge_description = request.POST['badge_description']
        badge_image = request.FILES['badge_image']
        user_emails = request.POST['user_emails']

        new_badge = Badge(
            badge_name = badge_name,
            badge_description = badge_description,
            badge_image = badge_image
        )
        new_badge.save()

        all_emails = [email.strip() for email in user_emails.split(',')]
        for email in all_emails:
            new_student = Student(
                student_email = email,
                student_badge = Badge.objects.filter(badge_name=badge_name)[0]
            )
            new_student.save()
        #user_joined_date = datetime.date.today()
    students = Student.objects.all()
    data = {
        'students' : students
    }
    return render(request, 'all_badges.html', data)

def verify(request):
    if request.method=='GET':
        try:
            badge_name = request.GET.get('name')
            email_id = request.GET.get('email')
            student_badge = Badge.objects.filter(badge_name=badge_name)[0]
            students = Student.objects.filter(student_badge=student_badge,student_email=email_id)
            if len(students)>0:
                data = {
                    'students':students
                }
                return render(request, 'all_badges.html', data)
            else:
                return render(request, 'no_data.html')
        except:
            return redirect('/badges')

    return redirect('/badges')
