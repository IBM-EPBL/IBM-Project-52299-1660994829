#server side scripts


import sqlite3

from flask import Flask,request,render_template,flash,url_for,redirect;

app=Flask(__name__)

app.config['SECRET_KEY']='9\xd7\x00F\x9ab(D\x83\xa3#\xe6\xc9\x87^[\x07\xa1\xdd\xd5\xcfm\x1bh'

#code for home page
@app.route("/")
def fun():
    return render_template('Home.html')
#code for signup page
@app.route('/Signin/',methods=['POST','GET'])
def login():
    if request.method=="POST":
       #msg=request.form['msg']
       name = request.form.get("email")
       Pass = request.form.get('pass')
       if not name:
          print("invalid ")
          flash("Please enter  the email")
       if not Pass:
           print("invalid")
           flash("Please enter the password") 
       else:
            conn=sqlite3.connect("student.db")
            sql="SELECT * FROM Info Where name='{}' AND pass='{}' ".format(name,Pass)  
            cursor=conn.cursor()
            cursor.execute(sql)
            ans = cursor.fetchall()
            print(ans)
            print("@@@@@@@@@@@@@")
            print(name,Pass)
            print(type(ans))
            if len(ans)>=1:
              print("Success")
              return render_template("Welcome.html",name=name)
            else:
               flash("Invalid login")
            conn.commit()
            conn.close()

    return render_template("Signin.html") 
#code for signup process
@app.route("/Signup/",methods=['POST','GET'])
def signup():
    if request.method=='POST':
       print("request sent")
       name = request.form.get("email")
       Pass = request.form.get('pass')
       if not name:
          print("invalid ")
          flash("Please enter  the email")
       if not Pass:
           print("invalid")
           flash("Please enter the password") 
       else:
           print("###############"+name+Pass)
           conn=sqlite3.connect("student.db")
#b+","+a+")"  
           sql="INSERT INTO Info VALUES('{}','{}')".format(name,Pass)
           cursor=conn.cursor()
           cursor.execute(sql)
           conn.commit()
           print("####Success###")
           conn.close()
           flash("Signup successfull")
           #when the signup process sucess automatically it will be entered 
           #into welcome page
           return render_template("Welcome.html",name=name)
    return render_template("Signup.html")

@app.route('/About')

def about():
     print("Entered into about page")
     conn=sqlite3.connect("student.db")
     sql="SELECT name FROM Info "  
     cursor=conn.cursor()
     cursor.execute(sql)
     ans = cursor.fetchall()
     print(ans)
     for i in ans:
        print(i[0])
        flash(i[0])
     return render_template('About.html')    
if __name__=="__main__":
    app.run(host="127.0.0.1",port=5271,debug=True)
