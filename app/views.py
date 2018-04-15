"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify
from forms import UploadForm
import os, json



###
# Routing for your application.
###


@app.route('/')
def index():
    """Render website's initial page and let VueJS take over."""
    return render_template('index.html')
    

@app.route('/api/upload', methods=['POST'])
def upload():
    error_list=[]
    form = UploadForm()
    if form.validate_on_submit():
        photograph = form.photo.data
        desc = form.description.data
        file = request.files['file']
        photograph.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        json_list = {}
        json_list['message'] = "File Upload Successful"
        json_list['filename'] = file.filename
        json_list['description'] = desc
        return json.dumps(json_list)
    else:
        for i in form_errors(form):
            error_list.append(i)
        json_error_list = {}
        json_error_list['errors'] = error_list
        return json.dumps(json_error_list)
        #json_list = {"message":"File Upload Successful" + '\n' + "filename": file.filename + '\n' + "description": desc}


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
