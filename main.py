from bs4 import BeautifulSoup as bs
import requests, json
from webscraping import webScraping  
import courses
import notion 



def main():

    ### Variables
    LisOfCourseAreas =  [
        'COMP', 'ELEC',  
        'MATH', 'PHYS'
    ]
    
    Notion = notion.setUpNotion()

        
    DicOfCourse = {}
    DicOfText = {}
    for area in LisOfCourseAreas:
        url = f'https://prog-crs.ust.hk/ugcourse/2021-22/{area}'
        DicOfText[area] = webScraping(url)
        DicOfCourse[area] = {}
        for course_code, course_info in DicOfText[area].items():
            #course_info is a dict
            newCourses = courses.CoursesPage(course_code, course_info) 
            code = newCourses.createCoursePage(Notion)
            if code == 400:
                print(code)
                break

            DicOfCourse[area][course_code] = newCourses.InfoDict

    with open('./WebScraping/dbCourses.json', 'w', encoding='utf8') as f:
        json.dump(DicOfCourse, f, ensure_ascii=False)

if __name__ == '__main__':
    main()
    
# def createJson(LisOfCourseAreas):
        
#     DicOfCourse = {}
#     DicOfText = {}     

#     for area in LisOfCourseAreas:
#         url = f'https://prog-crs.ust.hk/ugcourse/2021-22/{area}'
#         DicOfText[area] = webScraping(url)
#         DicOfCourse[area] = {}
#         for course_code, course_info in DicOfText[area].items():
#             #course_info is a dict
#             newCourses = CoursesPage(course_code, course_info) 
#             DicOfCourse[area][course_code] = newCourses.InfoDict

#         with open('./WebScraping/dbCourses.json', 'w', encoding='utf8') as f:
#             json.dump(DicOfCourse, f, ensure_ascii=False)
#         # status_code = newCourses.createCoursePage()

#         # # break the loop when error
#         # if status_code == 400 :
#         #     break
#     #print("OK")
#     return None