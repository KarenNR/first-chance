from flask import Flask, render_template, redirect, request, flash, jsonify, url_for
import variables
import variablesEnterprise
from flask_socketio import SocketIO, emit
from datetime import datetime
import openai

app = Flask(__name__)
socketio_rec = SocketIO(app, cors_allowed_origins="*")
app.secret_key = 'f1rstch4nc3'
openai.api_key = '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'

# Context for ChatGPT
messages = [ {"role": "system", "content": "You are a helpful assistant."} ]

@socketio_rec.on("chat")
def chat(message):
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})
    emit("chat_response", reply)


@app.route('/iniciar-sesion')
def loadLogin():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user[0] == username and user[1] == password:
            role = user[2]
            if role == 'student':
                return redirect(url_for('loadIndex'))
            elif role == 'company':
                return redirect(url_for('loadIndexEnterprise'))

    message = "Usuario o contraseña incorrecta"
    return render_template('login.html', message=message)

@app.route('/')
def loadIndex():
    jobOffers = variables.jobOffers
    feed=variables.feed
    return render_template('/student/index.html', jobOffers=jobOffers, feed=feed)


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



    
users = variables.users
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
    interests = variables.interests
    return render_template('/student/alertas.html', alerts=alerts, interests=interests)


@app.route('/trabajos/busquedas-recientes')
def loadRecentSearches():
    recentSearches = variables.recentSearches
    return render_template('/student/busquedas-recientes.html', recentSearches=recentSearches)


@app.route('/solicitudes')
def loadRequests():
    friendRequest=variables.friendRequest
    return render_template('/student/solicitudes.html', friendRequest=friendRequest)


@app.route('/chat')
def loadChat():
    enterpriseMessages = ("Buenas tardes, gracias por contactarnos, ¿ya has enviado tu CV?", "Perfecto, entonces está en revisión, quedamos al pendiente.")
    jobOffers = variables.jobOffers
    return render_template('/student/chat.html', enterpriseMessages=enterpriseMessages, jobOffers=jobOffers)



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
    messages = (
        (0, "Hola, ¿en qué puedo ayudarte el día de hoy?", datetime.now().strftime('%H:%M')),
    )
    return render_template('/student/chancebot.html', messages=messages)


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
    image = request.form["cv-image"]
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

    print(image)
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


@app.route('/enterprise/')
def loadIndexEnterprise():
    students = variablesEnterprise.students
    feed=variables.feed
    return render_template('/enterprise/index.html', students=students, feed=feed)


@app.route('/enterprise/trabajos')
def loadJobsEnterprise():
    students = variablesEnterprise.students
    return render_template('/enterprise/trabajos.html', students=students)


@app.route('/get-student-description/<int:id>')
def getStudentDescription(id):
    data = variablesEnterprise.studentDescription
    for item in data:
        if item[0] == id:
            return jsonify({"message": item})

 
@app.route('/enterprise/estudiante-cv/<int:id>')
def loadStudentCV(id):
    cv = variablesEnterprise.studentCV[id]
    return render_template('/enterprise/cv-estudiante.html', cv=cv, zip=zip)


@app.route('/enterprise/trabajos/guardados')
def loadSavedEnterprise():
    saved = variablesEnterprise.saved
    return render_template('/enterprise/guardados.html', saved=saved)


@app.route('/enterprise/trabajos/busquedas-recientes')
def loadRecentSearchesEnterprise():
    recentSearches = variablesEnterprise.recentSearches
    return render_template('/enterprise/busquedas-recientes.html', recentSearches=recentSearches)


@app.route('/enterprise/chat')
def loadChatEnterprise():
    studentMessages = ("Tengo oportunidad a las 13:00, ¿está bien?", "Perfecto, en unas horas nos vemos, ¡gracias por la oportunidad!")

    return render_template('/enterprise/chat.html', studentMessages=studentMessages)


@app.route('/enterprise/perfil')
def loadProfileEnterprise():
    posts = variablesEnterprise.posts
    ratings = variablesEnterprise.ratings
    rating1 = 10
    rating2 = 15
    rating3 = 15
    rating4 = 210
    rating5 = 150
    totalRatings = rating1 + rating2 + rating3 + rating4 + rating5
    average = ((1*rating1) + (2*rating2) + (3*rating3) +
               (4*rating4) + (5*rating5)) / totalRatings
    return render_template('/enterprise/perfil.html', posts=posts, totalRatings=totalRatings, average=average, ratings=ratings, 
                           rating1=rating1, rating2=rating2, rating3=rating3, rating4=rating4, rating5=rating5)


@app.route('/enterprise/perfil/vacantes')
def loadVacanciesEnterprise():
    vacancies = variablesEnterprise.vacancies
    return render_template('/enterprise/vacantes.html', vacancies=vacancies)


@app.route('/enterprise/perfil/crear-vacante')
def loadCreateVacancy():
    return render_template('/enterprise/crear-vacante.html')


@app.route('/create-vacancy', methods=['POST'])
def createVacancy():
    title = request.form["title"]
    location = request.form["location"]
    mode = request.form["mode"]
    time = request.form["time"]
    minRem = request.form["min-remuneration"]
    maxRem = request.form["max-remuneration"]
    description = request.form["description"]
    resName = request.form.getlist("responsibility-name")
    resDesc = request.form.getlist("responsibility-description")

    print(title)
    print(location, mode, time)
    print("${:,.2f} - ${:,.2f}".format(int(minRem), int(maxRem)))
    print(description)
    for n, d in zip(resName, resDesc):
        print(n,d)

    flash("Vacante creada exitosamente")
    return redirect('/enterprise/perfil/crear-vacante')


@app.route('/get-vacancy-information/<int:id>')
def getVacancyInformation(id):
    data = variablesEnterprise.vacanciesInfo
    for item in data:
        if item[0] == id:
            return jsonify({"message": item})


@app.route('/get-vacancy-applicants/<int:id>')
def getVacancyApplicants(id):
    data = variablesEnterprise.vacanciesApplicants
    applicants = []
    for item in data:
        if item[4] == id:
            applicants.append(item)
    return jsonify({"message": applicants})


@app.route('/enterprise/perfil/configuracion')
def loadProfileConfigurationEnterprise():
    email = variablesEnterprise.email
    username = variablesEnterprise.username
    return render_template('/enterprise/configuracion.html', email=email, username=username)


@app.route('/enterprise/detalle-estudiante/<int:id>')
def loadStudentDetail(id):
    studentDescription = variablesEnterprise.studentDescription[id]
    posts = [post for post in variablesEnterprise.studentPosts if post[0] == id]
    education = [education for education in variablesEnterprise.studentEducation if education[0] == id]
    projects = [project for project in variablesEnterprise.studentProjects if project[0] == id]
    return render_template('/enterprise/detalle-estudiante.html', studentDescription=studentDescription, posts=posts, education=education, projects=projects)

@app.route('/descripcion-empresa/<int:id>')
def loadEnterpriseProfile(id):
    enterpriseDescription= variables.enterpriseDescription[id-1]
    posts = variables.enterprisePosts[id-1]
    ratings = variables.enterpriseRatings[id-1]
    saved = variables.vacancies[id-1]
    rating1 = 10
    rating2 = 15
    rating3 = 15
    rating4 = 210
    rating5 = 150
    totalRatings = rating1 + rating2 + rating3 + rating4 + rating5
    average = ((1*rating1) + (2*rating2) + (3*rating3) +
               (4*rating4) + (5*rating5)) / totalRatings
    return render_template('/student/descripcion-empresa.html',saved=saved,enterpriseDescription=enterpriseDescription, posts=posts, totalRatings=totalRatings, average=average, ratings=ratings, 
                           rating1=rating1, rating2=rating2, rating3=rating3, rating4=rating4, rating5=rating5)



