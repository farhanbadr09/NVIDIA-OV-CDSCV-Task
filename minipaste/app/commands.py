from typing import DefaultDict
import click
from flask import Blueprint, cli
from .api import database, models
from . import config

database_bp = Blueprint("database", __name__)


@database_bp.cli.command("init")
@click.argument("stage")
def create_db(stage):
    """Create intial db for a given STAGE [dev|prod]"""
    cfg = config.DevConfig
    if stage == "prod":
        cfg = config.ProdConfig
    session = database.create_session(cfg.DATABASE_URI)
    models.Base.metadata.create_all(session.get_bind())
    print(f"created {stage} db")
