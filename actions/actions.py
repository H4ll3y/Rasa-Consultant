# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import pyodbc
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-9HKF41P\ADMIN;"
    "Database=ChatBot_Rasa;"
    "Trusted_Connection=yes;"
)

DC = []
CSKN = []
HPBB = []
HPLC = []
TTKLCD = []

cursor = conn.cursor()

cursor.execute('SELECT * FROM Subject WHERE Subject.Term = 1 AND Subject.Id_Major = \'IT\'')
DC.append(cursor.fetchall())

cursor.execute('SELECT * FROM Subject WHERE Subject.Term = 2 AND Subject.Id_Major = \'IT\'')
CSKN.append(cursor.fetchall())

cursor.execute('SELECT * FROM Subject WHERE Subject.Term = 3 AND Subject.Id_Major = \'IT\'')
HPBB.append(cursor.fetchall())

cursor.execute('SELECT * FROM Subject WHERE Subject.Term = 4 AND Subject.Id_Major = \'IT\'')
HPLC.append(cursor.fetchall())

cursor.execute('SELECT * FROM Subject WHERE Subject.Term = 5 AND Subject.Id_Major = \'IT\'')
TTKLCD.append(cursor.fetchall())

cursor.close()

CNTT = [DC, CSKN, HPBB, HPLC, TTKLCD]
case = []

def textSearchTerm(type, DC, CSKN, HPBB, TTKLCD):
      text = ""
      dtype = {
            1: ["đại cương"],
            2: ["khối ngành"],
            3: ["bắt buộc"],
            4: ["lựa chọn"],
            5: ["khoá luận, chuyên đề"]
      }  
      
      t = {i for i in dtype if dtype[i][0] in type}
      t = list(t)

      index = 1
      if t[0] == 1:
            text += "Những môn thuộc đại cương:\n"
            for i in range (0, len(DC[0])):
                  text += "%d. %s\n" %(index, DC[0][i][2])
                  index += 1
      elif t[0] == 2:
            text += "Những môn thuộc cơ sở khối ngành:\n"
            for i in range (0, len(CSKN[0])):
                  text += "%d. %s\n" %(index, CSKN[0][i][2])
                  index += 1
      elif t[0] == 3:
            text += "Những môn thuộc học phần bắt buộc:\n"
            for i in range (0, len(HPBB[0])):
                  text += "%d. %s\n" %(index, HPBB[0][i][2])
                  index += 1
      elif t[0] == 4:
            text += "Những môn thuộc học phần lựa chọn:\n"
            for i in range (0, len(HPLC[0])):
                  text += "%d. %s\n" %(index, HPLC[0][i][2])
                  index += 1
      else:
            text += "Những môn thuộc khoá luận, chuyền đề tốt nghiệp:\n"
            for i in range (0, len(TTKLCD[0])):
                  text += "%d. %s\n" %(index, TTKLCD[0][i][2])
                  index += 1
      return text
      
def textSearchDetailSubject(term, case, sub):
      text = ""
      check = False
      for i in range(0, len(term[0])):
            if [term[0][i][2].lower()] == case:
                  check = True
                  if term[0][i][6] == 1:
                        text += "Đây là môn thuộc các môn học đại cương"
                  elif term[0][i][6] == 2:
                        text += "Đây là môn thuộc các môn cơ sở khối ngành"
                  elif term[0][i][6] == 3:
                        text += "Đây là môn thuộc học phần bắt buộc"
                  elif term[0][i][6] == 4:
                        text += "Đây là môn thuộc học phần lựa chọn"
                  else:
                        text += "Đây là môn thuộc khoá luận, chuyên đề tốt nghiệp"
                  text += "\nSố tín chỉ của môn %s: %d\n" % (term[0][i][2], term[0][i][3])
                  if term[0][i][4] or term[0][i][5]:
                        text += "Để có thể đăng ký được môn học này cần đáp ứng yêu cầu sau:"
                  if term[0][i][4]:
                        l = []; 
                        text += "\nHoàn thành môn học tiên quyết:\n"
                        check = True
                        if len(term[0][i][4]) < 6:
                              cursor = conn.cursor()
                              cursor.execute('SELECT Name FROM Subject WHERE Subject.Id = \'%s\'' % term[0][i][4])
                              l.append(cursor.fetchall())
                              cursor.close()
                              text += "%s\n" % l[0][0][0]
                        else:
                              for i in range(0, len(term[0][i][4])):
                                    _l = term[0][i][4].split(", ")
                                    for j in range(0, len(_l)):
                                          cursor = conn.cursor()
                                          cursor.execute('SELECT Name FROM Subject WHERE Subject.Id = \'%s\'' % _l[j])
                                          l.append(cursor.fetchall())
                                          cursor.close()
                                    text += "%s\n" % l[0][0][i]
                  if term[0][i][5]:
                        check = True
                        text += "\nCần có: %d tín chỉ\n" % term[0][i][5]
                  text += "Bạn nên học môn này ở năm %d học kỳ " % term[0][i][8]
                  if term[0][i][7] != 0:
                        text += str(term[0][i][7])
                  else:
                        text += "1, 2 hoặc 3"
            elif case[0] in term[0][i][2].lower():
                  if check == False:
                        text += "Môn %s bao gồm:\n" %sub
                  text += "%s\n" % term[0][i][2]
                  check = True       
      return text, check

class ResponseInfoSub(Action):
      def name(self) -> Text:
            return "response_info_sub"

      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
            sub = tracker.get_slot("subject")
            type = tracker.get_slot("type")
            
            if sub == None and type == None:
                  dispatcher.utter_message(text = "Vui lòng kiểm tra lại tên môn học")
                  return []
            
            print("response_info_sub")
            print("subject: %s" %sub)
            print("type: %s" %type)
            
            if type:
                  type = type.lower()
                  text = textSearchTerm(type, DC, CSKN, HPBB, TTKLCD)
            
            if sub:
                  sub = sub.lower()  
                  if sub == "thể chất" or sub == "thể dục" or sub == "giáo dục thể chất":
                        dispatcher.utter_message(text = "Đây là môn giáo dục thể chất và đều là 1 tín chỉ:\n1. Thể chất cơ bản\n2. Thể chất nâng cao\n3. Thế chất cổ truyền\n4. Bóng bàn\n5.Bóng rổ\n6. Bóng chuyền\n7. Bóng chuyền nâng cao")
                  if sub == "khóa luận tốt nghiệp" or sub == "khóa luận":
                        case.append("KLTN".lower())
                  elif sub == "chuyên đề tốt nghiệp" or sub == "chuyên đề":
                        case.append("CĐTN".lower())
                  else:
                        case.append(sub)
                  for i in range(0, 5):
                        text, check = textSearchDetailSubject(CNTT[i], case, sub)
                        if check:
                              break
                  if check == False:
                        text += "Vui lòng kiểm tra lại tên môn học"
                        
            dispatcher.utter_message(text = text)
            case.clear()
            return []

def textSearchConditionSubject(list, check, term, case, subs, cres):
      if subs or cres:
            index = 0
            for i in range (0, len(term[0])):
                  temp = []
                  if term[0][i][4]:
                        l = []
                        _l = term[0][i][4].split(", ")
                        for j in range(0, len(_l)):
                              cursor = conn.cursor()
                              cursor.execute('SELECT Name FROM Subject WHERE Subject.Id = \'%s\'' % _l[j])
                              l.append(cursor.fetchall())
                              cursor.close()
                              for k in range(0, len(l[0][0])):
                                    temp.append(l[0][0][k].lower())
                        if set(temp).issubset(set(case)):
                              check.append(True)
                              list.append(term[0][i][2])
                        else:
                              check.append(False)
                        temp.clear()
      return list, check

class ResponseOfferSub(Action):
      def name(self) -> Text:
            return "response_offer_sub"
      
      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
            subs = tracker.get_slot("list")
            cres = tracker.get_slot("credit")
            
            print("response_offer_sub")
            print("subs: %s" %subs)
            print("cres: %s" %cres)
            
            if subs:
                  for sub in subs:
                        if sub != "học" and sub != "máy":
                              case.append(sub.lower())
                        elif sub == "máy":
                              sub = "Học máy"
                              case.append(sub.lower())
            if cres:
                  cres = cres.split()
                  for cre in cres:
                        if cre.isdigit():
                              if int(cre) >= 100:
                                    case.append(100)
                              if int(cre) >= 110:
                                    case.append(110)
                                    case.append(100)           
                              if int(cre) >= 120:
                                    case.append(120)
                                    case.append(110)
                                    case.append(100)
            
            list = []
            check = []
            for i in range(0, 5):
                  list, check = textSearchConditionSubject(list, check, CNTT[i], case, subs, cres)

            if True not in check:
                  text = "Vui lòng kiểm tra lại thông tin bạn cung cấp"
            elif True in check and len(list):
                  text = "Những môn học này hiện tại không phải điều kiện tiên quyết của môn học nào"
            else:
                  text = ""
                  index = 0
                  for i in list:
                        if index == 0:
                              text += "Trường hợp của bạn có thể học được những môn học sau:\n"
                        index += 1
                        text += "%d. %s\n" %(index, i)
            dispatcher.utter_message(text = text)
            case.clear()
            return []

def texrtSearchYearSubject(term, year, semester):
      text = ""
      if year == None and semester:
            text += "Vui lòng cung cấp thêm năm học"
      elif year and semester:
            y = list(year)
            s = list(semester)
            index = 1
            for j in range (0, 5):
                  for i in range (0, len(term[j][0])):
                        if set(y).issubset(set([term[j][0][i][8]])):
                              temp = []
                              if term[j][0][i][7] == 0:
                                    temp.append(1)
                                    temp.append(2)
                                    temp.append(3)
                              else:
                                    temp.append(term[j][0][i][7])

                              if set(s).issubset(set(temp)):
                                    if index == 1:
                                          text += "Lộ trình Năm %s Kỳ %s:\n" %(y[0], s[0])
                                    text += "%d. %s\n" %(index, term[j][0][i][2])
                                    index += 1
      elif year:
            y = list(year)
            index = 1
            for j in range (0, 5):
                  for i in range (0, len(term[j][0])):
                        if set(y).issubset(set([term[j][0][i][8]])):
                              if index == 1:
                                    text += "Lộ trình Năm %s:\n" % y[0]
                              text += "%d. %s Kỳ" %(index, term[j][0][i][2])
                              if term[j][0][i][7] == 0:
                                    text += " 1, 2 và 3\n"
                              else:
                                    text += str(term[j][0][i][7]) + "\n"
                              index += 1
      return text

class ResponseYearSemester(Action):
      def name(self) -> Text:
            return "response_year_semester"
                        
      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
            dyear = {
                  1: ["nhất", "một", "1"],
                  2: ["hai", "2"],
                  3: ["ba", "3"],
                  4: ["bốn", "4", " cuối"],
                  5: ["năm", "5"],
                  6: ["sáu", "6"]
            }
            dsemester = {
                  1: ["một", "nhất", "1"],
                  2: ["hai", "2", "giữa"],
                  3: ["ba", "3", "cuối"]
            }
            dys = {
                  1: ["nửa năm", "một nửa năm", "1 nửa năm", "một năm rưỡi", "1 năm rưỡi"],
                  2: ["hai năm rưỡi", "2 năm rưỡi", "nửa năm 2", "nửa năm hai"],
                  3: ["ba năm rưỡi", "3 năm rưỡi", "nửa năm 3", "nửa năm ba"],
                  4: ["bốn năm rưỡi", "4 năm rưỡi", "nửa năm 4", "nửa năm bốn"],
                  5: ["năm năm rưỡi", "5 năm rưỡi", "nửa năm 5", "nửa năm năm"]
            }
            
            year = tracker.get_slot("year")
            semester = tracker.get_slot("semester")
            year_semester = tracker.get_slot("ysem")
            
            print("response_year_semester")
            print("year: %s" %year)
            print("semester: %s" %semester)
            print("ysem: %s" %year_semester)
            
            text = ""
            
            if year:
                  year = {i for i in dyear if set([year.lower()]).issubset(set(dyear[i]))}
                  if year == None:
                        text += "Vui lòng kiểm tra lại năm học"
                        return []
            if semester:
                  semester = {i for i in dsemester if set([semester.lower()]).issubset(set(dsemester[i]))}
                  if semester == None:
                        text += "Vui lòng kiểm tra lại kỳ học"
                        return []
            if year_semester:
                  year = {i for i in dys if set([year_semester.lower()]).issubset(set(dys[i]))}
                  semester = {2}
            
            text = texrtSearchYearSubject(CNTT, year, semester)
                  
            dispatcher.utter_message(text = text)
            return []