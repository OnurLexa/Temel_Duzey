from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    print(f"Username: {username}, Password: {password}") # giris bilgilerini konsola yazdır
    return "giris bilgileri kaydedildi"

if __name__ == '__main__':
    app.run(debug=True)
