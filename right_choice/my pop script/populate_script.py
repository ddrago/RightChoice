import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'right_choice.settings') 
 
import django 
django.setup() 

from rango.models import User, University, College, Apprenticeship, Course_Uni, Course_College, Course_Apprenticeship, Career, SchoolSubjects, Company


def populate():

    computing_career = [{'career_name':'Software Engineer', 'areaOfStudy': 'Computing Science'}] #change this to list if it doesnt work.
    finance_career = [{'career_name': 'Banker', 'areaOfStudy': 'Finance'}]

    #careers = [computing_career, finance_career]
    school_subjects_computing_higher = [{'name': 'Compuitng Science', 'level': 'Higher', 'career_name':computing_career, 'subjectArea': 'Computing'},{'name': 'Mathmatics', 'level': 'Higher', 'career_name':computing_career, 'subjectArea': 'Maths'}]
    school_subjects_business_higher = [{'name': 'Business Studies', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]

    school_subjects_computing_nat5 = [{'name': 'Compuitng Science', 'level': 'Nat 5', 'career_name':computing_career, 'subjectArea': 'Computing'},{'name': 'Mathmatics', 'level': 'Nat 5', 'career_name':computing_career, 'subjectArea': 'Maths'}]
    school_subjects_business_nat5 = [{'name': 'Business Studies', 'level': 'Nat 5', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]

    school_subjects = school_subjects_computing_higher + school_subjects_business_higher + school_subjects_computing_nat5 + school_subjects_business_nat5
    
    courses_city_of_glasgow_college = [{'courseID':1, 'name':'Computing Science HNC', 'collegeName': 'City of Glasgow College', 'career_name':computing_career, 'subReqName':school_subjects_computing_nat5, 'gradesReq': 'CC', 'subjectSuggestions':'Computing Science, Maths and Physics'},
                                    {'courseID': 2, 'name': 'Finance and Accounting HNC', 'collegeName':'City of Glasgow College', 'career_name': finance_career, 'subReqName':school_subjects_business_nat5, 'gradesReq': 'CC', 'subjectSuggestions':'Business, Maths and Economics'}]

    courses_glasgow_uni = [{'courseID': 1, 'name': 'Computing Science Bsc', 'universityName':'Glasgow University', 'career_name': computing_career, 'subReqName':school_subjects_computing_higher, 'gradesReq': 'AAAB', 'subjectSuggestions':'Computing Science, Maths and Physics'}, 
                           {'courseID': 2, 'name': 'Finance and Accounting Bsc', 'universityName':'Glasgow University', 'career_name': finance_career, 'subReqName':school_subjects_business_higher, 'gradesReq': 'AAAB', 'subjectSuggestions':'Business, Maths and Economics'}]


    courses_apprenticeships_scotland = [{'courseID':1, 'name':'Accounting Apprenticeship', 'companyName': 'Apprenticeship Scotland', 'career_name':finance_career, 'gradesReq': 'No qualifications required', 'subjectSuggestions':'Business, Maths and Economics'}]

    Universities = [{'courses': courses_glasgow_uni, 'name': 'Glasgow University', 'location': 'Glasgow', 'details': 'One of Scotlands finest universites and the fourth oldest uni in the world', 'universityImage':'Glasgow_University.jpg', 'linkToUniWebsite': 'https://www.gla.ac.uk/'}]
    
    Colleges = [{'courses': courses_city_of_glasgow_college, 'name': 'City of Glasgow College', 'location':'Glasgow', 'details': 'The city of glasgow college is located right in the center of glasgow.', 'collegeImage':'city_of_glasgow_college.png', 'linkToCollegeWebsite':'https://www.cityofglasgowcollege.ac.uk/'}]
     
    Apprenticeships = [{'courses': courses_apprenticeships_scotland, 'name': 'Apprenticeships Scotland', 'location':'Glasgow', 'details': 'bla, bla, bla', 'companyImage': 'apprenticeship.png', 'linkToCompanyWebsite': 'https://www.apprenticeships.scot/become-an-apprentice/graduate-apprenticeships/accounting/'}]
   # user = User(username='defaultUserName', email='default_user@gmail.com', password='defaultPassword123')
    #user.save()
    
    
    def add_uni(name, location, details, universityImage, linkToUniWebsite):
        u = University.objects.get_or_create(name=name)[0]
        u.location = location
        u.details = details
        u.universityImage = universityImage
        u.linkToCollegeWebsite = linkToUniWebsite
        u.save()
        return u

    def add_career(careerName, areaOfStudy):
        c = Career.objects.get_or_create(careerName=careerName)[0]
        c.areaOfStudy=areaOfStudy
        c.save()
        return c

    def add_school_subjects(name, level, career_name, subjectArea):
        s = SchoolSubjects.objects.get_or_create(name=name, level=level)[0]
        s.career_name.set(career_name)
        s.subjectArea = subjectArea
        s.save()
        return s

    def add_college(name, location, details, collegeImage, linkToCollegeWebsite):
        c = College.objects.get_or_create(name=name)[0]
        c.location = location
        c.details = details
        c.collegeImage = collegeImage
        c.linkToCollegeWebsite = linkToCollegeWebsite
        c.save()
        return c


    def add_apprenticeship(name, location, details, companyImage, linkToCompanyWebsite):
        a = Apprenticeship.objects.get_or_create(name=name)[0]
        a.location = location
        a.details = details
        a.companyImage = companyImage
        a.linkToCompanyWebsite = linkToCompanyWebsite
        a.save()
        return a

    def course_uni(courseID, name, universityName, careerName, subReqName, gradesReq, subjectSuggestions): #career name & subReq are lists in this case
        u_course = Course_Uni.objects.get_or_create(courseID=courseID, universityName=universityName)[0]
        u_course.name = name
        u_course.gradesReq = gradesReq
        u_course.subjectSuggestions = subjectSuggestions
        u_course.careerName.add(*careerName)
        u_course.subReqName.add(*subReqName)
        u_course.save()
        return u_course

    def course_college(courseID, name, collegeName, careerName, subReqName, gradesReq, subjectSuggestions): #career name & subReq are lists in this case
        c_course = Course_College.objects.get_or_create(courseID=courseID, collegeName=collegeName)[0]
        c_course.name = name
        c_course.gradesReq = gradesReq
        c_course.subjectSuggestions = subjectSuggestions
        c_course.careerName.add(*careerName)
        c_course.subReqName.add(*subReqName)
        c_course.save()
        return c_course

    def course_apprenticeship(courseID, name, companyName, careerName, gradesReq, subjectSuggestions): #career name & subReq are lists in this case
        a_course = Course_Apprenticeship.objects.get_or_create(courseID=courseID, companyName=companyName)[0]
        a_course.name = name
        a_course.gradesReq = gradesReq
        a_course.subjectSuggestions = subjectSuggestions
        a_course.careerName.add(*careerName)
        a_course.save()
        return a_course

 #   for d in Universities:
 #       add_uni(d["name"],d["location"], d["details"], d["universityImage"], d["linkToUniWebsite"])

 #   for c in University.objects.all():
 #       print(f'-{c}')

#    for career in careers:
#        added_career = add_career(career["career_name"], career["areaOfStudy"])

#    for ca in Career.objects.all():
#        print(f'-{ca}')

#    for s in school_subjects:
#        add_school_subjects(s["name"], s["level"], added_career, s["subjectArea"])

#    for subject in SchoolSubjects.objects.all():
#        print(f'-{subject}')

    
    for d in Universities:
        uni_careers = []
        uni_subjects = []
        u = add_uni(d["name"],d["location"], d["details"], d["universityImage"], d["linkToUniWebsite"])
        for course in d["courses"]:
            for career in course["career_name"]:

                added_career = add_career(career["career_name"], career["areaOfStudy"])
                for s in course["subReqName"]:
                    added_subject = add_school_subjects(s["name"], s["level"], [added_career], s["subjectArea"])
                    uni_subjects.append(added_subject)
                uni_careers.append(added_career)

            course_uni(course["courseID"], course["name"], u, uni_careers, uni_subjects, course["gradesReq"], course["subjectSuggestions"])

    for college in Colleges:
        college_careers = []
        college_subjects = []
        c = add_college(college["name"],college["location"], college["details"], college["collegeImage"], college["linkToCollegeWebsite"])
        for course in college["courses"]:
            for career in course["career_name"]:

                added_career = add_career(career["career_name"], career["areaOfStudy"])
                for s in course["subReqName"]:
                    added_subject = add_school_subjects(s["name"], s["level"], [added_career], s["subjectArea"])
                    college_subjects.append(added_subject)
                college_careers.append(added_career)

            course_college(course["courseID"], course["name"], c, college_careers, college_subjects, course["gradesReq"], course["subjectSuggestions"])



    company = [{'name': "Apprenticeship Scotland", 'location': "edinburgh", "details": "The leading provider of apprentieships in Scotland.", 'linkToCompanyWebsite': "jjjj" }] 

    for d in company:
        t = Company.objects.get_or_create(name=d["name"], location=d["location"], details=d["details"], linkToCompanyWebsite=d["linkToCompanyWebsite"])[0]
        t.save()

    for apprenticeship in Apprenticeships:
        apprenticeship_careers = []
        a = add_apprenticeship(apprenticeship["name"],apprenticeship["location"], apprenticeship["details"], apprenticeship["companyImage"], apprenticeship["linkToCompanyWebsite"])
        for course in apprenticeship["courses"]:
            for career in course["career_name"]:

                added_career = add_career(career["career_name"], career["areaOfStudy"])
                apprenticeship_careers.append(added_career)

            course_apprenticeship(course["courseID"], course["name"], t, apprenticeship_careers, course["gradesReq"], course["subjectSuggestions"])


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
