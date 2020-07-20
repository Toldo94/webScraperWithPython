import os


class Add:
    def __init__(self, companyName, position, link, location, jobType, date):
        self.companyName = companyName
        self.position = position
        self.jobLink = link
        self.location = location
        self.jobType = jobType
        self.postedDate = date

    def __repr__(self):
        return 'Company: {}, Position: {}, Link: {} ,Location: {}, Type: {}, Posted: {}\n'.format(
            self.companyName,
            self.position,
            self.jobLink,
            self.location,
            self.jobType,
            self.postedDate,
        )

    def fileRepresentation(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\n'.format(
            self.companyName,
            self.position,
            self.jobLink,
            self.location,
            self.jobType,
            self.postedDate,
        )


class AddManager:
    def __init__(self):
        self.addList = []

    def addNewAdd(self, add):
        self.addList.append(add)

    def showAdds(self):
        for add in self.addList:
            print(add)

    def fileHeader(self):
        return 'Company\tPosition\tLink\tLocation\tType\tPosted\n'

    def saveToFile(self, filename):
        currentFileDir = os.path.abspath(os.path.dirname(__file__))
        saveFile = os.path.join(currentFileDir, filename)
        f = open(saveFile, 'w')
        f.write(self.fileHeader())
        f.close()
        with open(saveFile, mode='a+', encoding='utf-8') as my_file:
            for add in self.addList:
                my_file.write(add.fileRepresentation())

