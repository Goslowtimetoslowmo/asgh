from flask import Flask, request

app = Flask(__name__) # Flask app 생성

# 자세한 설명: https://dschloe.github.io/python/kakao_chatbot/chatbot_calculator/

@app.route('/') # main page route
def test2(): # main page function
    return "test2" # main page return

@app.route('/api/test', methods=['POST']) # api/test page route
def test():
    body = request.get_json() # request body
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "test message"
                    }
                }
            ]
        }
    }
    return responseBody # return response body

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) # run flask
