import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow_model.predict import predict_image as model_predict 
import json


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'upload_files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect('/error')
        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect('/error')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            image_pred, confidence = model_predict(file)
            messages = {
                'file': 'uploads/' + filename,
                'image_pred': str(image_pred),
                'confidence': str(confidence)
            }
            
            messages = json.dumps(messages)
            return redirect(url_for('file_predict', messages=messages))
        else:
            return redirect('/error')

    return render_template('index.html')


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/predict')
def file_predict():
    messages = request.args['messages']
    messages = json.loads(messages)


    return render_template('predict.html', predicted_value=messages['image_pred'], 
        predicted_confidence=messages['confidence'],
        image=messages['file'])



@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=5002, debug=True)