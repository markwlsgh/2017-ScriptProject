from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib.request
import urllib


key = 'c03YHDs%2B02nwNGnfZZhdQ%2FKC9cED7eHY1%2FzWomZJ7fTb4VyTLJ%2B29l1111N33w6yEnXmGnVeK34wEcnFUMjSKg%3D%3D'

def Date_Showing_Parsing():
    COURSE_ID = str(input("�����ڽ� ���̵� �Է��ϼ��� : "))
    numOfRows = str(input("� ����Ͻǰǰ���? : "))
    CURRENT_DATE = str(input("���س�¥ : "))
    HOUR = str(input("���س�¥���� ��ð����� ��ȸ�Ͻǰǰ���? : "))

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
        tm = item.find("tm").text  #�����ð�
        courseId = item.find("courseId").text # �ڽ� ���̵�
        courseAreaId = item.find("courseAreaId").text #�ڽ� �������̵�
        courseAreaName = item.find("courseAreaName").text #�ڽ� �����̸�
        spotAreaId = item.find("spotAreaId").text # ������ �������̵�
        spotAreaName = item.find("spotAreaName").text # ������ �����̸�
        courseName = item.find("courseName").text # �ڽ���
        spotName = item.find("spotName").text # ��������
        thema = item.find("thema").text # �׸�
        th3 = item.find("th3").text # 3�ð� ���
        #maxTa = item.find("maxTa").text #�ְ���
        #minTa = item.find("minTa").text #�������
        wd = item.find("wd").text #ǳ��
        ws = item.find("ws").text #ǳ��
        sky = item.find("sky").text #�ϴû���
        rhm = item.find("rhm").text #����
        pop = item.find("pop").text #����Ȯ��
        #rn = item.find("rn").text   #������


        print("=========================================")
        print("���� �ð� : ", tm)
        print("�ڽ� �̸� : ", courseName)
        print("������ ���� �̸� : ", spotAreaName)
        print("������ �̸� : ", spotName)
        print("�׸� : ", thema)
        print("��� : ", th3)
        print("�ϴ� ���� : ", sky)
        print("ǳ�� : ", wd)
        print("ǳ�� : ", ws)
        print("���� : ", rhm)
        print("����Ȯ�� : ", pop)
        print("=========================================�n")


def Area_Showing_Parsing():

    COURSE_ID = str(input("�����ڽ� ���̵� �Է��ϼ��� : "))
    numOfRows = str(input("� ����Ͻǰǰ���? : "))
    CURRENT_DATE = str(input("���س�¥ : "))
    HOUR = str(input("���س�¥���� ��ð����� ��ȸ�Ͻǰǰ���? : "))

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
        tm = item.find("tm").text  # �����ð�
        courseId = item.find("courseId").text  # �ڽ� ���̵�
        courseAreaId = item.find("courseAreaId").text  # �ڽ� �������̵�
        courseAreaName = item.find("courseAreaName").text  # �ڽ� �����̸�
        spotAreaId = item.find("spotAreaId").text  # ������ �������̵�
        spotAreaName = item.find("spotAreaName").text  # ������ �����̸�
        courseName = item.find("courseName").text  # �ڽ���
        spotName = item.find("spotName").text  # ��������
        thema = item.find("thema").text  # �׸�
        uvIndex = item.find("uvIndex").text
        fdIndex = item.find("fdIndex").text
        plIndexSo = item.find("plIndexSo").text
        plIndexWeed = item.find("plIndexWeed").text
        plIndexCharm = item.find("plIndexCharm").text


        print("=========================================")
        print("���� �ð� : ", tm)
        print("�ڽ� �̸� : ", courseName)
        print("������ ���� �̸� : ", spotAreaName)
        print("������ �̸� : ", spotName)
        print("�׸� : ", thema)
        print("�ڿܼ� ���� : ", uvIndex)
        print("���ߵ����� : ", fdIndex )
        print("�ҳ��� �ɰ��� ���� : ", plIndexSo)
        print("���� �ɰ��� ���� : ", plIndexWeed)
        print("������ �ɰ��� ���� : ", plIndexCharm )

        print("=========================================�n")