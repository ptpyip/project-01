from bs4 import BeautifulSoup as bs
import webbrowser, requests


def openWebPage(url) -> bool:
    status = webbrowser.open(url)
    return status

# variables
#url = 'https://prog-crs.ust.hk/ugcourse/2021-22/COMP'

def webScraping(url) -> dict :
        
    html_text = requests.get(url).text
    soup = bs(html_text, 'lxml')
    course_info = {}

    courses = soup.find_all('li', class_ = "crse accordion-item")
    for course in courses:
            
        course_description = course.find('div', class_ = 'data-row data-row-long').text
        course_code = course.find('div', class_ = 'crse-code').text
        course_code= course_code.replace(' ', '')
        course_name = course.find('div', class_ = 'crse-title').text
        course_creds = course.find('div', class_ = 'crse-unit').text
        course_creds = int(course_creds[0])

        course_detail = course.find_all('div', class_ = 'data-row data-row-default')
        course_remarks_headers = []
        course_remarks_datas = []
        course_remarks = {}
        
        for tag in course_detail:
            header = tag.find('div', class_ = 'header').text
            data = tag.find('div', class_ = 'data').text
            course_remarks[header] = data
                
        course_info[course_code] = {        
            'CourseCode':course_code,
            'CourseName':course_name,
            'CourseCredits':course_creds,
            'CourseDescription':course_description,
            'CourseRemarks':course_remarks
        }

    return course_info


print("imported")

