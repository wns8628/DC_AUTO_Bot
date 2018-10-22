# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLabel ,QWidget ,QVBoxLayout, QDesktopWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
import configparser


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 600)
        Dialog.setWindowIcon(QIcon('./venv/Include/logo.ico'))

        self.gridLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 20, 611, 551))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.title_text = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.title_text.setObjectName("title_text")
        self.gridLayout_4.addWidget(self.title_text, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pw_text = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.pw_text.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pw_text.setObjectName("pw_text")
        self.gridLayout.addWidget(self.pw_text, 2, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.id_text = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.id_text.setMaximumSize(QtCore.QSize(100, 16777215))
        self.id_text.setObjectName("id_text")
        self.gridLayout.addWidget(self.id_text, 1, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.post_btn = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.post_btn.setObjectName("post_btn")
        self.gridLayout_2.addWidget(self.post_btn, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 2)
        self.go_btn = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.go_btn.setObjectName("go_btn")
        self.gridLayout_5.addWidget(self.go_btn, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.des_text = QtWidgets.QTextEdit(self.gridLayoutWidget_5)
        self.des_text.setObjectName("des_text")
        self.gridLayout_5.addWidget(self.des_text, 2, 0, 1, 3)
        self.gridLayout_6.addLayout(self.gridLayout_5, 3, 0, 1, 2)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        # 여기는 이벤트달자 --------------------------------------------------------------------------------------------------------
        self.post_btn.clicked.connect(self.Post_select)
        self.go_btn.clicked.connect(self.go)

    # 이벤트처리함수들 정의 ㅇㅋ?----------------

    # 게시판선택누를시 이거뜸
    def Post_select(self):
        self.setWindowTitle('게시판 선택')
        self.setGeometry(300, 300, 300, 200)

        pots_label = QLabel('인기갤러리 top 15곳 돌아가면서합니다. 곧 설정추가하겠습니다.', self)
        layout = QVBoxLayout()
        layout.addWidget(pots_label)
        self.setLayout(layout)
        self.center()
        self.show()

    def center(self): #화면중간맞추기
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#----실행클릭시-------------------------------
    def go(self):

        id_text = self.id_text.text()    #아이디
        pw_text = self.pw_text.text()    #비번
        title = self.title_text.text()   # 제목적은거 이변수에담아서 제목에 넣는거지
        des_text = self.des_text.toPlainText()   # 이건 본문

        Config = configparser.ConfigParser()

        id = id_text
        pw = pw_text
        nos = 1

        URL = [  # "http://gall.dcinside.com/board/write/lists/?id=comic_new1",
            "http://gall.dcinside.com/board/write/?id=ib_new",  # 인방.
            "http://gall.dcinside.com/board/write/?id=fashion_new1",
            "http://gall.dcinside.com/board/write/lists/?id=baseball_new7&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=idolmaster&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=leagueoflegends2&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=iu_new&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=tigers_new&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=soulworker&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=produce48&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=twice&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=drama_new2&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=hanwhaeagles_new&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=exam_new&page=1",
            "http://gall.dcinside.com/board/write/lists/?id=kancolle&page=1",
            "http://gall.dcinside.com/board/write/lists?id=fantasy_new",
            "http://gall.dcinside.com/board/write/lists/?id=stock_new2&exception_mode=recommend",
            "http://gall.dcinside.com/board/write/lists/?id=cartoon&exception_mode=recommend"
        ]

        GALL = ["http://gall.dcinside.com/board/lists?id=essay"]
        options = webdriver.ChromeOptions()

        def nologin_auto(URL, nos):

            # headless 모드
            # options.add_argument('headless')
            # options.add_argument('window-size=1920x1080')
            # options.add_argument("disable-gpu")

            # user-agent 변경
            options.add_argument(
                "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
            # 크롬 드라이버 로드
            driver = webdriver.Chrome('./venv/Include/chromedriver', chrome_options=options)

            driver.implicitly_wait(3)

            # 글쓰기 페이지 로드
            driver.get(URL)
            time.sleep(3)

            # 로그인 구간
            driver.find_element_by_name('name').send_keys(id)
            driver.find_element_by_name('password').send_keys(pw)
            # driver.find_element_by_id('login_ok').click()

            # 글작성 페이지 로드
            # driver.get(GALL)

            # 글작성 구간
            driver.find_element_by_name('subject').send_keys(title + str(nos))       #제목

            time.sleep(3)
            driver.find_element_by_id("tx_switchertoggle").click();
            time.sleep(1)

            driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))

            driver.find_element_by_tag_name("body").send_keys(des_text + str(nos))                                #본문

            driver.switch_to_default_content()

            # 작성완료버튼
            # driver.find_element_by_xpath(
            #     "//input[@src='http://nstatic.dcinside.com/dgn/gallery/images/btn_save.gif']").click()
            driver.find_element_by_class_name("btn_blue").click()


            time.sleep(8)
            driver.quit()

        for j in range(0, 8):  # 0 < 2 즉 0,1두번반복
            for i in range(0, 17):
                nologin_auto(URL[i], nos)
            nos = nos + 1
            time.sleep(1800)

    #----------------------------------------

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "디시 갤러리 자동글쓰기 프로그램"))
        self.label_4.setText(_translate("Dialog", "제목:"))
        self.label_2.setText(_translate("Dialog", "PW:"))
        self.label.setText(_translate("Dialog", "ID:"))
        self.label_3.setText(_translate("Dialog", "* 익명으로 올릴 아이디,비번 지정                                   "))
        self.post_btn.setText(_translate("Dialog", "게시판 선택"))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p>* 본문에 이미지는 태그형식으로 넣으면 됩니다. ex : &lt;img&gt; 태그 </p></body></html>"))
        self.label_5.setText(_translate("Dialog", "본문"))
        self.go_btn.setText(_translate("Dialog", "실행"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ex = MyApp()
    # ex.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

