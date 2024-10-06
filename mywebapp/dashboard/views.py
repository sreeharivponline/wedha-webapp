from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot import ChatBot

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def what_we_do(request):
    return render(request, 'dashboard/what_we_do.html')

def help(request):
    return render(request, 'dashboard/help.html')

def join_us(request):
    return render(request, 'dashboard/join_us.html')

def issues_we_work_on(request):
    return render(request, 'dashboard/issues_we_work_on.html')

def quiz(request):
    return render(request, 'dashboard/quiz.html')

def contribute(request):
    return render(request, 'dashboard/contribute.html')

def login_view(request):
    return render(request, 'dashboard/login.html')

chatbot = ChatBot()

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        try:
            user_message = request.POST.get('message')
            if user_message:
                response = chatbot.get_response(user_message)
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'response': "No message provided."})
        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'response': "An error occurred."})
    return JsonResponse({'response': "Invalid request method."})