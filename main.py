import requests
from bs4 import BeautifulSoup
from advert import Add, AddManager


def __getNextPageLink(pageBody):
    paginationMenu = pageBody.find('ul')
    nextPage = paginationMenu.find('li', {'class': 'next'})
    return nextPage.a['href']

def __getCompanyListingName(companyListing):
    return companyListing.find('span', {'class' : 'listing-company-name'})

def getCompanyName(companyListing):
    companyNameListing = __getCompanyListingName(companyListing)
    return companyNameListing.contents[-1].strip()

def getPosition(companyListing):
    companyNameListing = __getCompanyListingName(companyListing)
    return companyNameListing.find('a').string

def getAdvertLink(companyListing):
    companyNameListing = __getCompanyListingName(companyListing)
    return companyNameListing.find('a')['href']

def getLocation(companyListing):
    locationListing = companyListing.find('span', {'class': 'listing-location'})
    locationLink = locationListing.find('a')
    return locationLink.string

def getJobType(jobTypeListing):
    jobs = []
    for jobData in jobTypeListing.contents:
        jobDataString = jobData.string.replace(',','').strip()
        if jobDataString:
            jobs.append(jobDataString)

    jobType = ', '.join(jobs)

def getPostedDate(listingPosted):
    return listingPosted.find('time').string

def main():
    site = 'https://www.python.org/jobs/'
    siteBase = 'https://www.python.org'
    result = requests.get(site)
    count = 0
    addManager = AddManager()
    while result.status_code == 200:
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        mainBodySection = soup.find('section')
        # find orderd list containing all jobt advert
        jobOrderList = mainBodySection.find('ol')
        jobItemsList = jobOrderList.find_all('li')
        # go throught all list items
        for jobItem in jobItemsList:
            # company listing
            companyListing = jobItem.find('h2')
            companyName = getCompanyName(companyListing)
            position = getPosition(companyListing)
            jobLink = siteBase + getAdvertLink(companyListing)
            location = getLocation(companyListing)
            # after h2 come span listing-job-type
            # job type listing
            jobTypeListing = jobItem.find('span', {'class' : 'listing-job-type'})
            jobType = getJobType(jobTypeListing)
            # listing posted
            listingPosted = jobItem.find('span', {'class': 'listing-posted'})
            jobPostedDate = getPostedDate(listingPosted)
            addManager.addNewAdd(Add(companyName, position, jobLink ,location, jobType, jobPostedDate))
        nextPageUri = __getNextPageLink(mainBodySection)
        if nextPageUri:
            result = requests.get(site + nextPageUri)
        else:
            break
    addManager.showAdds()
    addManager.saveToFile(filename='jobs.csv')

if __name__ == "__main__":
    main()