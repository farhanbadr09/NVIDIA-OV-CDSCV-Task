from flask import json, jsonify, wrappers, current_app, request
from sqlalchemy.sql.functions import mode
from ..api import api
from . import database, models


@api.route("/")
def default_route() -> wrappers.Response:
    return jsonify("pong!")


@api.route("/post")
def test_post() -> wrappers.Response:
    session = database.create_session(current_app.config.get("DATABASE_URI"))
    customer = models.Customers("john", "1234 Street", "john@doe.com")
    session.add(customer)
    session.commit()
    resp = {"success": True}
    return jsonify(resp)


@api.route("/paste", methods=["POST"])
def paste() -> wrappers.Response:
    """Stores posted content into paste and returns a paste-id"""
    session = database.create_session(current_app.config.get("DATABASE_URI"))
    paste = models.Paste(request.data.decode("utf-8"))
    session.add(paste)
    session.commit()
    resp = {"id": paste._id}
    return jsonify(resp)


@api.route("/paste/<_id>")
def get_paste(_id) -> wrappers.Response:
    """Returns a stored paste"""
    session = database.create_session(current_app.config.get("DATABASE_URI"))
    paste: models.Paste
    paste = session.query(models.Paste).filter(models.Paste._id == _id)
    return jsonify(paste[0].json())
