from dotenv import load_dotenv
import os
import json

load_dotenv()
OldUserList=os.getenv("OldUserList")
newM1List = os.getenv("newM1List")
newResidualList = os.getenv("newResidualList")

files = {"OldUserList":"files/" + OldUserList, "newM1List":"files/"+newM1List, "newResidualList":"files/"+newResidualList}
