import sys
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pycompiler.models import *
from django.contrib import messages
from user_handler.models import *

@login_required
def index(request, id):
    queryset = Questions.objects.get(qs_id = id)
    tc = TestCase.objects.get(qs_id = queryset)
    context = {'Questions':queryset, 'TestCase' : tc}
    return render(request, 'index.html', context)

@login_required
def runcode(request, id):

    if request.method == "POST":
        codeareadata = request.POST.get('codearea')
        input_part = request.POST.get('inputarea')
        y = input_part
        if y is not None:
            input_part = input_part.replace("\n"," ").split(" ")
            def input():
                a = input_part[0]
                del input_part[0]
                return a

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)  
            sys.stdout.close()
            sys.stdout = original_stdout  
            output = open('file.txt', 'r').read()
            tc = TestCase.objects.get(qs_id = id)

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    if str(tc.expected_output).strip() == str(output).strip():
        messages.info(request, 'Sample Testcase passed')
    else:
        messages.error(request, 'Sample testcase failed')
    queryset = Questions.objects.get(qs_id = id)
    tc = TestCase.objects.get(qs_id = queryset)
    context = {'Questions': queryset, 'TestCase': tc, "code": codeareadata, "input": y, "output": output}

    return render(request , 'index.html',context )

@login_required
def submitgg(request, id):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        input_part = request.POST['inputarea']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') 
            exec(codeareadata) 
            sys.stdout.close()
            sys.stdout = original_stdout 
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

        tc = TestCase.objects.get(qs_id = id)
        tempbool = False
        if str(tc.expected_output).strip() == str(output).strip():
            messages.info(request, 'Sample Testcase passed')
            tempbool = True
        else:
            messages.error(request, 'Sample testcase failed')
            tempbool = False
        code  = Code.objects.create(
            code = codeareadata,
            output = output,
            user = request.user,
            tc_pass = tempbool,
            qs_id = id 
        )
        code.save()

        qs = Questions.objects.get(qs_id = id)
        return render(request , 'index.html', {"code":codeareadata ,"input":y, "output":output, 'TestCase': tc, 'Questions': qs})