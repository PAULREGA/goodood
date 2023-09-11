from flask import Blueprint
from stage_one.controllers.v1.base import index, stage_one

app_blueprints = Blueprint("home", __name__)

app_blueprints.get("/status")(index)
app_blueprints.get("/api")(stage_one)
