from flask import Flask,request,render_template 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    flag = "Oops..." 
    name = "Hoge"
    if request.method == 'POST':
        name = request.headers.get('User-Agent')
        if 'admin' == request.headers.get('User-Agent') and 'garbage' == request.form["people"]:
            flag = "wizCTF{WIZ_z4QXaWKP}"
    
    
    return render_template('hello.html', title='販売停止しちゃったね', name=name, flag=flag) #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)