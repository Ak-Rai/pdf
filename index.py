from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import uuid
import shutil
from src import convert_text

app = Flask(__name__)
app.debug = True
CORS(app)
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def handle_upload(file):
    try:
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'])
        folderPath = os.path.join(upload_path, str(uuid.uuid4()))
        os.mkdir(folderPath)
        file.save(os.path.join(folderPath, filename))
        return folderPath
    except:
        print('Something went wrong while Uploading File.')


def get_text(folderPath, filename):
    path = os.path.join(folderPath, filename)
    text = convert_text.readPdf(path)
    if len(text) < 10:
        print('Unsupported File Type.')
    return text


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    try:
        files = request.files.getlist('file[]')
        for file in files:
            print(file)
        if (len(files) == 0):
            e = "No file selected for uploading."
            return jsonify({'htmlresponse': render_template('error.html', error=e)})

        result_list = []
        for file in files:
            print(file.filename)
            if file.filename.endswith(('png', 'jpg', 'jpeg', 'pdf')):
                if file.filename == '':
                    resp = jsonify({'message': 'No file selected for uploading.'})
                    resp.status_code >= 400
                    return resp
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    folderPath = handle_upload(file)
                    text = get_text(folderPath, filename)
                    result_list.append(text)
                    shutil.rmtree(folderPath)
            else:
                e = "Check file extension. File extension should be only '.jpg', '.jpeg', '.png', '.pdf'."
                return jsonify({'htmlresponse': render_template('error.html', error=e)})
        return jsonify({'htmlresponse': render_template('result.html', result_list=result_list)})
    except Exception as e:
        return jsonify({'htmlresponse': render_template('error.html', error=e)})


if __name__ == "__main__":
    print("IN MAIN")
    app.run(port=5000, debug=True)
