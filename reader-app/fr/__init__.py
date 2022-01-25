import os

import flask

from fr.reader.factory import ReaderFactory
from fr.views.demo import bp as demo_bp

# root project_dir
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get reader factory instance
reader_factory = ReaderFactory(project_dir=project_dir)


def create_app(flask_config: str = 'development'):
    # initialize flask app
    flask_app = flask.Flask(__name__, instance_relative_config=False)
    # initialize flask config
    flask_config = flask_config.capitalize()
    flask_app.logger.info(f'Initializing Flask app for {flask_config} environment...')
    flask_app.config.from_object(f'config.{flask_config}')

    with flask_app.app_context():
        # Add model factory to flask_app config
        flask_app.config['READER_FACTORY'] = reader_factory

        # Initialize static folder
        flask_app.static_url_path = flask_app.config.get('STATIC_FOLDER')
        flask_app.static_folder = os.path.join(flask_app.root_path, flask_app.static_url_path)

        # Register blueprints
        from .views import demo
        flask_app.register_blueprint(demo.bp)

        # return app based on app_type
        flask_app.logger.info(f'Initialized Flask app for {flask_config} environment...')
        return flask_app
