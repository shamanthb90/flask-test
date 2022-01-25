import os

from fr import create_app

# read flask env from environment
flask_config = os.getenv('FLASK_CONFIG', 'development')
# create flask app
app = create_app(flask_config=flask_config)

if __name__ == '__main__':
    # Start flask app
    app.run(
        host=os.getenv('HOST', '127.0.0.1'),
        port=os.getenv('port', '8000'),
        debug=app.config['DEBUG'],
        threaded=True,
        use_reloader=False,
    )
