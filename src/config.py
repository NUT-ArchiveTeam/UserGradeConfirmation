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
        # 属性が全て文字列であることを確認
        if all(isinstance(getattr(self, attr), str) for attr in 
           ["OldList", "NewList", "ResidualList", "SheetOldList", "SheetNewList", "SheetResidualList"]):
        
            # ファイルとシートの辞書を作成
            files = {k: f"files/{getattr(self, k)}" for k in ["OldList", "NewList", "ResidualList"]}
            sheets = {k: getattr(self, k) for k in ["SheetOldList", "SheetNewList", "SheetResidualList"]}

            self.dict = {"files": files, "sheets": sheets}
        
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



