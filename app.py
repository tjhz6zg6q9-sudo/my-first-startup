from flask import Flask, render_template, request

app = Flask(__name__)

# 1. 這是首頁路由：當有人連上網址，我們把 index.html 丟給他
@app.route('/')
def index():
    return render_template('index.html')

# 2. 這是表單處理路由：接收來自 HTML 表單的資料
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    
    # --- 新增儲存邏輯 ---
    # 使用 'a' (append) 模式，代表「把新資料附加在檔案末尾」
    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(f"姓名: {name}, 信箱: {email}\n")
    # ------------------

    print(f"成功存檔：{name}")
    return f"感謝您，{name}！您的資料已成功存入我們的系統。"
if __name__ == '__main__':
    # 換成 5001，這樣絕對不會跟 Mac 內建的 AirPlay 衝突
    app.run(debug=True, port=5001)

