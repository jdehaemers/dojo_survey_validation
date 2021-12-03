from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.dojo import Dojo

fields = []

@app.route('/')
def survey():
    languages = ['Python', 'JavaScript', 'HTML', 'C++', 'C#']
    return render_template('survey.html', languages = languages)

@app.route('/process', methods=['POST'])
def process():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    global fields
    fields = []
    data = {
        'name' : request.form['name'], 
        'location' : request.form['location'],
        'language': request.form['language'],
        'comment' : request.form['comment'] 
        }
    for i in request.form:
        fields.append(i)
        session[i] = request.form[i]
    print(session)
    Dojo.create(data)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', fields=fields)
