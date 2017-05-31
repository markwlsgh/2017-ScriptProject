from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib.request
import urllib


key = 'c03YHDs%2B02nwNGnfZZhdQ%2FKC9cED7eHY1%2FzWomZJ7fTb4VyTLJ%2B29l1111N33w6yEnXmGnVeK34wEcnFUMjSKg%3D%3D'

def Date_Showing_Parsing():
    COURSE_ID = str(input("관광코스 아이디를 입력하세요 : "))
    numOfRows = str(input("몇개 출력하실건가요? : "))
    CURRENT_DATE = str(input("기준날짜 : "))
    HOUR = str(input("기준날짜부터 몇시간까지 조회하실건가요? : "))

    global key
    url = 'http://newsky2.kma.go.kr/service/TourSpotInfoService/SpotShrtData?'
    new_url = url + 'serviceKey='+ key + '&HOUR=' +HOUR +'&COURSE_ID=' +COURSE_ID + '&pageNo=1' + '&startPage=1' + '&numOfRows=' + numOfRows + '&pageSize=10' +'&CURRENT_DATE=' + CURRENT_DATE

    data=urllib.request.urlopen(new_url).read()
    d=str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)

    for item in itemElements:
        tm = item.find("tm").text  #예보시간
        courseId = item.find("courseId").text # 코스 아이디
        courseAreaId = item.find("courseAreaId").text #코스 지역아이디
        courseAreaName = item.find("courseAreaName").text #코스 지역이름
        spotAreaId = item.find("spotAreaId").text # 관광지 지역아이디
        spotAreaName = item.find("spotAreaName").text # 관광지 지역이름
        courseName = item.find("courseName").text # 코스명
        spotName = item.find("spotName").text # 관광지명
        thema = item.find("thema").text # 테마
        th3 = item.find("th3").text # 3시간 기온
        #maxTa = item.find("maxTa").text #최고기온
        #minTa = item.find("minTa").text #최저기온
        wd = item.find("wd").text #풍향
        ws = item.find("ws").text #풍속
        sky = item.find("sky").text #하늘상태
        rhm = item.find("rhm").text #습도
        pop = item.find("pop").text #강수확률
        #rn = item.find("rn").text   #강수량


        print("=========================================")
        print("예보 시간 : ", tm)
        print("코스 이름 : ", courseName)
        print("관광지 지역 이름 : ", spotAreaName)
        print("관광지 이름 : ", spotName)
        print("테마 : ", thema)
        print("기온 : ", th3)
        print("하늘 상태 : ", sky)
        print("풍향 : ", wd)
        print("풍속 : ", ws)
        print("습도 : ", rhm)
        print("강수확률 : ", pop)
        print("=========================================굈")


def Area_Showing_Parsing():

    COURSE_ID = str(input("관광코스 아이디를 입력하세요 : "))
    numOfRows = str(input("몇개 출력하실건가요? : "))
    CURRENT_DATE = str(input("기준날짜 : "))
    HOUR = str(input("기준날짜부터 몇시간까지 조회하실건가요? : "))

    global key
    url = 'http://newsky2.kma.go.kr/service/TourSpotInfoService/SpotIdxData?'
    new_url = url +'serviceKey='+ key + '&CURRENT_DATE=' + CURRENT_DATE + '&HOUR=' + HOUR + '&COURSE_ID=' +COURSE_ID + '&pageNo=1&startPage=1'+ '&numOfRows=' + numOfRows + '&pageSize=3'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        tm = item.find("tm").text  # 예보시간
        courseId = item.find("courseId").text  # 코스 아이디
        courseAreaId = item.find("courseAreaId").text  # 코스 지역아이디
        courseAreaName = item.find("courseAreaName").text  # 코스 지역이름
        spotAreaId = item.find("spotAreaId").text  # 관광지 지역아이디
        spotAreaName = item.find("spotAreaName").text  # 관광지 지역이름
        courseName = item.find("courseName").text  # 코스명
        spotName = item.find("spotName").text  # 관광지명
        thema = item.find("thema").text  # 테마
        uvIndex = item.find("uvIndex").text
        fdIndex = item.find("fdIndex").text
        plIndexSo = item.find("plIndexSo").text
        plIndexWeed = item.find("plIndexWeed").text
        plIndexCharm = item.find("plIndexCharm").text


        print("=========================================")
        print("예보 시간 : ", tm)
        print("코스 이름 : ", courseName)
        print("관광지 지역 이름 : ", spotAreaName)
        print("관광지 이름 : ", spotName)
        print("테마 : ", thema)
        print("자외선 지수 : ", uvIndex)
        print("식중독지수 : ", fdIndex )
        print("소나무 꽃가루 지수 : ", plIndexSo)
        print("잡초 꽃가루 지수 : ", plIndexWeed)
        print("참나무 꽃가루 지수 : ", plIndexCharm )

        print("=========================================굈")