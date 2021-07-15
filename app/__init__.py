from flask import Flask
import os
from flask import Flask, flash, request, \
redirect, url_for, render_template, send_from_directory

from app.dogscatspredictor import DogsCatsPredictor
from PIL import Image 


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #Configuration --------------------------

    app.config.from_mapping(
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'},
        MODEL_PATH = os.path.join(app.root_path, '..', 'models', 'dogscats.pt'),
    )

    dogsCatsPredictor = DogsCatsPredictor(app.config['MODEL_PATH'])

    #Routes --------------------------------------

    @app.route("/", methods=['GET', 'POST'])
    def dogOrCat():
        if request.method == 'POST':
            # Check if the post request has the file part.
            # Return status code 400, bad request.
            if 'file' not in request.files:
                return({'error':'No file part supplied!'}, 400)
            file = request.files['file']

            # If the user does not select a file, the browser submits an
            # empty file without a filename. Return status code 400, bad request.
            if file.filename == '':
                return({'error':'No file selected'}, 400)

            if file and allowed_file(file.filename):
                image = Image.open(file).convert('RGB')
                prediction = dogsCatsPredictor.predictCatOrDog(image)
                print(prediction)
                return({'class':prediction}, 200)
                
        #If the method is GET, which is what your browser does when visiting a website
        return render_template('dogscats.html')

    #Functions -------------------------------------

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    '''Check if extension is allowed'''
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

    return app

