
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


from app.database import User



@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
    }
    out["users"] = User.query.all()
    return out



@app.route("/users", methods=["POST"])
def create_user():
    out = {
         "ok": True,
        "message": "Success"
    }
    user_data = request.json

    db.session.add (
        User(
            first_name =user_data.get("first_name"),
            last_name =user_data.get("last_name"),
            hobbies = user_data.get("hobbies")
    
        )
    )
    db.session.commit()
    return out, 201
    



@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
        "ok": True,
        "message":"Success"
    }
    user = User.query.filter_by(id=uid).first()
    user.active = 0
    db.session.commit()
    return out, 200

    
    


@app.route("/users/<int:uid>", methods=["GET"])
def get_single_user(uid):
    out ={
        "ok": True,
        "message": "Success"
    }
    out["user"] = User.query.filter_by(id=uid).first()
    
    return out

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your user agent is %s</p>" % user_agent
