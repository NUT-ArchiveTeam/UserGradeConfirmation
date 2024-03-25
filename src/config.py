from dotenv import load_dotenv
import os
import json

load_dotenv()
OldUserList=os.getenv("OldUserList")
newM1List = os.getenv("newM1List")
newResidualList = os.getenv("newResidualList")

SheetOldUserList=os.getenv("SheetOldUserList")
SheetNewM1List = os.getenv("SheetNewM1List")
SheetNewResidualList = os.getenv("SheetNewResidualList")


def config() :
    if (OldUserList is None or newM1List is None or newResidualList is None or SheetOldUserList is None or SheetNewM1List is None or SheetNewResidualList is None):
        return 0
    else:
        files = {"OldUserList":"files/" + OldUserList, "newM1List":"files/"+newM1List, "newResidualList":"files/"+newResidualList}
        sheets = {"SheetOldUserList":SheetOldUserList, "SheetNewM1List":SheetNewM1List, "SheetNewResidualList":SheetNewResidualList}
        return files,sheets
