from flask import testing, wrappers
from minipaste.app.api import database, models
import sqlite3


def test_create_app(test_client: testing.FlaskClient):
    """Test app creation"""
    out: wrappers.Response = test_client.get("/api/")
    assert out.data.decode("utf-8").replace('"', "") == "pong!\n"


def test_paste(test_client: testing.FlaskClient, mocked_session):
    """Test simple paste route stores sent data and returns id"""
    test_data = "test_paste test data"
    out: wrappers.Response = test_client.post("/api/paste", data=test_data)

    # verify for paste id
    paste_resp = out.get_json()
    assert paste_resp["id"] == 1

    # verify data storage
    results = [r for r in mocked_session.query(models.Paste).all()]
    assert len(results) == 1

    stored_paste: models.Paste = results[0]
    assert stored_paste._id == 1
    assert stored_paste.content == test_data


def test_get_paste(test_client: testing.FlaskClient, mocked_session):
    """Test getting paste that already exists"""
    # setup test data
    test_msg = "Get Paste Test"
    session = database.create_session("sqlite://")
    paste = models.Paste(test_msg)
    session.add(paste)

    # call route
    out: wrappers.Response = test_client.get("/api/paste/1")

    # check response
    recv_paste = out.json
    assert recv_paste["_id"] == 1
    assert recv_paste["content"] == test_msg
