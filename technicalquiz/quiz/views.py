from django.shortcuts import render
from django.http import HttpResponse

var quizzes = [
        {
            'question'      :   'Q1: Who came up with the theory of relativity?',
            'choices'       :   [
                                    'Sir Isaac Newton',
                                    'Nicolaus Copernicus',
                                    'Albert Einstein',
                                    'Ralph Waldo Emmerson'
                                ],
            'correct'       :   'Albert Einstein',
            'explanation'   :   'Albert Einstein drafted the special theory of relativity in 1905.',
        },
        {
            'question'      :   'Q2: Who is on the two dollar bill?',
            'choices'       :   [
                                    'Thomas Jefferson',
                                    'Dwight D. Eisenhower',
                                    'Benjamin Franklin',
                                    'Abraham Lincoln'
                                ],
            'correct'       :   'Thomas Jefferson',
            'explanation'   :   'The two dollar bill is seldom seen in circulation. As a result, some businesses are confused when presented with the note.',
        },
        {
            'question'      :   'Q3: What event began on April 12, 1861?',
            'choices'       :   [
                                    'First manned flight',
                                    'California became a state',
                                    'American Civil War began',
                                    'Declaration of Independence'
                                ],
            'correct'       :   'American Civil War began',
            'explanation'   :   'South Carolina came under attack when Confederate soldiers attacked Fort Sumter. The war lasted until April 9th 1865.',
        }

    ]

# Create your views here.
def home(request):
    context={
        'quizzes':quizzes
    }
    return render(request,'quiz/home.html',context)

def about(request):
    return render(request,'quiz/about.html')

