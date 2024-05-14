from django.shortcuts import render
from . import forms
import requests
import json
import random
from . import data

def get_question():
    response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple').json()
    return {i['question']: [i['correct_answer']] + i['incorrect_answers'] for i in response['results']}

# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST.get('user_name') not in data.DATA:
            data.DATA.update({
            request.POST.get('user_name'):{
                'PASSWORD': request.POST.get('password'),
                'CURRENTSCORE': 0,
                'HIGHSCORE': 0,
                'PREVIOUS': 0,
            }
        })
        return quiz(request)
    return render(request, 'register.html', {'form': forms.userRegisteration()})

def quiz(request):
    username = request.POST.get('user_name')
    if request.method == 'POST':
        opt = list('abcd')
        if data.DATA[username]['PREVIOUS'] and opt[data.DATA[username]['PREVIOUS']] in request.POST:
            data.DATA[username]['CURRENTSCORE'] += 1
            data.DATA[username]['HIGHSCORE'] = max(data.DATA[username]['CURRENTSCORE'], 
                                                   data.DATA[username]['HIGHSCORE'])
    questions = get_question()
    for question in questions:
        question = question
        options = questions[question]
        correct_option = options[0]
        random.shuffle(options)
        correct_option_number = options.index(correct_option)
        data.DATA[username]['PREVIOUS'] = correct_option_number
        choices = ['A', 'B', 'C', 'D']
        for i in range (4):
            options[i] = choices[i] + '.) ' + options[i]
        return render(request, 'quiz.html', {
            'username': username,
            'options': options,
            'question': question,
            'form': forms.options, 
            'Score': data.DATA[username]['CURRENTSCORE']
        })
    
def index(request):
    return render(request, 'gameindex.html')