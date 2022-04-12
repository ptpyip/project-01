import requests, json

class NotionAPI():
    
    def __init__(self, token: str, database_id: str, ver: str) -> None:
        ### Variables
        self.token = token

        self.database_id = database_id

        self.headers = {
            "Authorization": "Bearer " + token,
            "Notion-Version": ver,
            "Content-Type": "application/json"
        }

    ### Functions
    def readDatabase(self):
        read_url = f'https://api.notion.com/v1/databases/{self.database_id}/query'

        res = requests.request("POST", read_url, headers=self.headers)
        data = res.json()
        print(res.status_code)
        # print(res.text)

        with open('./db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
            
        return None


    def createPage(self, dictOfData) -> list:
        create_url = 'https://api.notion.com/v1/pages'

        newPageData = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Course Name":{
                    "title":[
                        {
                            "text":{
                                "content": dictOfData['CourseName']
                                }
                        }
                    ]
                },
                "Course Code": {
                    "rich_text":[
                        {
                            "text":{
                            "content": dictOfData['CourseCode']
                            }
                        }
                    ]
                },
                "USTSpace": {
                    "url" : dictOfData['USTspaceUrl']
                    },
                "Credits":{
                    'number' : dictOfData['CourseCredits']
                    }
            }
        }


        data = json.dumps(newPageData)
        res = requests.request("POST", create_url, headers=self.headers, data=data)

        #print(res.status_code)
        print(res.status_code)
        request_return = res.json()
        newPageId = request_return['id']
        newPageUrl = request_return['url']

        return [newPageId, newPageUrl, res.status_code]

    def updatePage(self, dictOfInfo): # dictOfInfo = dbCourses.json[CourseName]
        pageId = dictOfInfo['id']
        updateUrl = f'https://api.notion.com/v1/pages/{pageId}'

        newData = {
            "properties": dictOfInfo
        }

        data = json.dumps(newData)
        res = requests.request("PATCH", updateUrl, headers=self.headers, data=data)
        # how to know update what?

        return res.status_code

# help to setup notion intergation
def setUpNotion():
    setup = False
    while not setup:
        token = input("Plz give me ur token: ").strip()
        database_id = input("Plz give me ur database id: ").strip()
        ver = input("Plz give me ur notion version: ").strip()
        
        print("Your Notion info is :")
        print(f"token: {token}")
        print(f"database_id: {database_id}")
        print(f"ver: {ver}")
        
        if (input("Are you sure ur input correct? (y/n)") == "y") : setup = True
        
    return NotionAPI(token, database_id, ver)