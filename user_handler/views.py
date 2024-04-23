from django.shortcuts import render,redirect
from user_handler.models import *
from pycompiler.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registerstu(request):
    if request.method == "POST":
        first_name = request.POST.get('stu_first_name')
        last_name = request.POST.get('stu_last_name')
        username = request.POST.get('stu_username')
        rollno = request.POST.get('rollno')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already Exists')
            return redirect('/register-student/')

        user = User.objects.create(
            first_name=  first_name,
            last_name = last_name,
            username = username,
            is_staff = False
        )

        user.set_password(password)
        user.save()

        student = Student.objects.create(
            user = user,
            rollno = rollno
        )

        student.save()

        messages.info(request, 'Student Account created')
        return redirect('/register-student/')



    return render(request, 'registerstu.html')

def registerfac(request):
    if request.method == "POST":
        first_name = request.POST.get('fac_first_name')
        last_name = request.POST.get('fac_last_name')
        username = request.POST.get('fac_username')
        # rollno = request.POST.get('rollno')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'User already Exists')
            return redirect('register-faculty')

        user = User.objects.create(
            first_name=  first_name,
            last_name = last_name,
            username = username,
            is_staff = True
        )

        user.set_password(password)
        user.save()

        faculty = Faculty.objects.create(
            user = user,
            # rollno = rollno
        )

        faculty.save()

        messages.info(request,'Faculty Account Created')

        return redirect('/register-faculty/')



    return render(request, 'registerfac.html')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
                
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Incorrect Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/questions')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required
def new_test(request):
    return render(request, 'new_test.html')

@login_required
def create_qs(request):
    if request.method == 'POST':
        qs_title = request.POST.get('qs_title')
        question_text = request.POST.get('question')
        new_question = Questions.objects.create(qs_title=qs_title, question=question_text)
        return redirect('/questions/') 

    return render(request, 'new_test.html')

@login_required
def allques(request):
    queryset = Questions.objects.all()
    context = {'Questions': queryset}
    return render(request, 'questions.html', context)

@login_required
def attempted(request, id):

    code = Code.objects.filter(qs_id=id)
    user_ids = code.values_list('user_id', flat=True)
    stu = Student.objects.filter(user__id__in=user_ids)
    qs = Questions.objects.get(qs_id = id)
    tc = TestCase.objects.all()
    return render(request, "attempted_questions.html", {'Questions': qs, 'TestCase': tc, 'Code': code, 'Student': stu})

@login_required
def new_testcase(request):
    return render(request, 'new_testcase.html')

@login_required
def create_testcase(request):
    if request.method == 'POST':
        qs_id = request.POST.get('qs_id')
        testcase_input = request.POST.get('testinput')
        expected_output = request.POST.get('testoutput')
        question = Questions.objects.get(pk=qs_id)
        TestCase.objects.create(qs_id=question, testcase_input=testcase_input, expected_output=expected_output)
        return redirect('/questions/')

    return redirect('/')

@login_required
def sq(request):
    if request.method == 'POST':
        qs_id = request.POST.get('id')
        return redirect('/ques/'+str(qs_id))