template = {
    # "openapi": "3.1.0",
    "swagger": "2.0",
    "uiversion": 2,
    "info": {
        "title": "stage_one",
        "description": "stage_one API Documentations",
        "contact": {
            "email": "fasogbaemmanuel@gmail.com",
            "name": "Emmanuel O. Fasogba",
            "url": "www.twitter.com/tz_emiwest",
        },
        "termsOfService": "www.twitter.com/tz_emiwest",
        "version": "1.0.0"
    },
    # base route for blueprint registration
    "basePath": "/api",  # if swagger 2.0
    # "path": "/api",  # if openapi 3.1.0
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer\
                tokens.\n\nExample: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}
