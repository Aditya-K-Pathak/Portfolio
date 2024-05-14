from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import time
import json
from .Executioner import execute


def index(request):
    return render(request, 'api_index.html', {})

@csrf_exempt
def editor(request):
    """
    Handle code execution requests.

    This view function processes incoming POST requests containing code snippets
    in various programming languages. It executes the code and returns the output,
    execution time, and other relevant information as a JSON response.

    Parameters:
    - request: HttpRequest object containing the code snippet and the programming language.

    Returns:
    - JsonResponse: A JSON response containing the execution result, response time,
      and execution time. In case of an error (e.g., invalid programming language),
      it returns an error message.

    Note:
    - This view is CSRF exempt, allowing it to accept requests from other domains.
    - Supported programming languages are Python, Java, C++, and C.
    """
    if request.method == 'POST':
        initial_time = time.time()
        request = json.loads(request.body.decode('utf-8'))
        if request['code']:
            if request['lang'] == "Python":
                output = execute.ExecuteFile.execute_python_code(request['code'], request['input'] or '')
            elif request['lang'] == "Java":
                output = execute.ExecuteFile.execute_java_code(request['code'], request['input'] or '')
            elif request['lang'] == "C++":
                output = execute.ExecuteFile.execute_cpp_code(request['code'], request['input'] or '')
            elif request['lang'] == "C":
                output = execute.ExecuteFile.execute_c_code(request['code'], request['input'] or '')
            else:
                return JsonResponse({
                    "status": "Error",
                    "result": {
                        "ResponseTime": datetime.now(),
                        "Response": "Invalid Language"
                    }
                })
            return JsonResponse({
                "status": "Success",
                "result": {
                    "ResponseTime": datetime.now(),
                    "Input": request['code'],
                    "Response": output,
                    "Execution Time": time.time() - initial_time,
                }
            })

        return JsonResponse({
            "request": ['code'],
            "status": "Success",
            "result": {
                "ResponseTime": datetime.now(),
                "Response": "API Call was Successful"
            }
        })
    return JsonResponse({
        "status": "Success",
        "result": {
            "ResponseTime": datetime.now(),
            "Response": "Hello World!"
        }
    })

