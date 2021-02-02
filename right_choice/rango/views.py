from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Course_Uni, University, Course_College, Course_Apprenticeship, College, Apprenticeship, Career, SchoolSubjects, Company, User
from django.db.models import Q
def index(request):
    context_dict = {'boldmessage': 'Context dict test'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'Created by Stuart, Euan, Diego, Zhenkun and Daniyal'}
    return render(request, 'rango/about.html', context=context_dict)


def SearchResults(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query)

            results= Course_Uni.objects.filter(lookups).distinct()
            collegeResults = Course_College.objects.filter(lookups).distinct()
            apprenticeshipResults = Course_Apprenticeship.objects.filter(lookups).distinct()

            context={'results': results, 'collegeResults': collegeResults, 'apprenticeshipResults' : apprenticeshipResults,'submitbutton': submitbutton}

            return render(request, 'rango/search_results.html', context)

        else:
            return render(request, 'rango/search_results.html')

    else:
        return render(request, 'rango/search_results.html')
def uni_course(request, uni_course_slug):
    context_dict = {}

    try:
        course = Course_Uni.objects.get(slug=uni_course_slug)

        uni = University.objects.filter(name=course.universityName) 
        

        context_dict['course'] = course
        context_dict['uni'] = uni 
        
    except Category.DoesNotExist:
        context_dict['course'] = None
        context_dict['uni'] = None

    return render(request, 'rango/uni_course.html', context=context_dict)


def college_course(request, college_course_slug):
    context_dict = {}

    try:
        course = Course_College.objects.get(slug=college_course_slug)
        college = College.objects.filter(name=course.collegeName) 
        

        context_dict['course'] = course
        context_dict['college'] = college
        
    except Category.DoesNotExist:
        context_dict['course'] = None
        context_dict['college'] = None

    return render(request, 'rango/college_course.html', context=context_dict)

def apprenticeship_course(request, apprenticeship_course_slug):
    context_dict = {}

    try:
        course = Course_Apprenticeship.objects.get(slug=apprenticeship_course_slug)
        apprenticehsip = Apprenticeship.objects.filter(name=course.name) 
        

        context_dict['course'] = course
        context_dict['college'] = college
        
    except Category.DoesNotExist:
        context_dict['course'] = None
        context_dict['college'] = None

    return render(request, 'rango/apprenticeship_course.html', context=context_dict)

def uni(request):
    context_dict = {'boldmessage': 'Look at all the courses available or search for a desired course'}
    return render(request, 'rango/university.html', context=context_dict)

def college(request):
    context_dict = {'boldmessage': 'Look at all the courses available or search for a desired course'}
    return render(request, 'rango/college.html', context=context_dict)

def apprenticeship(request):
    context_dict = {'boldmessage': 'Look at all the companies offering apprenticeships'}
    return render(request, 'rango/apprenticeship.html', context=context_dict)

