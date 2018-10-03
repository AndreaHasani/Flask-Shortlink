from flask import Flask, render_template, request, session, jsonify, redirect
from models import *
from app import application
from functions import *


@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@application.route("/shortner", methods=["POST"])
def shortner():
    url = request.form.get("url", "", str)
    exist = db.session.query(Shortlink).filter_by(fullUrl=url).first()
    if exist:
        result = "<p>Shortlink created: {}r/{}</p>".format(
            request.url_root, exist.id)
        return jsonify(result=result, code=1)
    _id = shortlink(db, Shortlink, url)
    result = "<p>Shortlink created: {}r/{}</p>".format(
        request.url_root, _id)
    return jsonify(result=result, code=1)


@application.route("/r/<_id>")
def redir(_id):
    result = db.session.query(Shortlink).filter_by(id=_id).first()
    return redirect(result.fullUrl, code=302)
