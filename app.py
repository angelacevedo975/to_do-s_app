from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///database/tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db= SQLAlchemy(app)
colors={
    1:"success",
    2:"warning",
    3:"danger"
}

class Task(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String)
    priority= db.Column(db.Integer)

    def __repr__(self):
        return "<Task %r" % self.id

@app.route("/")
def index():
    tasks= Task.query.all()
    return render_template("index.html", tasks=tasks, colors= colors)

@app.route("/add", methods=["POST"])
def adding():
    print(request.form["task"], request.form["priority"])
    task= Task(content= request.form["task"], priority= request.form["priority"])
    db.session.add(task)
    db.session.commit()
    return "adding"

if __name__=="__main__":
    app.run(debug=True)