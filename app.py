#!/usr/bin/env python3
from flask import Flask, redirect, url_for
from werkzeug.contrib.fixers import ProxyFix
from flask_dance.contrib.github import make_github_blueprint, github

from config import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = 'supersekrit'
blueprint = make_github_blueprint(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scope='public_repo',  # minimal access scope that allows repository fork
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")  # read GitHub user name
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

if __name__ == "__main__":
    app.run()
