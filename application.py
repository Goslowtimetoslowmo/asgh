# Ver. 나이스 API 웹 크롤링해서 자동 불러올때(아직 추가 개발 필요)
from flask import Flask, request, jsonify
import requests
import sys
from bs4 import BeautifulSoup
import schedule
import datetime
import time

app = Flask(__name__)

@app.route("/")
def today_menu():
    def get_html(URL):
        _html = ""
        resp = requests.get(URL)
        if resp.status_code == 200:
            _html = resp.text
        return _html
    
    MMEAL_SC_CODE = 2 # 중식2 석식3 
    today = datetime.datetime.today()
    MLSV_YMD = today.strftime("%Y%m%d") # <= 오늘 날짜 불러오기
    
    URL = (
        "https://open.neis.go.kr/hub/mealServiceDietInfo?"
        "ATPT_OFCDC_SC_CODE=K10&SD_SCHUL_CODE=7800079&MMEAL_SC_CODE=%d&MLSV_YMD=%s" %(MMEAL_SC_CODE, MLSV_YMD) 
    )
    html_text = get_html(URL)
    soup = BeautifulSoup(html_text, features="xml") 
    dish_list = soup.find_all("DDISH_NM")
    
    if len(dish_list)==0:
        today_menu_message = "급식 정보가 없습니다."
    else:
        menu = dish_list[0].get_text().split('<br/>')
        for i in menu:
            today_menu_message = "오늘 급식\n"+i
    return today_menu_message

schedule.every().day.at("08:00").do(today_menu) # 08:00에 크롤링 갱신

while True:
    schedule.run_pending()
    time.sleep(1)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons" : ["오늘 급식", "내일 급식"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    today_menu_message = today_menu() # today_menu()에서 today_menu_message return값을 받음
    if content == "오늘 급식":

        dataSend = {
            "message": {
                "text": today_menu_message
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["오늘 급식", "내일 급식"]
            }
        }
    return jsonify(dataSend)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
