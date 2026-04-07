from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#database model(data class)
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    note=db.Column(db.String(100),nullable=False)
    
    
    def __repr__(self):
        return f"{self.id}"    
    

@app.route("/", methods=["POST","GET"])
def notes():
    if request.method=="POST":
        new_topic = request.form['topic'] #Flask has captured it 
        new_note =request.form['note']
        
        One_note=Notes(topic=new_topic, note=new_note)
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






if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)