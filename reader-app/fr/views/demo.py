import os

from flask import Blueprint
from flask import current_app as app
from flask import render_template, make_response
from flask import request
from flask import send_from_directory

from fr.reader.service import get_file_contents
from fr.views.utils import request_utils
from fr.views.utils import response_utils

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@bp.route('/', methods=['GET'])
def home():
    return response_utils.get_response(
        code=200,
        message='success',
        data=dict(app_name=request_utils.get_app_name(), environ=dict(os.environ)),
    )


@bp.route('/api/v1/show_file', methods=['GET'])
def show_file():
    filename, start, end = get_request_args()
    contents = get_file_contents(factory=request_utils.get_reader_factory(),
                                 filename=filename,
                                 start_line=start,
                                 end_line=end)
    resp = make_response(contents)
    return resp
    # return render_template('index.html', contents=contents)


def get_request_args():
    filename = request.args.get('file', default='file1.txt', type=str)
    start_ln = request.args.get('start_ln', default=-1, type=int)
    end_ln = request.args.get('end_ln', default=-1, type=int)
    return filename, start_ln, end_ln
