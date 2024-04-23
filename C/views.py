import os
import subprocess
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from C.models import *
from django.contrib import messages
from user_handler.models import *

@login_required
def runcode(request, id):
    output = ""
    code_original = ""
    input_data = ""

    if request.method == "POST":
        code = request.POST.get('codearea')
        code_original = code
        input_data = request.POST.get('inputarea')  # Retrieve user input data
        # print(input_data)

        try:
            # Base path for saving files
            base_path = "C:\\Users\\Pratham\\Desktop\\C COMPILER"

            # Path for the source code file
            source_file_path = os.path.join(base_path, 'code.c')

            # Save user-submitted code to the fixed file path
            default_storage.save(source_file_path, ContentFile(code))

            # Compilation
            executable_path = os.path.join(base_path, 'code.exe')
            compilation_process = subprocess.run(['gcc', '-o', executable_path, source_file_path, '-mconsole'], capture_output=True, text=True)

            if compilation_process.returncode == 0:
                # Execution with input data
                # input_bytes = input_data.encode('utf-8')  # Encode input data to bytes
                execution_process = subprocess.run([executable_path], input=input_data, capture_output=True, text=True)
                output = execution_process.stdout + execution_process.stderr
            else:
                output = "Compilation Error:\n" + compilation_process.stderr

        except Exception as e:
            output = f"Error: {e}"

        finally:
            # Cleanup: Delete the code.c file after execution
            if os.path.exists(source_file_path):
                os.remove(source_file_path)

    Qs = Questions.objects.get(qs_id = id)
    tc = TestCase.objects.get(qs_id = id)
    if str(tc.expected_output).strip() == str(output).strip():
        messages.info(request, 'Sample Testcase passed')
    else:
        messages.error(request, 'Sample testcase failed')
    return render(request, 'indexc.html', {'TestCase' : tc, 'code': code_original, 'output': output, 'Questions': Qs})


@login_required
def homepage(request, id):
    queryset = Questions.objects.get(qs_id = id)
    tc = TestCase.objects.get(qs_id = queryset)
    context = {'Questions':queryset, 'TestCase' : tc}
    return render(request, 'indexc.html', context)
