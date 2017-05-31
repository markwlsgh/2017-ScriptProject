# -*- coding: cp949 -*-
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request

##global
conn = None
regKey = '4VB0o7ZOlNdClfP%2FidH3cNjCCsAfg3APKmEf7Tqg4aS2uPSNn1pA2avCeTcqVVY4pV6I7252637lX8LFUtxXJQ%3D%3D'

server =  "newsky2.kma.go.k"

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
port = "587"
#&HOUR=24&COURSE_ID=1&pageNo=1&startPage=1&numOfRows=10&pageSize=10&CURRENT_DATE=2016120101
def FindingWhere():
    uri = userURIBuilder(server, ServiceKey=regKey, HOUR='24',COURSE_ID='1',  pageNo = '1', numOfRows='1',pageSize='10',CURRENT_DATE='2016120101' )  # ���� �˻� URL

    data = urllib.request.urlopen(uri).read()

    d = str(data, "utf-8")

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    #print(d)
    itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)
    for item in itemElements:
        Cityname = item.find("spotName").text
        Citycode = item.find("thema").text
        print("=========================================")
        print("Cityname : ", Cityname)
        print("CityCode : ", Citycode)
        print("=========================================�n")


def userURIBuilder(server, **user):  # ** ������ ���������� ���� ����
    # str = "http://" + server + "/search" + "?" #���̹��˻� URI
    str = "http://" + server + "/service/TourSpotInfoService/SpotIdxData" + "?"  # �����˻� URI
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getBusDataFromCitycode(citycode):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
        # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, ServiceKey=regKey, cityCode='25', routeId='DJB3030052ND')  # ���� �˻� URL
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)

    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractBookData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book ������Ʈ�� �����ɴϴ�.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        citycode = item.find("citycode")
        cityname = item.find("cityname")
        print(cityname)
        if len(cityname.text) > 0:
            return {"citycode": citycode.text, "cityname": cityname.text}


def sendMain():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    msgtext = str(input('write message :'))
    passwd = str(input(' input your password of gmail account :'))
    msgtext = str(input('Do you want to include book data (y/n):'))
    if msgtext == 'y':
        keyword = str(input('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))

    import mysmtplib
    # MIMEMultipart�� MIME�� �����մϴ�.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container�� �����մϴ�.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # �޼����� ������ MIME ������ ÷���մϴ�.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # �α��� �մϴ�.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword�� �ش��ϴ� å�� �˻��ؼ� HTML�� ��ȯ�մϴ�.
            ##��� �κ��� �ۼ�.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # ����( body ) �κ��� ��� �մϴ�.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # �� ���� ��û��� ������ �����Ѵ�.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server �����մϴ�.


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True
