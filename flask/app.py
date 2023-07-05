from flask import Flask ,render_template, url_for ,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname= db.Column(db.String(120),  nullable=False)
    collegename= db.Column(db.String(120),  nullable=False)
    city= db.Column(db.String(120),  nullable=False)
    address= db.Column(db.String(120),  nullable=False)
    contact= db.Column(db.String(120),  nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.firstname

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="POST":
       firstn=request.form.get('fname')
       secondn=request.form.get('lname')
       collegename=request.form.get('college')
       city=request.form.get('city')
       address=request.form.get('address')
       contact=request.form.get('phonenumb')
       email=request.form.get('email')
       user=User(firstname=firstn,lastname=secondn,collegename=collegename,city=city,address=address,contact=contact,email=email)
       db.session.add(user)
       db.session.commit()
       return("login successfuly")
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug = True)