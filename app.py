import os
from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_mysqldb import MySQL
import variables

app = Flask(__name__)
app.secret_key = 'f1rstch4nc3'


@app.route('/iniciar-sesion')
def loadLogin():
    return render_template('login.html')


@app.route('/')
def loadIndex():
    return render_template('student/index.html')


@app.route('/trabajos')
def loadJobs():
    jobOffers = variables.jobOffers
    return render_template('/student/trabajos.html', jobOffers=jobOffers)


@app.route('/get-job-description/<int:id>')
def getJobDescription(id):
    data = variables.jobDescription
    for item in data:
        if item[0] == id:
            return jsonify({"message": item})


@app.route('/trabajos/aplicaciones')
def loadApplications():
    applications = variables.applications
    return render_template('/student/aplicaciones.html', applications=applications)


@app.route('/get-application-info/<int:id>')
def getApplicationInfo(id):
    data = variables.applicationInfo
    for item in data:
        if item[0] == id:
            return jsonify({"message": item})


@app.route('/trabajos/guardados')
def loadSaved():
    saved = variables.saved
    return render_template('/student/guardados.html', saved=saved)


@app.route('/trabajos/alertas-empleo')
def loadAlerts():
    alerts = variables.alerts
    return render_template('/student/alertas.html', alerts=alerts)


@app.route('/trabajos/busquedas-recientes')
def loadRecentSearches():
    return render_template('/student/busquedas-recientes.html')


@app.route('/solicitudes')
def loadRequests():
    return render_template('/student/solicitudes.html')


@app.route('/chat')
def loadChat():
    return render_template('/student/chat.html')


@app.route('/detalle/<int:id>')
def loadDetail(id):
    data = variables.jobDescription
    for item in data:
        if item[0] == id:
            return render_template('/student/detalle.html', job=item)


@app.route('/perfil')
def loadProfile():
    posts = variables.posts
    education = variables.education
    projects = variables.projects
    return render_template('/student/perfil.html', posts=posts, education=education, projects=projects)


@app.route('/chancebot')
def loadChancebot():
    return render_template('/student/chancebot.html')


@app.route('/perfil/cv')
def loadProfileCV():
    cv = variables.cv
    return render_template('/student/cv.html', cv=cv, zip=zip)


@app.route('/perfil/configuracion')
def loadProfileConfiguration():
    email = variables.email
    username = variables.username
    return render_template('/student/configuracion.html', email=email, username=username)


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
