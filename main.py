import requests
from bs4 import BeautifulSoup
from advert import Add, AddManager

site = 'https://www.python.org/jobs/'
siteBase = 'https://www.python.org'

result = requests.get(site)
count = 0
addManager = AddManager()

while result.status_code == 200:
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    mainBodySection = soup.find('section')
    jobOrderList = mainBodySection.find('ol')
    jobItemsList = jobOrderList.find_all('li')
    for jobItem in jobItemsList:
        # h2 title data
        jobAddvert = jobItem.find('h2')
        companyNameListing = jobAddvert.find('span', {'class' : 'listing-company-name'})
        companyName = companyNameListing.contents[-1].strip()
        position = companyNameListing.find('a').string
        jobLink = siteBase + companyNameListing.find('a')['href']
        locationSpan = jobAddvert.find('span', {'class': 'listing-location'})
        locationLink = locationSpan.find('a')
        location = locationLink.string
        # after h2 come span listing-job-type
        jobTypeSpan = jobItem.find('span', {'class' : 'listing-job-type'})
        jobs = []
        for jobData in jobTypeSpan.contents:
            jobDataString = jobData.string.replace(',','').strip()
            if jobDataString:
                jobs.append(jobDataString)

        jobType = ', '.join(jobs)
        # posted string
        jobPostedSpan = jobItem.find('span', {'class': 'listing-posted'})
        jobPostedDate = jobPostedSpan.find('time').string
        addManager.addNewAdd(Add(companyName, position, jobLink ,location, jobType, jobPostedDate))
    paginationMenu = mainBodySection.find('ul')
    nextPage = paginationMenu.find('li', {'class': 'next'})
    nextPageUri = nextPage.a['href']
    if nextPageUri:
        result = requests.get(site + nextPageUri)
    else:
        break

addManager.showAdds()
addManager.saveToFile()
