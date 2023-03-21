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

ML111 = "Triết học Mác-Lênin"
ML112 = "Kinh tế chính trị và CNXH khoa học"
ML202 = "Tư tưởng Hồ Chí Minh"
ML203 = "Đường lối cách mạng của Đảng CS Việt Nam"
CS101 = "Công dân số"
MA101 = "Logic, suy luận toán học và kỹ thuật đếm"
CS100 = "Tin đại cương"
NA151 = "Khoa học môi trường"
EC101 = "Kinh tế học đại cương"
VL101 = "Tiếng Việt thực hành"
SH131 = "Pháp luật đại cương"
GE101 = "Tiếng Anh sơ cấp 1"
GE102 = "Tiếng Anh sơ cấp 2"
GE103 = "Tiếng Anh sơ cấp 3"
GE201 = "Tiếng Anh sơ trung cấp 1"
GE202 = "Tiếng Anh sơ trung cấp 2"
GE205 = "Tiếng Anh sơ trung cấp 3"
GE301 = "Tiếng Anh trung cấp 1"
GE303 = "Tiếng Anh trung cấp 2"
GE305 = "Tiếng Anh trung cấp 3"
GF101 = "Tiếng Pháp 1"
GF102 = "Tiếng Pháp 2"
GJ101 = "Tiếng Nhật 1"
GJ102 = "Tiếng Nhật 2"
GZ101 = "Tiếng Trung 1"
GZ102 = "Tiếng Trung 2"
GI101 = "Tiếng Ý 1"
GI102 = "Tiếng Ý 2"
GK101 = "Tiếng Hàn 1"
GK102 = "Tiếng Hàn 2"
PG100 = "Giaó dục thể chất"
PG121 = "Giaó dục quốc phòng"

MA103 = "Số và cấu trúc đại số"
MA110 = "Giải tích 1"
MA111 = "Giải tích 2"
MA120 = "Đại số tuyến tính"
MA231 = "Xác xuất thống kê"
MI201 = "Toán rời rạc"
CF212 = "Cấu trúc dữ liệu"
CS110 = "Kỹ thuật số"
CS121 = "Ngôn ngữ lập trình"
CS122 = "Lập trình hướng đối tượng"
CS212 = "Kiến trúc máy tính"
CS315 = "Nguyên lý hệ điều hành"
IS222 = "Cơ sở dữ liệu"
NW212 = "Mạng máy tính"
IS314 = "Hệ thống thông tin"
IS322 = "Hệ quản trị cơ sở dữ liệu"
IS329 = "Dữ liệu lớn"
IS332 = "Phân tích thiết kế hướng đối tượng"
IS334 = "Quản lý dự án hệ thống thông tin"
MI322 = "Trí tuệ nhân tạo và công nghệ tri thức"
SE302 = "Công nghệ phần mềm"
CS311 = "Lập trình ứng dụng di động"
IT320 = "Lập trình Python"
IT332 = "Internet of Things"
IT333 = "Công nghệ Web"
IT380 = "Dự án Công nghệ thông tin"
CF231 = "Lý thuyết thông tin và mã hóa"
CS321 = "Nhập môn khoa học dữ liệu"
SE380 = "Project"
SE422 = "Quản lý dự án phần mềm"
IS345 = "An toàn thông tin"
NW312 = "Thiết kế và quản trị mạng"
NW332 = "An toàn mạng"
CF211 = "Phân tích và thiết kế thuận toán"
CS223 = "Lập trình Java"
CS224 = "Lập trình .Net"
CS320 = "Học máy"
CS325 = "Lập trình PHP"
IS324 = "Phân tích cơ sở dữ liệu"
IS424 = "Lập trình cơ sở dữ liệu"
SE312 = "Kiểm thử và đảm bảo chất lượng phần mềm"
MI312 = "Đồ họa"
MI414 = "Giao diện người máy"
CF301 = "Ngôn ngữ hình thức và Otomat"
CS312 = "Lập trình hệ thống"
CS316 = "Hệ điều hành Linux"
CS425 = "Một số vấn đề hiện đại trong khoa học máy tính"
IS325 = "Cơ sở dữ liệu phân tán"
IS326 = "Khai phá dữ liệu"
IS333 = "Phân tích và thiết kế hệ thống thông tin"
IS383 = "Hệ thống thông tin nâng cao"

IP404 = "Thực tập ngành CNTT"
IT499 = "KLTN ngành CNTT"
IS484 = "CĐTN: Cơ sở dữ liệu"
SE487 = "CĐTN: Phát triển phần mềm"
IP401 = "Thực tập ngành Khoa học máy tính"
CS499 = "KLTN ngành Khoa học máy tính"
NW439 = "CĐTN: An toàn mạng"

DC = dict()
CSKN = dict()
HPBB = dict()
HPLC = dict()
TTKLCD = dict()

DC[ML111] = [2, ]
DC[ML112] = [3, [ML111]]
DC[ML202] = [2, [ML112]]
DC[ML203] = [3, [ML202]]
DC[CS101] = [2, ]
DC[MA101] = [3, ]
DC[CS100] = [2, ]
DC[NA151] = [2, ]
DC[EC101] = [3, ]
DC[VL101] = [2, ]
DC[SH131] = [2, ]
DC[GE101] = [2, ]
DC[GE102] = [2, [GE101]]
DC[GE103] = [2, [GE102]]
DC[GE201] = [2, [GE103]]
DC[GE202] = [2, [GE201]]
DC[GE205] = [2, [GE202]]
DC[GE301] = [2, [GE205]]
DC[GE303] = [2, [GE301]]
DC[GE305] = [2, [GE303]]
DC[GF101] = [2, ]
DC[GF102] = [2, [GF101]]
DC[GJ101] = [2, ]
DC[GJ102] = [2, [GJ101]]
DC[GZ101] = [2, ]
DC[GZ102] = [2, [GZ101]]
DC[GI101] = [2, ]
DC[GI102] = [2, [GI101]]
DC[GK101] = [2, ]
DC[GK102] = [2, [GK101]]
DC[PG100] = [4, ]
DC[PG121] = [4, ]
##########################################################
CSKN[MA103] = [3, [MA101]]
CSKN[MA110] = [3, [MA101]]
CSKN[MA111] = [3, [MA110]]
CSKN[MA120] = [3, [MA101]]
CSKN[MA231] = [4, [MA120, CS101]]
CSKN[MI201] = [3, [CS122]]
CSKN[CF212] = [3, [CS122]]
CSKN[CS110] = [2, [MA101]]
CSKN[CS121] = [3, [CS100]]
CSKN[CS122] = [3, [CS121]]
CSKN[CS212] = [3, [CS110, CS122]]
CSKN[CS315] = [3, [CS212]]
CSKN[IS222] = [3, [CS121, MA103]]
CSKN[NW212] = [2, [CS212]]

HPBB[IS314] = [3, [IS222]]
HPBB[IS322] = [3, [IS222]]
HPBB[IS329] = [2, [IS222]]
HPBB[IS332] = [3, [CS122, IS222]]
HPBB[IS334] = [3, [IS314]]
HPBB[MI322] = [3, [MI201, CF212]]
HPBB[SE302] = [2, [IS322]]
HPBB[CS311] = [2, [CS122]]
HPBB[IT320] = [3, [MA120, CF212]]
HPBB[IT332] = [2, [SE302]]
HPBB[IT333] = [3, [NW212]]
HPBB[IT380] = [2, [IS314]]

HPLC[CF211] = [2, [CS121]]
HPLC[CS223] = [3, [CS122]]
HPLC[CS224] = [3, [IS222]]
HPLC[CS320] = [3, [MA231]]
HPLC[CS325] = [3, [IS222]]
HPLC[IS324] = [3, [IS322]]
HPLC[IS424] = [3, [IS322]]
HPLC[SE312] = [3, [SE302]]
HPLC[MI312] = [2, [CS122, MA120]]
HPLC[MI414] = [2, [MI312]]

TTKLCD[IP404] = [2, [100]]
TTKLCD[IT499] = [6, [120]]
TTKLCD[IS484] = [6, [110, IS322]]
TTKLCD[SE487] = [6, [110, SE302]]

CNTT = [DC, CSKN, HPBB, HPLC, TTKLCD]
case = []
            
class ResponseInfoSub(Action):
      def name(self) -> Text:
            return "response_info_sub"

      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
            sub = tracker.get_slot("subject").lower()
            print(sub)
            case.append(sub)
            check = False
            for i in range(0, 5):
                  for key, value in CNTT[i].items():
                        if [key.lower()] == case:
                              if i == 0:
                                    dispatcher.utter_message(text = "Đây là môn thuộc các môn học đại cương")
                              elif i == 1:
                                    dispatcher.utter_message(text = "Đây là môn thuộc các môn học cơ sở khối ngành")
                              elif i == 2:
                                    dispatcher.utter_message(text = "Đây là môn thuộc các môn học phần bắt buộc")
                              elif i == 3:
                                    dispatcher.utter_message(text = "Đây là môn thuộc các môn học phần lựa chọn")
                              elif i == 4:
                                    dispatcher.utter_message(text = "Đây là môn thuộc các môn học thực tập, khóa luận và chuyên đề tốt nghiệp")
                              dispatcher.utter_message(text = "Đây là số tín chỉ của môn %s: %d" % (key, value[0]))
                              dispatcher.utter_message(text = "Để có thể đăng ký được môn học này cần đáp ứng yêu cầu sau:")
                              for j in range(0, len(value[1])):
                                    if isinstance(value[1][j], str):
                                          check = True
                                          dispatcher.utter_message(text = "Hoàn thành môn học tiên quyết: %s" % value[1][j])
                                    else:
                                          check = True
                                          dispatcher.utter_message(text = "Cần có: %d tín chỉ" % value[1][j])
                        elif case[0] in key.lower():
                              dispatcher.utter_message(text = "%s" % key)
                              check = True
            if check == False:
                  dispatcher.utter_message(text = "Vui lòng kiểm tra lại tên môn học!")
            case.clear()
            return []

class ResponseOfferSub(Action):
      def name(self) -> Text:
            return "response_offer_sub"
      
      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
            subs = tracker.get_slot("list")
            cres = tracker.get_slot("credit")
            if subs:
                  print(subs)
                  for sub in subs:
                        if sub != "học":
                              case.append(sub.lower())
                        if sub == "máy":
                              sub = "Học máy"
                              case.append(sub.lower())
            if cres:
                  cres = cres.split()
                  print(cres)
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
            print(case)
            if subs or cres:
                  index = 0
                  for i in range (0, 5):
                        for key, value in CNTT[i].items():
                              if len(value) > 1:
                                    temp = []
                                    for v in value[1]:
                                          if isinstance(v, str):
                                                temp.append(v.lower())
                                          else:
                                                temp.append(v)
                                    if set(temp).issubset(set(case)):
                                          if index == 0:
                                                dispatcher.utter_message(text = "Trường hợp của bạn có thể học được những môn học sau:")
                                          index += 1
                                          dispatcher.utter_message(text = "%d. %s" %(index, key))
                                    temp.clear()
                  if index == 0:
                        dispatcher.utter_message(text = "Những môn học này hiện tại không phải điều kiện tiên quyết của môn học nào")
                  index = 0
                  dispatcher.utter_message(text = "Bạn có thể học được những môn sau không có điều kiện tiên quyết khác như:")
                  for i in range (0, 5):
                        for key, value in CNTT[i].items():
                              if len(value) == 1 and set([key.lower()]).issubset(set(case)) == False:
                                    index += 1
                                    dispatcher.utter_message(text = "%d. %s" %(index, key))
            else:
                  dispatcher.utter_message(text = "Vui lòng thêm thông tin cho yêu cầu của bạn!")
            case.clear()
            return []
