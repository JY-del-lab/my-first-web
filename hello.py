import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # 1. 냉장고(DB)를 열어서 데이터를 가져옵니다.
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    row = cursor.fetchone() # 데이터 한 줄 가져오기
    conn.close()
    
    # 2. 웹브라우저에 보여줄 화면을 꾸밉니다.
    if row:
        return f"<h1>나의 첫 웹사이트</h1><p>DB에서 꺼낸 정보 -> 이름: {row[0]}, 나이: {row[1]}세</p>"
    else:
        return "<h1>나의 첫 웹사이트</h1><p>아직 데이터가 없습니다.</p>"

if __name__ == '__main__':
    # 웹 서버를 실행합니다.
    app.run(debug=True)