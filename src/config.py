from dotenv import load_dotenv
import os

class AppConfig:
    def __init__(self):
        load_dotenv()
        self.OldList = os.getenv("OldList")
        self.NewList = os.getenv("NewList")
        self.ResidualList = os.getenv("ResidualList")
        self.SheetOldList = os.getenv("SheetOldList")
        self.SheetNewList = os.getenv("SheetNewList")
        self.SheetResidualList = os.getenv("SheetResidualList")

    def __getitem__(self, key):
        return self.dict.get(key)

        
    def get_files_and_sheets(self):
        if  (self.OldList is str and self.NewList and str and self.ResidualList is str
             and self.SheetOldList is str and self.SheetNewList is str and self.SheetResidualList is str):
            
            files = {"OldList": "files/" + self.OldList,
                     "NewList": "files/" + self.NewList,
                     "ResidualList": "files/" + self.ResidualList}
            sheets = {"SheetOldList": self.SheetOldList,
                      "SheetNewList": self.SheetNewList,
                      "SheetResidualList": self.SheetResidualList}
            
            self.dict = {"files": files,"sheets": sheets}
            
            return self.dict

