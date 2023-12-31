# Ver. 나이스 API 사용 못할 때(2023에 실제 사용한) 
from flask import Flask, json, request, jsonify
import sys
import datetime
app = Flask(__name__)

@app.route('/schoolmeal', methods=['POST'])
def schoolmeal():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content = content.replace("\n","")
    print(content)
    today = datetime.date.today()
    tmrw = today + datetime.timedelta(days = 1)
    date_today = today.strftime("%Y%m%d")
    date_tmrw = tmrw.strftime("%Y%m%d")
    data1 = {
        '20231205':"급식 정보가 없습니다.",
        '20231206':"물밥(한우)\n쇠고기감자국\n마라로제찜닭\n삼색나물\n햄앤두부전\n김치류\n문어볼",
        '20231207':"강황밥\n도토리묵국\n감자매운조림\n돼지(LA)갈비찜\n아삭콩나물무침\n알타리무김치\n블랙컬치즈케익",
        '20231208':"달걀볶음밥\n유부국\n꽈리고추찜\n알배기쑥갓겉절이\n렌치샐러드\n랍스터버터구이\n김치류\n방울토마토",
        '20231209':"급식 정보가 없습니다.",
        '20231210':"급식 정보가 없습니다.",
        '20231211':"발아현미밥\n쇠고기미역국\n두절콩나물잡채\n파닭치킨\n배추김치\n애플파이\n블루베리주스",
        '20231212':"흑미밥\n닭곰탕(찹쌀)\n배떡누들떡볶이\n제육볶음\n채소달걀말이\n김치류\n포도쥬스",
        '20231213':"찰보리밥\n동태찌개\n동파육\n두부부침\n불닭팽이버섯\n김치류\n구슬톡톡",
        '20231214':"차조밥\n오징어호박찌개\n가지양념구이\n시래기볶음\n뿌링클치킨텐더\n김치류\n마카롱",
        '20231215':"차수수밥\n콩가루배추된장국\n브로콜리달걀찜\n고사리볶음\n닭채소볶음\n허니버터연근칩\n김치류",
        '20231216':"급식 정보가 없습니다.",
        '20231217':"급식 정보가 없습니다.",
        '20231218':"발아현미밥\n꼬치어묵우동국\n낙지볶음\n콘치즈함박\n김치류\n코코제로\n프렌치토스트",
        '20231219':"기장밥\n돈육김치찌개\n닭조림\n숙주오이무침\n새우호박전\n김치류",
        '20231220':"황포묵비빔밥\n콩나물무채된장국\n모듬소시지볶음\n김치류\n약고추장\n메이플피칸파이\n초코우유",
        '20231221':"찰보리밥\n쇠고기버섯국\n달걀장조림\n등갈비찜\n두부잡채\n김치류\n치즈인깨비핫도그",
        '20231222':"찹쌀밥\n볶음김치파스타\n브로콜리스프\n심쿵하트단무지\n회오리감자튀김\n닭봉고추장구이\n김치류\n올데이크리스마스케익",
        '20231223':"급식 정보가 없습니다.",
        '20231224':"급식 정보가 없습니다.",
        '20231225':"메리크리스마스~ !",
        '20231226':"찰보리밥\n파닭개장\n돈육간장불고기\n오징어실채마늘쫑볶음\n세발나물\n김치류\n귤",
        '20231227':"차조밥\n감자탕(묵은지)\n참나물무침\n애호박버섯볶음\n훈제오리숙주볶음\n김치류",
        '20231228':"찹쌀밥\n얼큰쇠고기무국\n닭찜\n김치전\n연유갈릭토스트\n베라아이스컵"
    }
    data2 = {
        '20231205':"급식 정보가 없습니다.",
        '20231206':"급식 정보가 없습니다.",
    }
    if content == "오늘 중식" or content == "오늘중식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : data1[date_today]
                        }
                    }
                ]
            }
        }
    elif content == "내일 중식" or content == "내일중식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : data1[date_tmrw]
                        }
                    }
                ]
            }
        }
    elif content == "오늘 석식" or content == "오늘석식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "급식 정보가 없습니다." #data2[date_today] 
                        }
                    }
                ]
            }
        }
    elif content == "내일 석식" or content == "내일석식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "급식 정보가 없습니다." #data2[date_tmrw]
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "잘못된 발화입니다.\n'도움말'을 보내서 발화 방법을 확인해주세요."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
