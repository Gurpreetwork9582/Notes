from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_migrate import Migrate




app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SECRET_KEY"] = "mysecretkey123"
db = SQLAlchemy(app)

login_manager=LoginManager() # handles all the login functionalities
login_manager.init_app(app) # initializing db with flask app
login_manager.login_view = "login" # if user not logged in send them to login fuction


migrate = Migrate(app,db) #flask-migration - Migration lets developer to make changes in db columns without deleting data
                            # or otherwise delete db and then recreate again, not suitable for production
#DB model
class Users(db.Model,UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    note = db.relationship('Notes',uselist=False, back_populates='user')


#database model(data class)
class Notes(db.Model):
    __tablename__= "notes"
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),name="fk_notes_user_id")
    user = db.relationship('Users', back_populates='note')
    
   
    
    def __repr__(self):
        return f"{self.id}"    
    
    

@app.route("/", methods=["POST","GET"])
@login_required
def notes():
    if request.method=="POST":
        new_topic = request.form['topic'] #Flask has captured it 
        new_note =request.form['note']
        
        One_note=Notes(topic=new_topic, note=new_note, user=current_user)
        try:
            db.session.add(One_note)
            db.session.commit()
            return redirect("/")
            
        except Exception as e:
            return f"Error {e}"
    else:
        All_Notes=Notes.query.all()
        return render_template('notes.html', All_Notes=All_Notes)
        
   #return render_template('notes.html')


@app.route("/delete/<id>")
def delete(id):
    delete_id=Notes.query.get_or_404(id)
    try:
        db.session.delete(delete_id)
        db.session.commit()
        return redirect("/")
    
    except Exception as e:
        return f"Error{e}"



@app.route("/edit/<int:id>", methods=["POST","GET"])
def edit(id):
    edit_id=Notes.query.get_or_404(id)
    if request.method=="POST":
        edit_id.topic=request.form['topic']
        edit_id.note=request.form['note']
        try:
            db.session.commit()
            return redirect("/")
        
        except Exception:
            return f"Error {Exception}"
    else:
         return render_template('edit2.html', note_id=edit_id, topic=edit_id.topic,note=edit_id.note)    




# Load user for Flask-Login
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


# Register route
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"] 
        password = request.form["password"]

        if Users.query.filter_by(username=username).first():
            return render_template("sign_up.html", error="Username already taken!")

        else:
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    
    return render_template("sign_up.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = Users.query.filter_by(username=username).first()

        if user and user.password==password:
            login_user(user)
            return redirect(url_for("profile"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")



# Home route
#@app.route("/loginuser")
#def home():
#    return render_template("home.html")

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("notes"))

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)