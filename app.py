from flask import Flask,render_template,request,redirect
app = Flask(__name__)
people=[{'name':'郑倩倩','chinese':'98','english':'100','math':'99'},
{'name':'刘铭浩','chinese':'100','english':'100','math':'100'},
{'name':'毛文亮','chinese':'95','english':'87','math':'90'},]


"""
class User:
    def __init__(self, username, email):
        self.email=email
        self.username=username
@app.route("/filter")#过滤器的使用,1 "|"管道符的使用，后连接使用的函数，前面是数据
def index():
    user=User(username="刘铭浩的网站",email="xx@qq.com")
    return render_template("filter.html",user=user)

@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return render_template("blog_detail.html",blog_id=blog_id,username="刘铭浩")
@app.route("/control")
def control_statement():
    age=19
    books=[{"name":"白乐欣","gender":"女"},{"name":"刘铭浩","gender":"男"}]
    return render_template("control.html",age=age,books=books)

@app.route("/child_1")#继承文件中extends函数，block的用法#把父模板的标题换掉，用这个，下面的不变
def child1():
    return render_template("child_1.html")
@app.route("/static")
def static_demo():
    return render_template("static.html")
"""
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        print("从服务器接收到的数据",username,password)
        return redirect('/admin')
    return render_template("login.html")
@app.route('/admin')
def admin():
    return render_template("admin.html",people=people)
@app.route('/add',methods=["GET","POST"])
def add():
    if request.method=="POST":
        username=request.form.get("username")
        chinese=request.form.get("chinese")
        math=request.form.get("math")
        english=request.form.get("english")
        print("从服务器接收到的数据",username,chinese,math,english)
        people.append({'name':username,'chinese':chinese,'english':english,'math':math})
        return redirect('/admin')
    return render_template("add.html")
@app.route('/delete')
def delete():
     print(request.method)
     username=request.args.get('name')
     for peo_2 in people:
         if peo_2['name']==username:
             people.remove(peo_2)
     return redirect('/admin')
@app.route('/change')
def change():
    username=request.args.get('name')
    for peo_2 in people:
        if peo_2['name']==username:
            return render_template('/change.html',people=peo_2)


if __name__ == '__main__':
    app.run(debug=True)















