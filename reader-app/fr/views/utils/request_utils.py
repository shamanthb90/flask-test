from flask import current_app as app


def get_app_config_value(key):
    return app.config[key] if key in app.config else None


def get_app_name():
    return get_app_config_value('NAME')


def get_reader_factory():
    return get_app_config_value('READER_FACTORY')
