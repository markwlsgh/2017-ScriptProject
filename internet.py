from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib.request
import urllib


key = '4VB0o7ZOlNdClfP%2FidH3cNjCCsAfg3APKmEf7Tqg4aS2uPSNn1pA2avCeTcqVVY4pV6I7252637lX8LFUtxXJQ%3D%3D'

#키워드 검색
def AreaFinding():
    keyword = str(input("Keyword : "))
    hangul_utf8 = urllib.parse.quote(keyword)

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword?'
    new_url = url + 'ServiceKey=' + key + '&keyword=' + hangul_utf8 + '&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  # 주소
        addr2 = item.find("addr2").text  # 동
        #areacode = item.find("areacode").text  # 지역번호
        mapx = item.find("mapx").text  # x좌표
        mapy = item.find("mapy").text  # y좌표
        title = item.find("title").text  # 관광지 지역이름
        #tel = item.find("tel").text #전화번호
        #createdtime = item.find("createdtime").text  # 등록일

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        print("detailed address : ", addr2)
        #print("areacode : ", areacode)
        print("GPS x : ", mapx)
        print("GPS y : ", mapy)
        #print("tel  : ", tel)
        #print("createdtime : ", createdtime)
        print("=========================================")


#키워드 검색
def FindingKeyword():
    keyword = str(input("Keyword : "))
    hangul_utf8 = urllib.parse.quote(keyword)

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword?'
    new_url = url + 'ServiceKey='+ key + '&keyword=' + hangul_utf8 + '&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  #주소
        #addr2 = item.find("addr2").text #동
        areacode = item.find("areacode").text #지역번호
        mapx = item.find("mapx").text #x좌표
        mapy = item.find("mapy").text #y좌표
        title = item.find("title").text # 관광지 지역이름
        #tel = item.find("tel").text #전화번호
        createdtime = item.find("createdtime").text #등록일

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        #print("detailed address : ", addr2)
        print("areacode : ", areacode)
        print("GPS x : ", mapx)
        print("GPS y : ", mapy)
        #print("tel  : ", tel)
        print("createdtime : " , createdtime)
        print("=========================================")


#행사검색
def SearchFestival():
    evejtstartDate = str(input("start date : "))
    eventEndDate = str(input("end date : "))
    arrange = str(input("sorting (A=title, B=look, C=change, D=create date): " ))


    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?'
    new_url = url + 'ServiceKey='+ key + '&eventStartDate=' + evejtstartDate + '&eventEndDate=' + eventEndDate + '&arrange=' + arrange + 'listYN=Y&pageNo=1&numOfRows=10&MobileOS=ETC&MobileApp=AppTesting'
    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  #주소
        addr2 = item.find("addr2").text #동
        areacode = item.find("areacode").text #지역번호
        mapx = item.find("mapx").text #x좌표
        mapy = item.find("mapy").text #y좌표
        title = item.find("title").text # 관광지 지역이름
        #tel = item.find("tel").text #전화번호
        createdtime = item.find("createdtime").text #등록일
        eventstartdate = item.find("eventstartdate").text #행사시작일
        eventenddate = item.find("eventenddate").text #행사종료일

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        print("detailed address : ", addr2)
        print("eventstartdate : ", eventstartdate)
        print("eventenddate : ", eventenddate)
        print("areacode : ", areacode)
        print("GPS x : ", mapx)
        print("GPS y : ", mapy)
        #print("tel  : ", tel)
        print("createdtime : " , createdtime)
        print("=========================================")


def SearchNear():
    print("#&mapX=126.981611&mapY=37.568477&radius=1000")
    mapX = str(input("Position x : "))
    mapY = str(input("Position y : "))
    radius = str(input("radius (m) : "))
    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/locationBasedList?'
    new_url = url + 'ServiceKey=' + key + '&mapX=' + mapX + '&mapY=' + mapY + '&radius=' + radius + '&pageNo=1&numOfRows=10&listYN=Y&arrange=A&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  # 주소
        addr2 = item.find("addr2").text  # 동
        areacode = item.find("areacode").text  # 지역번호
        mapx = item.find("mapx").text  # x좌표
        mapy = item.find("mapy").text  # y좌표
        title = item.find("title").text  # 관광지 지역이름
        # tel = item.find("tel").text #전화번호
        createdtime = item.find("createdtime").text  # 등록일
        dist = item.find("dist").text

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        print("detailed address : ", addr2)
        print("areacode : ", areacode)
        print("GPS x : ", mapx)
        print("GPS y : ", mapy)
        # print("tel  : ", tel)
        print("createdtime : ", createdtime)
        print("dist(m) : ", dist)
        print("=========================================")


def SearchStay():

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchStay?'
    new_url = url + 'ServiceKey=' + key + '&goodstay=1'  + '&arrange=A&listYN=Y&pageNo=1&numOfRows=10&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  # 주소
        #addr2 = item.find("addr2").text  # 동
        #areacode = item.find("areacode").text  # 지역번호
        mapx = item.find("mapx").text  # x좌표
        mapy = item.find("mapy").text  # y좌표
        title = item.find("title").text  # 관광지 지역이름
        # tel = item.find("tel").text #전화번호
        #createdtime = item.find("createdtime").text  # 등록일
        #dist = item.find("dist").text

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        #print("detailed address : ", addr2)
        #print("areacode : ", areacode)
        print("GPS x : ", mapx)
        print("GPS y : ", mapy)
        # print("tel  : ", tel)
        #print("createdtime : ", createdtime)
        #print("dist(m) : ", dist)
        print("=========================================")


#상세정보
def detailCommon() :

    print("#&contentId=126508")
    contentId = str(input("contentId : "))

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?'
    new_url = url + 'ServiceKey=' + key + '&contentId='  + contentId + '&defaultYN=Y&addrinfoYN=Y&overviewYN=Y&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        addr1 = item.find("addr1").text  # 주소
        addr2 = item.find("addr2").text  # 동
        homepage = item.find("homepage").text  # 지역번호
        overview = item.find("overview").text  # x좌표
        #telname = item.find("telname").text
        title = item.find("title").text  # 관광지 지역이름

        print("=========================================")
        print("title : ", title)
        print("address : ", addr1)
        print("detailed address : ", addr2)
        print("homepage : ", homepage)
        print("overview  : ", overview)
        #print("telname : ", telname)
        # print("tel  : ", tel)
        print("overview : ", overview)
        print("=========================================")
