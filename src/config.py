from dotenv import load_dotenv
import os

class AppConfig:
    def __init__(self):
        load_dotenv()
        self.OldUserList = os.getenv("OldUserList")
        self.newM1List = os.getenv("newM1List")
        self.newResidualList = os.getenv("newResidualList")
        self.SheetOldUserList = os.getenv("SheetOldUserList")
        self.SheetNewM1List = os.getenv("SheetNewM1List")
        self.SheetNewResidualList = os.getenv("SheetNewResidualList")

    def __getitem__(self, key):
        return self.dict.get(key)

        
    def get_files_and_sheets(self):
        if  (self.OldUserList is str and self.newM1List and str and self.newResidualList is str
             and self.SheetOldUserList is str and self.SheetNewM1List is str and self.SheetNewResidualList is str):
            
            files = {"OldUserList": "files/" + self.OldUserList,
                     "newM1List": "files/" + self.newM1List,
                     "newResidualList": "files/" + self.newResidualList}
            sheets = {"SheetOldUserList": self.SheetOldUserList,
                      "SheetNewM1List": self.SheetNewM1List,
                      "SheetNewResidualList": self.SheetNewResidualList}
            
            self.dict = {"files": files,"sheets": sheets}
            
            return self.dict

