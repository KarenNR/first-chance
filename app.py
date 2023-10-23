import os
from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'f1rstch4nc3'

@app.route('/')
def loadIndex():
    return render_template('student/index.html')

@app.route('/trabajos')
def loadJobs():
    # Get Job Offers
    jobOffers = ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
                 (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León", "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
                 (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"))
    return render_template('/student/trabajos.html', jobOffers=jobOffers)

@app.route('/solicitudes')
def loadRequests():
    return render_template('/student/solicitudes.html')

@app.route('/chat')
def loadChat():
    return render_template('/student/chat.html')

@app.route('/perfil')
def loadProfile():
    # Get posts
    posts = (('Post 1', 'Prueba'), ('Post 2', 'Prueba'))
    # Get education items
    education = (('UDEM', 'ITC', '2023'), ('Regio Cumbres', 'Preparatoria', '2020'))
    # Get projects
    projects = (('Proyecto 1', 'Prueba'), ('Proyecto 2', 'Prueba'))
    return render_template('/student/perfil.html', posts=posts, education=education, projects=projects)

@app.route('/perfil/informacion')
def loadProfileInformation():
    return render_template('/student/informacion.html')

@app.route('/chancebot')
def loadChancebot():
    return render_template('/student/chancebot.html')

@app.route('/perfil/cv')
def loadProfileCV():
    return render_template('/student/cv.html')

@app.route('/perfil/configuracion')
def loadProfileConfiguration():
    return render_template('/student/configuracion.html')

@app.route('/editar-cv')
def loadCVForm():
    return render_template('student/editar-cv.html')

@app.route('/design-cv', methods=['POST'])
def designCV():
    name = request.form["name"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    phone = request.form["phone"]
    website = request.form["website"]
    profile = request.form["profile"]
    institutionList = request.form.getlist("institution")
    gradeList = request.form.getlist("grade")
    yearList = request.form.getlist("year")
    skillsList = request.form.getlist("skill")
    extraTitles = request.form.getlist("extra-section-title")
    extraDescriptions = request.form.getlist("extra-section-description")

    print(name, lastname, email, phone, website)
    print(profile)
    for i, g, y in zip(institutionList, gradeList, yearList):
        print(i, g, y)
    for i in skillsList:
        print(i)
    for t, d in zip(extraTitles, extraDescriptions):
        print(t, d)

    flash("Currículum creado exitosamente")
    return redirect('/editar-cv')