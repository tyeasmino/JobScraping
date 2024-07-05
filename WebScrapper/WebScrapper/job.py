import requests
from bs4 import BeautifulSoup

# job = input('Énter a job Title: ')
# location = input('enter location ')

# print(job) 



# url = ''dfsfldfjlj'

# url = 'https://www.indeed.com/job?q='



titles = []
links = []
companies = []
sumaries = [] 

dates = [] 


def job_data(url, items) : 

    res = requests.get(url).content
    soup = BeautifulSoup(res, 'html.parser')
    data = soup.find_all('div', class_ = 'jobsearch-SerpJobCard') 

    for i in data: 
        title = i.find('h2', class_ ='title')

        if item[0] in title.text:
            company = i.find('span', class_ = 'company')
            link = title.find('a')
            summary = i.find('div', class_ = 'summary') 

            data = i.find('span', class_ = 'date') 

            titles.append(title.text.strip())
            links.append('https://www.indeed.co.in'+link['href'])
            companies.append(company.text.strip())
            dates.append(date.text.string())
            summaries.append(summary.text.strip())

    return titles, companies, summary, dates, links 

    # job_data(url, items) 