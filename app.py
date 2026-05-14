from flask import Flask, render_template, request

app = Flask(__name__)

# --- 1. 首頁 ---
@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, render_template, request

app = Flask(__name__)

# --- 1. 首頁 ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 1. 從表單抓取資料 (確保名稱與 HTML 裡的 name 一致)
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')  # <-- 這是新增的！
    
    # 2. 儲存資料到檔案 (把意見也寫進去)
    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(f"姓名: {name}, 信箱: {email}, 意見: {message}\n")

    print(f"成功存檔：{name}")
    return f"感謝您，{name}！您的資料與意見已成功存入我們的系統。"

# --- 3. 秘密後門 (這段原本在下面，現在要搬到這裡！) ---
@app.route('/secret-view')
def view_data():
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return f"<pre>{content}</pre>" 
    except FileNotFoundError:
        return "目前還沒有任何資料喔！"

# --- 4. 啟動引擎 (必須放在最後一行) ---
if __name__ == '__main__':
    app.run(debug=True, port=5001)