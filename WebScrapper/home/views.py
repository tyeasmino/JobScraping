from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout, authenticate, login
from bs4 import BeautifulSoup
import requests 
from csv import writer
 
# from job import job_data 

# Create your views here.
def index(request):
    template_name = "index.html"
    
    if request.user.is_anonymous: 
        return redirect("/signin")  

    else: 
        if request.method == 'POST': 
            company_name_list = []
            skills_list = []
            more_info_list = [] 
            published_date_list = [] 


            unfamiliar_skill = request.POST['title']  

            html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python').text
            soup = BeautifulSoup(html_text, 'lxml') 
            jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') 

            all_a = soup.find_all('a') 
            print(all_a)  


            with open(f'{unfamiliar_skill}.csv', 'w', encoding='utf8', newline='') as f: 
                thewriter = writer(f)  
                header = ['Company Name', 'Skills', 'More Information'] 
                thewriter.writerow(header)
                
                for job in jobs:   
                    published_date = job.find('span', class_ = 'sim-posted').span.text 

                    if 'few' in published_date:   
                        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace('  ', ' ') 
                        skills = job.find('span', class_ = 'srp-skills').text.replace('  ', ' ')
                        more_info = job.header.h2.a['href'] 

                        if unfamiliar_skill not in skills:  
                            info=[company_name, skills, more_info] 
                            thewriter.writerow(info) 

                            company_name_list.append(company_name)
                            skills_list.append(skills)
                            more_info_list.append(more_info) 
                            published_date_list.append(published_date) 

                            

            context = { 
                'company_name': company_name_list,
                'skills': skills_list, 
                'more_info': more_info_list, 
            } 
            return render(request, template_name, context) 
        
    return render(request, template_name) 


def about_site(request):
    template_name = "about_site.html"
    return render(request, template_name)

def faq(request):
    template_name = "faq.html"
    return render(request, template_name)

def signin(request):
    template_name = "signin.html" 

    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password) 
 
        user = authenticate(username=username, password=password) 

        if user is not None: 
            login(request, user) 
            return redirect("/")
        else: 
            return render(request, template_name) 

    return render(request, template_name) 

def signup(request): 
    template_name = "signup.html" 
    if request.method == 'POST': 
        new_user = User(username = request.POST["username"])
        new_user.set_password(request.POST["password"])
        new_user.save() 
        
        new_user.is_active = True
        return redirect('/signin') 
    
    return render(request, template_name) 

def logoutUser(request): 
    logout(request) 
    return redirect('/signin') 


# def contact(request):
#     template_name = "contact.html"
#     return render(request, template_name)

# def about_us(request): 
#     template_name = "about_us.html"    
#     return render(request, template_name) 
 