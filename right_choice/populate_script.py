import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'right_choice.settings')

import django
django.setup()

from rango.models import User, University, College, Apprenticeship, Course_Uni, Course_College, Course_Apprenticeship, Career, SchoolSubjects, Company


def populate():

    career = [{'career_name':"Software Engineer", 'areaOfStudy': "Computing Science"}, {'career_name': "Mathematician", 'areaOfStudy': "Mathematician"}]
    #finance_career = {'career_name': 'Banker', 'areaOfStudy': 'Finance'}
    for d in career:
        t = Career.objects.get_or_create(careerName=d['career_name'], areaStudy=d['areaOfStudy'])[0]
        t.save()
    for c in Career.objects.all():
        print(f'-{c}')

    school_subjects_computing_higher = [{'name': 'Computing Science', 'level': 'Higher', 'career_name':"Software Engineer", 'subjectArea': 'Computing'},{'name': 'Mathematics', 'level': 'Higher', 'career_name':"Mathematician", 'subjectArea': 'Maths'}]
    #school_subjects_business_higher = [{'name': 'Business Studies', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]
    for d in school_subjects_computing_higher:
        t = SchoolSubjects.objects.get_or_create(name=d["name"], level=d["level"], subjectArea=d["subjectArea"])[0]
        t.career_name.filter(careerName=d["career_name"])
        t.save()
    for c in SchoolSubjects.objects.all():
        print(f'-{c}')


    school_subjects_computing_nat5 = [{'name': 'Compuitng Science', 'level': 'Nat 5', 'career_name':"Software Engineer", 'subjectArea': 'Computing'},{'name': 'Mathematics', 'level': 'Nat 5', 'career_name':"Mathematician", 'subjectArea': 'Maths'}]
    #school_subjects_business_nat5 = [{'name': 'Business Studies', 'level': 'Nat 5', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]
    for d in school_subjects_computing_nat5:
        t = SchoolSubjects.objects.get_or_create(name=d["name"],level=d["level"], subjectArea=d["subjectArea"])[0]
        t.career_name.filter(careerName=d["career_name"])
        t.save()
    for c in SchoolSubjects.objects.all():
        print(f'-{c}')


    Colleges = [{'courses': None, 'name': 'City of Glasgow College', 'location':'Glasgow', 'details': 'The city of glasgow college is located right in the center of glasgow.', 'collegeImage':'city_of_glasgow_college.png', 'linkToCollegeWebsite':'https://www.cityofglasgowcollege.ac.uk/'}]
    for d in Colleges:
        t = College.objects.get_or_create(name=d["name"], location=d["location"], details=d["details"], linkToCollegeWebsite=d["linkToCollegeWebsite"])[0]
        t.save()
    for c in College.objects.all():
        print(f'-{c}')


    courses_city_of_glasgow_college = [{'courseID':1, 'name':'Computing Science HNC', 'collegeName': College.objects.get(name="City of Glasgow College"), 'career_name':Career.objects.get(areaStudy="Computing Science"), 'subReqName':SchoolSubjects.objects.get(name="Mathematics", level="Nat 5"), 'gradesReq': 'CC', 'subjectSuggestions':'Computing Science, Maths and Physics'},
                                    {'courseID': 2, 'name': 'Finance and Accounting HNC', 'collegeName': College.objects.get(name="City of Glasgow College"), 'career_name': Career.objects.get(areaStudy="Mathematician"), 'subReqName':SchoolSubjects.objects.get(name="Mathematics", level="Nat 5"), 'gradesReq': 'CC', 'subjectSuggestions':'Business, Maths and Economics'}]
    for d in courses_city_of_glasgow_college:
        t = Course_College.objects.get_or_create(courseID=d["courseID"], name=d["name"], collegeName=d["collegeName"], gradesReq=d["gradesReq"], subjectSuggestions=d["subjectSuggestions"])[0]
        t.careerName.filter(careerName=d["career_name"])
        t.subReqName.filter(name=d["subReqName"])
        t.save()
    for c in Course_College.objects.all():
        print(f'-{c}')

    Universities = [{'courses': None, 'name': 'Glasgow University', 'location': 'Glasgow', 'details': 'One of Scotlands finest universites and the fourth oldest uni in the world', 'universityImage':'Glasgow_University.jpg', 'linkToUniWebsite': 'https://www.gla.ac.uk/'}]
    for d in Universities:
        t = University.objects.get_or_create(name=d['name'], location=d['location'], details=d['details'])[0]
        t.save()

    for c in University.objects.all():
        print(f'-{c}')


    courses_glasgow_uni = [{'courseID': 1, 'name': 'Computing Science Bsc', 'universityName':University.objects.get(name="Glasgow University"), 'career_name': Career.objects.get(areaStudy="Computing Science"), 'subReqName':SchoolSubjects.objects.get(name="Mathematics", level="Higher"), 'gradesReq': 'AAAB', 'subjectSuggestions':'Computing Science, Maths and Physics'},
                           {'courseID': 2, 'name': 'Finance and Accounting Bsc', 'universityName':University.objects.get(name="Glasgow University"), 'career_name': Career.objects.get(areaStudy="Mathematician"), 'subReqName':SchoolSubjects.objects.get(name="Mathematics", level="Higher"), 'gradesReq': 'AAAB', 'subjectSuggestions':'Business, Maths and Economics'}]
    for d in courses_glasgow_uni:
        t = Course_Uni.objects.get_or_create(courseID=d["courseID"], name=d["name"], universityName=d["universityName"], gradesReq=d["gradesReq"], subjectSuggestions=d["subjectSuggestions"])[0]
        t.careerName.filter(careerName=d["career_name"])
        t.subReqName.filter(name=d["subReqName"])
        t.save()
    for c in Course_Uni.objects.all():
        print(f'-{c}')

    company = [{'name': "Apprenticeship Scotland", 'location': "edinburgh", "details": "The leading provider of apprentieships in Scotland.", 'linkToCompanyWebsite': "jjjj" }]

    for d in company:
        t = Company.objects.get_or_create(name=d["name"], location=d["location"], details=d["details"], linkToCompanyWebsite=d["linkToCompanyWebsite"])[0]
        t.save()
    for c in Company.objects.all():
        print(f'-{c}')


    courses_apprenticeships_scotland = [{'courseID':1, 'name':'Accounting Apprenticeship', 'companyName': Company.objects.get(name='Apprenticeship Scotland'), 'careerName':Career.objects.get(areaStudy="Mathematician"), 'gradesReq': 'No qualifications required', 'subjectSuggestions':'Business, Maths and Economics'}]
    for d in courses_apprenticeships_scotland:
        t = Course_Apprenticeship.objects.get_or_create(courseID=d["courseID"], name=d["name"], companyName=d["companyName"], gradesReq=d["gradesReq"], subjectSuggestions=d["subjectSuggestions"])[0]
        t.careerName.filter(careerName=d["careerName"])
        t.save()
    for c in Course_Apprenticeship.objects.all():
        print(f'-{c}')


    Apprenticeships = [{'name': 'Apprenticeship Scotland', 'location':'Glasgow', 'details': 'bla, bla, bla', 'companyImage': 'apprenticeship.png', 'linkToCompanyWebsite': 'https://www.apprenticeships.scot/become-an-apprentice/graduate-apprenticeships/accounting/'}]
    for d in Apprenticeships:
        t = Apprenticeship.objects.get_or_create(name=d["name"], location=d["location"], details=d["details"], companyImage=d["companyImage"], linkToCompanyWebsite=d["linkToCompanyWebsite"])[0]
        t.save()

    for c in Apprenticeship.objects.all():
        print(f'-{c}')

    user = User(username='defaultUserName', email='default_user@gmail.com', password='defaultPassword123')
    user.save()





if __name__ == '__main__':
    print('Starting right choice population script...')
    populate()
