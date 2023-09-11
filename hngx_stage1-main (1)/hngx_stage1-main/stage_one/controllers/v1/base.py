from flask import jsonify, request
from flasgger import swag_from
from datetime import datetime
from stage_one.utils.utils import Responses


@swag_from('../../docs/status.yml')
def index():
    resp = {
        'data': True,
        'message': "Running..",
        'status_code': 200
    }
    return jsonify(**resp)


@swag_from('../../docs/stage_one.yml')
def stage_one():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    weekday = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'
    ]
    today = datetime.utcnow()
    current_day = weekday[today.weekday()]
    current_utc_time = today.strftime("%Y-%m-%dT%H:%M:%SZ")
    resp = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": "https://github.com/fashemma007/hngx_stage1/blob/main/run.py",
        "github_repo_url": "https://github.com/fashemma007/hngx_stage1",
        "status_code": 200,
    }
    return jsonify(resp)