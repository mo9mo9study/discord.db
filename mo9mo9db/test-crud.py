# -*- coding: utf-8 -*-
import sys
import inspect
from pprint import pprint

from dbtables import Studytimelogs, Studymembers, Studytags

arg = ""
args = sys.argv

print(f"引数の数：{len(args)}({args})")
if len(args) > 1: 
    arg = args[1]
    session = Studymembers.session()
else:
    print("引数に[insert/update/delete/select]を指定してください")
    sys.exit()

if arg == "insert":
    # insert
    obj = Studymembers(guild_id="470074961617354773",
                            member_id="603567991132782592",
                            member_name="SuPleiades",
                            joined_dt="2021-01-15 09:05:01")
    Studymembers.insert(obj)
elif arg == "update":
    # Update
    obj = Studymembers.objects(session).first()
    obj.enrollment = True
    obj.organize = False  
    obj.save(session)
    #pprint(inspect.getmembers(obj), indent=4)
elif arg == "delete":
    obj = Studymembers.objects(session).first()
    obj.delete(session)
elif arg == "select":
    member_id = "603567991132782592"
    obj = Studymembers.objects(session).filter(Studymembers.member_id == member_id).first()
    #pprint(inspect.getmembers(obj.__dict__), indent=4)
    pprint(obj.__dict__, indent=4)
else:
    print("引数に[insert/update/delete/select]を指定してください")
    sys.exit()


# select

# Delete
    



