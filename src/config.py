import os

from dotenv import load_dotenv


class AppConfig:
    def __init__(self):
        load_dotenv()
        self.OldList = os.getenv("OldList")
        self.NewList = os.getenv("NewList")
        self.ResidualList = os.getenv("ResidualList")
        self.CreateList = os.getenv("CreateList")
        self.OldGrade = os.getenv("OldGrade")
        self.NewGrade = os.getenv("NewGrade")

    def __getitem__(self, key):
        return self.dict.get(key)

    def get_files_and_sheets(self):
        # 属性が全て文字列であることを確認
        if all(
            isinstance(getattr(self, attr), str)
            for attr in [
                "OldList",
                "NewList",
                "ResidualList",
                "CreateList",
                "OldGrade",
                "NewGrade",
            ]
        ):
            # ファイルとシートの辞書を作成
            files = {
                k: f"files/{getattr(self, k)}"
                for k in ["OldList", "NewList", "ResidualList", "CreateList"]
            }

            grades = {
                k: f"{getattr(self, k)}"
                for k in [
                    "OldGrade",
                    "NewGrade",
                ]
            }

            self.dict = {"files": files, "grades": grades}

        return self.dict


if __name__ == "__main__":
    load_dotenv()
    OldList = os.getenv("OldList", "")
    NewList = os.getenv("NewList")
    ResidualList = os.getenv("ResidualList")
    SheetOldList = os.getenv("SheetOldList")
    SheetNewList = os.getenv("SheetNewList")
    SheetResidualList = os.getenv("SheetResidualList")

    print(OldList)
    print(NewList)
    print(ResidualList)
    print(SheetNewList, SheetOldList, SheetResidualList)

    print(type(OldList))
    print(isinstance(OldList, str))
