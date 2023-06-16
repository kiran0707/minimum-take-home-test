from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
import calculate_emission as c

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# secret key to utilize session in Flask
app.secret_key = 'secretkey'


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        # save emission file 
        ef = request.files.get('emission_file')	
        emission_file = secure_filename(ef.filename)
        ef.save(os.path.join(app.config['UPLOAD_FOLDER'], emission_file))
        session['uploaded_emission_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], emission_file)
        # save activity file
        act_f = request.files.get('activity_file')	
        activity_file = secure_filename(act_f.filename)
        act_f.save(os.path.join(app.config['UPLOAD_FOLDER'], activity_file))
        session['uploaded_activity_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], activity_file)
        return render_template('upload2.html')
    return render_template("upload.html")


@app.route('/show_merged',methods=['POST','GET'])
def showMerged():
    emission_file = session.get('uploaded_emission_file_path', None)
    activity_file = session.get('uploaded_activity_file_path', None)
    lookup = request.form['lookup']
    # read csv
    final_df = c.calculate_df(emission_file, activity_file, lookup)
    # Converting to html Table
    result_data = final_df.to_html()
    return render_template('show_csv_data.html', data_var=result_data)

@app.route('/show_group_by',methods=['POST','GET'])
def showGroup():
    emission_file = session.get('uploaded_emission_file_path', None)
    activity_file = session.get('uploaded_activity_file_path', None)
    lookup = request.form['lookup']
    group = request.form['group']
    # read csv
    final_df = c.calculate_group(emission_file, activity_file, lookup, group)
    # Converting to html Table
    result_data = final_df.to_html()
    return render_template('show_csv_data.html', data_var=result_data)

@app.route('/show_sorted_by',methods=['POST','GET'])
def showSort():
    emission_file = session.get('uploaded_emission_file_path', None)
    activity_file = session.get('uploaded_activity_file_path', None)
    lookup = request.form['lookup']
    sort = request.form['sort']
    # read csv
    final_df = c.calculate_sort(emission_file, activity_file, lookup, sort)
    # Converting to html Table
    result_data = final_df.to_html()
    return render_template('show_csv_data.html', data_var=result_data)

@app.route('/show_filter_by',methods=['POST','GET'])
def showFilter():
    emission_file = session.get('uploaded_emission_file_path', None)
    activity_file = session.get('uploaded_activity_file_path', None)
    lookup = request.form['lookup']
    filter = request.form['filter']
    fvalue = request.form['fvalue']
    # read csv
    final_df = c.calculate_filter(emission_file, activity_file, lookup, filter, fvalue)
    # Converting to html Table
    result_data = final_df.to_html()
    return render_template('show_csv_data.html', data_var=result_data)

if __name__ == '__main__':
    app.run(debug=True)
