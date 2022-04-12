from bs4 import BeautifulSoup as bs
import requests, json
from webscraping import webScraping  
import notion 

# Create HKUST course object
class CoursesPage():
    def __init__(self, course_code, course_info) -> None:  
        # course_info is a dict. 
        self.CourseCode = course_code
        self.CourseName = course_info['CourseName']
        self.CourseCredits = course_info['CourseCredits']
        self.CourseDescription = course_info['CourseDescription']
        self.CourseRemarks = None
        
        if (course_info['CourseRemarks'] != {}): self.CourseRemarks = course_info['CourseRemarks']

        self.CourseAreas = [course_code[0:4]]
        self.USTspaceUrl = f'https://ust.space/review/{course_code}'
        
        self.InfoDict = {
            'CourseCode':self.CourseCode,
            'CourseName':self.CourseName,
            'CourseCredits':self.CourseCredits,
            'CourseAreas':self.CourseAreas,
            'CourseDescription':self.CourseDescription,
            'CourseRemarks':self.CourseRemarks,
            'USTspaceUrl':self.USTspaceUrl
        }

    def createCoursePage(self, NotionAPI: notion.NotionAPI) -> int:
        
        # call the notion API
        ListOfReturn = NotionAPI.createPage(self.InfoDict)

        self.Id = ListOfReturn[0]
        self.InfoDict['id'] = self.Id

        self.url = ListOfReturn[1]
        self.InfoDict['url'] = self.url

        code = ListOfReturn[2]
        return code # for detect error





