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
        if  (type(self.OldList) is str and type(self.NewList) is str and type(self.ResidualList) is str
             and type(self.SheetOldList) is str and type(self.SheetNewList) is str and type(self.SheetResidualList) is str):
            
            files = {"OldList": "files/" + self.OldList,
                     "NewList": "files/" + self.NewList,
                     "ResidualList": "files/" + self.ResidualList}
            sheets = {"SheetOldList": self.SheetOldList,
                      "SheetNewList": self.SheetNewList,
                      "SheetResidualList": self.SheetResidualList}
            
            self.dict = {"files": files,"sheets": sheets}
            
            return self.dict
        

    
if __name__ == "__main__":
    load_dotenv()
    OldList = os.getenv("OldList","")
    NewList = os.getenv("NewList")
    ResidualList = os.getenv("ResidualList")
    SheetOldList = os.getenv("SheetOldList")
    SheetNewList = os.getenv("SheetNewList")
    SheetResidualList = os.getenv("SheetResidualList")

    print(OldList)
    print(NewList)
    print(ResidualList)
    print(SheetNewList,SheetOldList,SheetResidualList)

    print(type(OldList))
    print(type(OldList) is str)



