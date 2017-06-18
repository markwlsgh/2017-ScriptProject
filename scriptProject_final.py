from tkinter import *
from tkinter import font
from internet import *

import folium
import urllib.request
import urllib
import smtplib
from tkinter import*
from tkinter import *
from tkinter import font
from internet import *
import os
import folium
import urllib.request
import urllib
import smtplib
from tkinter import*
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
from email.mime.text import MIMEText

import spam

key = '4VB0o7ZOlNdClfP%2FidH3cNjCCsAfg3APKmEf7Tqg4aS2uPSNn1pA2avCeTcqVVY4pV6I7252637lX8LFUtxXJQ%3D%3D'
pageNum = 1
totalCount = 0
keywordOn = 0
festivalOn = 0
onoff = 0
######################################################################################## tkinter 구현부분
g_Tk = Tk()
g_Tk.geometry("950x550+300+100")
DataList = []

mainImageUrl="http://cfile25.uf.tistory.com/image/171C0E334E2690BC2D8EF9"
with urllib.request.urlopen(mainImageUrl) as u:
    raw_data=u.read()

mainIm=Image.open(BytesIO(raw_data))
mainImage=ImageTk.PhotoImage(mainIm)

mainImageLabel=Label(g_Tk,image=mainImage,height=800,width=1000)
mainImageLabel.pack()
mainImageLabel.place(x=0,y=100)


subMainurl="http://tourkorea.org/img/6.jpg"
with urllib.request.urlopen(subMainurl) as u:
    raw_data=u.read()

subMainim=Image.open(BytesIO(raw_data))
subMainimage=ImageTk.PhotoImage(subMainim)

subMainlabel=Label(g_Tk,image=subMainimage,height=200,width=1000)
subMainlabel.pack()
subMainlabel.place(x=0,y=-100)



def InitTopText():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SubText = Label(g_Tk, font=TempFont, text="2013180015 변경민\n2013180017 석진호")
    SubText.pack()
    SubText.place(x=790, y= 500)
    global titlebox
    titlebox = Text(g_Tk, width=33, height=5, borderwidth=3, relief='solid')
    titlebox.pack()
    titlebox.place(x=360, y=0)

    titlebox.configure(state='disabled')
    TempFont = font.Font(g_Tk, size=30, weight='normal', family = '휴먼매직체')
    MainText = Label(g_Tk, font = TempFont, text="관광정보 검색")
    MainText.pack()
    MainText.place(x=370,y=15)




def InitSearchListBox():
    global SearchListBox

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='휴먼매직체')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=0, height=0, borderwidth=3, relief='solid')

    SearchListBox.insert(1, "키워드")
    SearchListBox.insert(2, " 행사 ")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=65)


#검색창
def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = '휴먼매직체')
    InputLabel = Entry(g_Tk, font = TempFont, width = 12, borderwidth = 4, relief = 'solid')
    InputLabel.pack()
    InputLabel.place(x=60, y=68)

#상세정보 버튼
def InitDetailButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="상세 정보",  command=detailedKeyword)
    SearchButton.pack()
    SearchButton.place(x=95, y=475)

#페이지 버튼
def InitPageButtonPrev():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="이전",  command=PrevPage)
    SearchButton.pack()
    SearchButton.place(x=15, y=475)
def InitPageButtonNext():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="다음",  command=NextPage)
    SearchButton.pack()
    SearchButton.place(x=215, y=475)

#이메일 버튼
def InitEmailButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="이메일 보내기",  command=emailAction)
    SearchButton.pack()
    SearchButton.place(x=675, y=425)

#지도 버튼
def InitmapButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="지도 보기",  command=mapAction)
    SearchButton.pack()
    SearchButton.place(x=675, y=375)

#검색버튼
def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='normal', family = '휴먼매직체')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=220, y=68)

#검색 버튼 동작
def SearchButtonAction():
    global SearchListBox , keywordOn , festivalOn,pageNum

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    RenderText2.delete(0,END)
    pageNum = 1
    iSearchIndex = SearchListBox.curselection()[0]  # 由ъ뒪?몃컯???몃뜳??媛?몄삤湲?

    if iSearchIndex == 0:  # ?꾩꽌愿
        FindingKeyword()
        keywordOn = 1
        festivalOn = 0
    elif iSearchIndex == 1:  # 紐⑤쾾?뚯떇
        SearchFestival()
        keywordOn = 0
        festivalOn = 1

    RenderText.configure(state='disabled')

#상세 정보 뜨게하는 창
def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=0,y=0)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=55, height=27, borderwidth=3, relief='solid', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=275, y=110)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

######################

#제목만 뜨게하는것
def InitRenderText2():
        global RenderText2

        RenderTextScrollbar = Scrollbar(g_Tk)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=90)

        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RenderText2 = Listbox(g_Tk, font=TempFont, activestyle='none',
                                width=33, height=22, borderwidth=5, relief='solid',
                                yscrollcommand=RenderTextScrollbar.set)

        RenderText2.pack()
        RenderText2.place(x=10, y=110)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        #RenderText.configure(state='disabled')
###########################################################################################################################기능함수 부분

#키워드 검색 제목만 뜨기
def FindingKeyword():
    keyword = InputLabel.get()

    hangul_utf8 = urllib.parse.quote(keyword)

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword?'
    new_url = url + 'ServiceKey=' + key + '&keyword=' + hangul_utf8 + '&listYN=Y&pageNo=' + str(pageNum)  + '&numOfRows=20&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    global itemList
    itemNum = 1
    itemList = []
    for item in itemElements:
        if item.find("title") != None:
            title = item.find("title").text  # ������ �����̸�
            RenderText2.insert(itemNum, title)
            itemNum += 1
        if item.find("contentid") != None:
            contentid = item.find("contentid").text
            itemList.append(contentid)


        RenderText.insert(INSERT, "\n")
#행사검색
def SearchFestival():
    eventEndDate = str(spam.returnNowTime())

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?'
    new_url = url + 'ServiceKey=' + key + '&eventStartDate=20170101&eventEndDate=' + eventEndDate + '&arrange=A&listYN=Y&pageNo='+ str(pageNum) +'&numOfRows=20&MobileOS=ETC&MobileApp=AppTesting'
    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    global itemList, totalCount
    itemNum = 1
    itemList = []
    for item in itemElements:
        if item.find("title") != None:
            title = item.find("title").text  # ������ �����̸�
            RenderText2.insert(itemNum, title)
            itemNum += 1
        if item.find("contentid") != None:
            contentid = item.find("contentid").text
            itemList.append(contentid)

        RenderText.insert(INSERT, "\n")

##버튼 함수
def PrevPage():
    global pageNum , keywordOn,festivalOn
    if pageNum > 1:
        pageNum -= 1
        #RenderText.delete(0, END)
        RenderText2.delete(0,END)
    if (keywordOn == 1):
        FindingKeyword()
    else:
        SearchFestival()
def NextPage():
    global pageNum
    pageNum += 1
    #RenderText.delete(0,END)
    RenderText2.delete(0, END)
    if (keywordOn == 1):
        FindingKeyword()
    else:
        SearchFestival()

#키워드 검색 상세정보
def detailedKeyword():
    global onoff
    onoff += 1
    keyword = itemList[RenderText2.curselection()[0]]
    hangul_utf8 = urllib.parse.quote(keyword)

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex2 = RenderText2.curselection()[0]  # 由ъ뒪?몃컯???몃뜳??媛?몄삤湲?

    global key
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?'
    new_url = url + 'ServiceKey=' + key + '&contentId='  + hangul_utf8 + '&firstImageYN=Y&defaultYN=Y&addrinfoYN=Y&overviewYN=Y&mapinfoYN=Y&MobileOS=ETC&MobileApp=AppTesting'

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("item")  # return list type
    # print(itemElements)

    for item in itemElements:
        if item.find("title") != None:
            title = item.find("title").text  # ������ �����̸�
            RenderText.insert(INSERT,"이 름 : " )
            RenderText.insert(INSERT, title)
            RenderText.insert(INSERT, "\n")
        if item.find("addr1") != None:
            addr1 = item.find("addr1").text  # �ּ�
            RenderText.insert(INSERT, "주 소 : ")
            RenderText.insert(INSERT, addr1)
            RenderText.insert(INSERT, "\n")
        if item.find("addr2") != None:
            addr2 = item.find("addr2").text  # ��
            RenderText.insert(INSERT, "상세 주소 : ")
            RenderText.insert(INSERT, addr2)
            RenderText.insert(INSERT, "\n")
        if item.find("zipcode") != None:
            areacode = item.find("zipcode").text  # ������ȣ
            RenderText.insert(INSERT, "우편 번호 : ")
            RenderText.insert(INSERT, areacode)
            RenderText.insert(INSERT, "\n")

        if item.find("tel") != None:
            tel = item.find("tel").text  # ��ȭ��ȣ
            RenderText.insert(INSERT, "전화번호 : ")
            RenderText.insert(INSERT, tel)
            RenderText.insert(INSERT, "\n")

        if item.find("overview") != None:
            overview = item.find("overview").text  # �����
            RenderText.insert(INSERT, "개요 : ")
            RenderText.insert(INSERT, overview)
            RenderText.insert(INSERT, "\n")

        if item.find("homepage") != None:
            homepage = item.find("homepage").text  # x��ǥ
            RenderText.insert(INSERT, "홈페이지 주소 : ")
            RenderText.insert(INSERT, homepage)
            RenderText.insert(INSERT, "\n")

        if item.find("mapx") != None:
            mapx = item.find("mapx").text  # y��ǥ
        if item.find("mapy") != None:
            mapy = item.find("mapy").text  # y��ǥ

        map_osm = folium.Map(location=[mapy, mapx], zoom_start=13)
        folium.Marker([mapy, mapx], popup='Mt. Hood Meadows').add_to(map_osm)
        map_osm.save('지도 위치.html')

        RenderText.insert(INSERT, "\n")

        global image
        image = None
        if item.find("firstimage") != None:

            firstimage2 = item.find("firstimage2").text  # �����
            with urllib.request.urlopen(firstimage2) as u:
                raw_data = u.read()

            im = Image.open(BytesIO(raw_data))
            image = ImageTk.PhotoImage(im)

            label = Label(g_Tk, image=image, height=200, width=220)
            label.pack()
            label.place(x=683, y=115)
            g_Tk.mainloop()

def Initimagebox():
    global Imagebox

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    Imagebox = Text(g_Tk, width=33, height=16, borderwidth=3, relief='solid')
    Imagebox.pack()
    Imagebox.place(x=675, y=110)

    Imagebox.configure(state='disabled')


def emailAction():
    global InputmailLabel, InputpasswdLabel, InputymailLabel
    g_Tk2 = Tk()
    g_Tk2.geometry("500x400+400+200")
    DataList2 = []

    TempFont = font.Font(g_Tk2, size=10, weight='bold', family='휴먼매직체')
    MailText = Label(g_Tk2, font=TempFont, text="이메일 입력")
    MailText.pack()
    MailText.place(x=20, y= 30)

    TempFont = font.Font(g_Tk2, size=15, weight='bold', family='휴먼매직체')
    InputmailLabel = Entry(g_Tk2, font=TempFont, width=26, borderwidth=12, relief='solid')
    InputmailLabel.pack()
    InputmailLabel.place(x=20, y=60)

    TempFont = font.Font(g_Tk2, size=10, weight='bold', family='휴먼매직체')
    MailText = Label(g_Tk2, font=TempFont, text="비밀번호 입력")
    MailText.pack()
    MailText.place(x=20,y =130)

    TempFont = font.Font(g_Tk2, size=15, weight='bold', family='휴먼매직체')
    InputpasswdLabel = Entry(g_Tk2, font=TempFont, width=26, borderwidth=12, relief='solid')
    InputpasswdLabel.pack()
    InputpasswdLabel.place(x=20, y=160)

    TempFont = font.Font(g_Tk2, size=10, weight='bold', family='휴먼매직체')
    MailText = Label(g_Tk2, font=TempFont, text="받을 사람 이메일 입력")
    MailText.pack()
    MailText.place(x=20, y = 230)

    TempFont = font.Font(g_Tk2, size=15, weight='bold', family='휴먼매직체')
    InputymailLabel = Entry(g_Tk2, font=TempFont, width=26, borderwidth=12, relief='solid')
    InputymailLabel.pack()
    InputymailLabel.place(x=20, y=260)

    TempFont = font.Font(g_Tk2, size=12, weight='bold', family='휴먼매직체')
    SearchButton = Button(g_Tk2, font=TempFont, text="메일 보내기", command=EmailButtonAction)
    SearchButton.pack()
    SearchButton.place(x=200, y=360)



def EmailButtonAction():
        keyword = itemList[RenderText2.curselection()[0]]
        hangul_utf8 = urllib.parse.quote(keyword)

        RenderText.configure(state='normal')
        RenderText.delete(0.0, END)
        iSearchIndex2 = RenderText2.curselection()[0]  # 由ъ뒪?몃컯???몃뜳??媛?몄삤湲?

        global key
        url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?'
        new_url = url + 'ServiceKey=' + key + '&contentId=' + hangul_utf8 + '&firstImageYN=Y&defaultYN=Y&addrinfoYN=Y&overviewYN=Y&mapinfoYN=Y&MobileOS=ETC&MobileApp=AppTesting'

        data = urllib.request.urlopen(new_url).read()
        d = str(data.decode('utf-8'))

        from xml.etree import ElementTree
        tree = ElementTree.fromstring(d)

        itemElements = tree.getiterator("item")  # return list type

        # InputmailLabel, InputpasswdLabel, InputymailLabel
        mymail = str(InputmailLabel.get())
        mypasswd = str(InputpasswdLabel.get())
        yourmail = str(InputymailLabel.get())

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        textfile = u"행사 정보.txt"
        testfile = open(textfile, 'w')
        for item in itemElements:
            if item.find("title") != None:
                title = item.find("title").text  # ������ �����̸�
                testfile.write('<br>\n행사 이름: ' + title)

            if item.find("addr1") != None:
                addr1 = item.find("addr1").text  # �ּ�
                testfile.write('<br>\n주소: ' + addr1)

            if item.find("addr2") != None:
                addr2 = item.find("addr2").text  # ��
                testfile.write('<br>\n상세 주소: ' + addr2)

            if item.find("zipcode") != None:
                zipcode = item.find("zipcode").text  # ������ȣ
                testfile.write('<br>\n우편 번호 : ' + zipcode)

            if item.find("overview") != None:
                overview = item.find("overview").text  # x��ǥ
                testfile.write('<br>\n개 요 : ' + overview)

            if item.find("tel") != None:
                tel = item.find("tel").text  # ��ȭ��ȣ
                testfile.write('<br>\n전화번호: ' + tel)

            if item.find("homepage") != None:
                homepage = item.find("homepage").text  # �����
                testfile.write('<br>\n홈페이지 주소: ' + homepage)

            if item.find("firstimage") != None:
                firstimage = item.find("firstimage").text  # �����
                testfile.write('<br>\n이미지 주소: ' + firstimage)

        testfile.close()
        # myid = str(input('발신자의 이메일 아이디를 입력해 주세요'))
        # mypasswd = str(input('비밀번호를 입력해 주세요'))
        s.login(mymail, mypasswd)
        fp = open(textfile, 'rb')
        msg = MIMEText(fp.read(), "html", _charset="utf-8")
        me = mymail
        you = yourmail

        msg['Subject'] = '요청한 정보 입니다.'
        msg['From'] = me
        msg['To'] = you
        s.sendmail(me, you, msg.as_string())
        s.quit()

def mapAction():
    global onoff
    if onoff >= 1:
        os.startfile('지도 위치.html')

##############################
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitRenderText2()
InitDetailButton()
InitEmailButton()
InitPageButtonPrev()
InitPageButtonNext()
Initimagebox()
InitmapButton()

#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()