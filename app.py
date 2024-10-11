from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime)

    def __repr__(self):
        return '<Task %r'% self.id


@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/jenny')
def show_jenny_page():
    return """
    <h1>My name is Jenny</h1> 
    <p>My name is Ray</p>"""

    

@app.route('/jenny')
def show_ray_page():
    return "My name is Ray"

if __name__ == "__main__":
    app.run(debug=True)