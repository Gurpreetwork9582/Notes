from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#database model(data class)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),nullable=False, unique=True)
    password =db.Column(db.String(100),nullable=False)
    
    
    def __repr__(self):
        return f"{self.id}"    


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        current_email=request.form['email']
        current_password=request.form['password']
        
        new_Account=User(email=current_email, password=current_password)
        try:
            db.session.add(new_Account)
            db.session.commit()
            return redirect("/")

        except Exception as e:
            print(f"Error:{e}")
            return f"{e}"
            
    else:
        Accounts = User.query.order_by(User.id).all()
        return render_template('index.html', Accounts=Accounts)
            

@app.route("/delete/<int:id>")
def delete(int:id):
    deletuser=User.query.get_or_404(id)
    try:
        db.session.delete(deletuser)
        db.session.commit()
        return redirect("/")
    except Exception:
        return f"Error {Exception}"    

@app.route("/Edit/<id>", methods= ["POST","GET"])
def Edit(id):
    edituser=User.query.get_or_404(id)
    if request.method == "POST":
        edituser.email=request.form['email']
        try:
            db.session.commit()
            return redirect("/")
        
        except Exception:
            return f"Error {Exception}"
    
    else:
        return render_template('edit.html', user=edituser)




if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)