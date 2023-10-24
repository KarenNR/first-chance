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
                 (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
                  "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
                 (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"))
    return render_template('/student/trabajos.html', jobOffers=jobOffers)


@app.route('/get-job-description/<int:id>')
def getJobDescription(id):
    data = (
        (
            1,
            "Practicante Diseño UI/UX",
            "/static/images/armazen.png",
            "Armazen",
            4.7,
            "Apocada, Nuevo León",
            "Remoto",
            "Medio tiempo",
            "$6,000 - $9,000",
            False,
            '''Como Practicante de Diseño UI/UX, serás parte de nuestro equipo de diseño y desempeñarás un papel fundamental en 
            la creación de experiencias de usuario atractivas y funcionales. Contribuirás al diseño de interfaces de usuario 
            intuitivas y atractivas, mejorando la usabilidad de nuestras aplicaciones y sitios web.
            ''',
            [["Diseño de Interfaces de Usuario", "Colabora en la creación de diseños de interfaces de usuario atractivas y funcionales para aplicaciones web y móviles, asegurando una experiencia de usuario intuitiva."],
             ["Pruebas y Evaluación", "Participa en pruebas de usabilidad y evaluación de la experiencia del usuario para identificar áreas de mejora en el diseño y la navegación."],
             ["Prototipado Interactivo", "Ayuda en la creación de prototipos interactivos que representen las funcionalidades y la navegación de las aplicaciones."],
             ["Colaboración en Equipos", "Trabaja en estrecha colaboración con diseñadores, desarrolladores y otros miembros del equipo."],
             ["Investigación de Usuario", "Contribuye a la investigación de usuario mediante la recopilación y el análisis de comentarios de los usuarios."]]
        ),
        (
            2,
            "Practicante Desarrollo de Software",
            "/static/images/neorem.png",
            "Neorem",
            4.5,
            "Monterrey, Nuevo León",
            "Remoto",
            "Tiempo completo - Horarios flexibles",
            "$6,000 - $9,000",
            True,
            '''Como Practicante Desarrollador de Software, te unirás a nuestro equipo de desarrollo y tendrás la oportunidad de 
            adquirir experiencia práctica en el emocionante mundo del desarrollo de software. Tu papel será fundamental para 
            contribuir al desarrollo, prueba y mantenimiento de nuestras aplicaciones y sistemas de software.
            ''',
            [["Desarrollo de Código", "Participa en la escritura, modificación y depuración de código para nuevas características o mejoras en las aplicaciones y sistemas existentes."],
             ["Pruebas y Depuración", "Colabora en pruebas unitarias y de integración para garantizar que el código funcione de manera eficiente y cumpla con los requisitos."],
             ["Mantenimiento de Código", "Ayuda en la identificación y resolución de problemas de código, así como en la aplicación de actualizaciones y correcciones."],
             ["Investigación y Aprendizaje", "Realiza investigaciones independientes para estar al tanto de las mejores prácticas y las tendencias actuales en el desarrollo de software."],
             ["Colaboración en Equipos", "Trabaja en estrecha colaboración con otros miembros del equipo de desarrollo, participando en reuniones y colaborando en proyectos conjuntos."]]
        ),
        (
            3,
            "Practicante de Ciberseguridad",
            "/static/images/cisce.png",
            "Cisce",
            4,
            "Escobedo, Nuevo León",
            "Presencial",
            "Medio tiempo",
            "$6,000 - $9,000",
            True,
            '''Como Practicante de Ciberseguridad, formarás parte de nuestro equipo encargado de proteger la infraestructura y los 
            datos críticos de la organización. Esta pasantía te brindará la oportunidad de adquirir experiencia práctica en el 
            emocionante campo de la ciberseguridad y contribuir a la defensa de la información de la empresa.
            ''',
            [["Monitoreo de seguridad", "Colabora en el monitoreo constante de la seguridad de la red y los sistemas para identificar posibles amenazas o intrusiones."],
             ["Análisis de Vulnerabilidades", "Ayuda en la identificación y evaluación de vulnerabilidades en sistemas y aplicaciones, y participa en la implementación de soluciones de seguridad."],
             ["Gestión de Incidentes", "Participa en la respuesta a incidentes de seguridad, incluida la documentación y la comunicación de eventos de seguridad."],
             ["Pruebas de Penetración", "Contribuye en la realización de pruebas de penetración en la infraestructura y las aplicaciones para identificar debilidades y puntos de entrada potenciales para atacantes."],
             ["Concientización en Ciberseguridad", "Colabora en programas de concientización y capacitación en ciberseguridad para los empleados."]]
        )
    )
    for item in data:
        if item[0] == id:
            return jsonify({"message": item})


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
    education = (('UDEM', 'ITC', '2023'),
                 ('Regio Cumbres', 'Preparatoria', '2020'))
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
