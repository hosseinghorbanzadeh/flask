from flask import Flask,request,url_for,redirect,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Date

app=Flask(__name__)
#app.secret_key = "Hossein722GH"
app.config['SECRET_KEY'] = 'the_random_string'
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://hossein:Passw0rd@localhost/ticket"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Employee(db.Model):
    __tablename__='employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    meliCode = db.Column(db.Integer, unique=True, nullable=False)
    dateOfBirth=db.Column(db.Date)
    fatherName=db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self,id,name,lastName,email,meliCode,dateOfBirth,fatherName,password):
        self.id=id
        self.name=name
        self.lastName=lastName
        self.email=email
        self.meliCode=meliCode
        self.dateOfBirth=dateOfBirth
        self.fatherName=fatherName
        self.password=password

@app.route('/')
def index():
         return render_template("login.html")


@app.route('/login',methods=['GET','POST'])
def Login():
      if request.method=='POST':
           id=request.form['id']
           password=request.form['password']
           EM = Employee.query.filter_by(id=id).first()
           em=Employee.query.get(id)
           if EM is None:
                SRTmsg=f"invalid equipment {id}"
                SRTmsg=f"نام کاربری {id}  موجود نیست"
                return jsonify({"error": SRTmsg}), 400
           if em.password!=password:
                return jsonify({"error": "رمز عبور اشتباه است!!"}), 400
                
           #return render_template('panel.html',name=em.name+' '+em.lastName)
           return render_template('panel.html',em=em)

@app.route('/data',methods=['POST'] )
def data():
    if request.method=='POST':
        id=request.form['id']
        name=request.form['name']
        lastName=request.form['lastName']
        email=request.form['email']
        meliCode=request.form['meliCode']
        dateOfBirth =request.form['dateOfBirth']
        fatherName=request.form['fatherName']
        password=request.form['password']
        em=Employee(id,name,lastName,email,meliCode,dateOfBirth,fatherName,password)
        db.session.add(em)
        db.session.commit()
        return f"Your name is:{name}"
    return "<h1> Data </h1>"
if __name__=='__main__':
        app.run(debug=True)
