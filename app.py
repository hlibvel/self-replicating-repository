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


def get_login():
	"""Reads GitHub user name"""
    resp = github.get("/user")
    assert resp.ok
    return resp.json()["login"]


def make_a_fork(owner, repo_name):
	"""Forks requested repository"""
    resp = github.post(f'/repos/{owner}/{repo_name}/forks')
    assert resp.ok

    return resp.json()


@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    make_a_fork(OWNER, REPO_NAME)
    return """
        Dear @{login},
        now you have a fork of {owner}/{repo_name} on GitHub""".format(
            login=get_login(),
            owner=OWNER,
            repo_name=REPO_NAME
            )

if __name__ == "__main__":
    app.run()
