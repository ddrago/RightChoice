import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'right_choice.settings') 
 
import django 
django.setup() 

from rango.models import User, University, College, Apprenticship, Course_Uni, Course_College, Course_Apprenticeship, Career, SchoolSubjects


def populate():

    computing_career = {'career_name':'Software Engineer', 'areaOfStudy': 'Computing Science'}
    finance_career = {'career_name': 'Banker', 'areaOfStudy': 'Finance'}


    school_subjects_computing_higher = [{'name': 'Compuitng Science', 'level': 'Higher', 'career_name':computing_career, 'subjectArea': 'Computing'},{'name': 'Mathmatics', 'level': 'Higher', 'career_name':computing_career, 'subjectArea': 'Maths'}]
    school_subjects_business_higher = [{'name': 'Business Studies', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]

    school_subjects_computing_nat5 = [{'name': 'Compuitng Science', 'level': 'Nat 5', 'career_name':computing_career, 'subjectArea': 'Computing'},{'name': 'Mathmatics', 'level': 'Nat 5', 'career_name':computing_career, 'subjectArea': 'Maths'}]
    school_subjects_business_nat5 = [{'name': 'Business Studies', 'level': 'Nat 5', 'career_name':finance_career, 'subjectArea': 'Business'}, {'name': 'Mathamatics', 'level': 'Higher', 'career_name':finance_career, 'subjectArea': 'Maths'}]
    
    courses_city_of_glasgow_college[{'courseID':1, 'name':'Computing Science HNC', 'collegeName': 'City of Glasgow College', 'career_name':computing_career, 'subReqName':school_subjects_computing_nat5, 'gradesReq': 'CC', 'subjectSuggestions':'Computing Science, Maths and Physics'},
                                    {'courseID': 2, 'name': 'Finance and Accounting HNC', 'collegeName':'City of Glasgow College', 'career_name': finance_career, 'subReqName':school_subjects_business_nat5, 'gradesReq': 'CC', 'subjectSuggestions':'Business, Maths and Economics'}]

    courses_glasgow_uni = [{'courseID': 1, 'name': 'Computing Science Bsc', 'universityName':'Glasgow University', 'career_name': computing_career, 'subReqName':school_subjects_computing_higher, 'gradesReq': 'AAAB', 'subjectSuggestions':'Computing Science, Maths and Physics'}, 
                           {'courseID': 2, 'name': 'Finance and Accounting Bsc', 'universityName':'Glasgow University', 'career_name': finance_career, 'subReqName':school_subjects_business_higher, 'gradesReq': 'AAAB', 'subjectSuggestions':'Business, Maths and Economics'}]


    courses_apprenticeships_scotland = [{'courseID':1, 'name':'Accounting Apprenticeship', 'companyName': 'Apprenticeship Scotland', 'careerName':finace_career, 'gradesReq': 'No qualifications required', 'subjectSuggestions':'Business, Maths and Economics'}]

    Universities = [{'courses': courses_glasgow_uni, 'name': 'Glasgow University', 'location': 'Glasgow', 'details': 'One of Scotlands finest universites and the fourth oldest uni in the world', 'universityImage':'Glasgow_University.jpg', 'linkToUniWebsite': 'https://www.gla.ac.uk/'}]
    
    Colleges = [{'courses': courses_city_of_glasgow_college, 'name': 'City of Glasgow College', 'location':'Glasgow', 'details': 'The city of glasgow college is located right in the center of glasgow.', 'collegeImage':'city_of_glasgow_college.png', 'linkToCollegeWebsite':'https://www.cityofglasgowcollege.ac.uk/'}]
     
    Apprenticeships = [{'courses': courses_apprenticeships_scotland, 'name': 'Apprenticeships Scotland', 'location':'Glasgow', 'details': 'bla, bla, bla', 'companyImage': 'apprenticeship.png', 'linkToCompanyWebsite': 'https://www.apprenticeships.scot/become-an-apprentice/graduate-apprenticeships/accounting/'}]
    user = User(username='defaultUserName', email='default_user@gmail.com', password='defaultPassword123')
    user.save()
    


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
