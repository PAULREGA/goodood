#!venv/bin/python3
"""
Copyright (c) 2023 - present imitor.tech
"""
import os
from dotenv import load_dotenv, find_dotenv
from stage_one import app

load_dotenv(find_dotenv())


if __name__ == "__main__":
    # print(app.url_map)  # uncomment to show all available endpoints/routes
    # print(app.config.get('MAIL_PORT'))
    app.run(
        host='0.0.0.0',
        port=os.getenv('PORT'),
    )
