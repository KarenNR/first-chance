# Get Job Offers - loadJobs
jobOffers = ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
             (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
              "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
             (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"))

# Get job description - getJobDescription
jobDescription = (
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
         ["Colaboración en Equipos",
          "Trabaja en estrecha colaboración con diseñadores, desarrolladores y otros miembros del equipo."],
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

# Get applications - loadApplications
applications = (
    (0, "Armazen", "Practicante Diseño UI/UX", 1),
    (1, "Acme Inc.", "Ingeniero de Software", 2),
    (2, "Tech Solutions", "Desarrollador Frontend", 3),
    (3, "ABC Corporation", "Analista de Datos", 4),
    (4, "Cloud Innovators", "Arquitecto de Nube", 2),
    (5, "Startech", "Desarrollador de Aplicaciones Móviles", 1)
)

# Get application information - getApplicationInfo
applicationInfo = (
    (0, "Practicante Diseño UI/UX", "/static/images/neorem.png",
     "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo"),
    (1, "Ingeniero de Software", "/static/images/armazen.png",
     "Acme Inc.", "Monterrey, Nuevo León", "Presencial", "Medio tiempo"),
    (2, "Desarrollador Frontend", "/static/images/cisce.png",
     "Tech Solutions", "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (3, "Analista de Datos", "/static/images/armazen.png",
     "ABC Corporation", "Monterrey, Nuevo León", "Mixto", "Medio tiempo"),
    (4, "Arquitecto de Nube", "/static/images/cisce.png",
     "Cloud Innovators", "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (5, "Desarrollador de Aplicaciones Móviles", "/static/images/armazen.png",
     "Startech", "Monterrey, Nuevo León", "Remoto", "Medio tiempo")
)

# Get saved jobs - loadSaved
saved = ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
         (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
          "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
         (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"))

# Get job alerts - loadAlerts
alerts = (
    (0, "Practicante Diseño UI/UX", "Armazen",
     "Apodaca, Nuevo León", "Remoto", "Medio tiempo"),
    (1, "Ingeniero de Software", "Acme Inc.",
     "Monterrey, Nuevo León", "Presencial", "Medio tiempo"),
    (2, "Desarrollador Frontend", "Tech Solutions",
     "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (3, "Analista de Datos", "ABC Corporation",
     "Monterrey, Nuevo León", "Mixto", "Medio tiempo"),
    (4, "Arquitecto de Nube", "Cloud Innovators",
     "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (5, "Desarrollador de Aplicaciones Móviles", "Startech",
     "Monterrey, Nuevo León", "Remoto", "Medio tiempo")
)

# Get posts - loadProfile
posts = (
    ("Reconocimiento Alumno Distinguido PR2023",
     '''Orgulloso de haber recibido este reconocimiento que se le otorga al 1% de la carrera. Este tipo de premios
                 me motivan a seguir dando lo mejor de mí mismo y a aplicar todo lo que sé en buscando ser un agente de cambio.''',
     "/static/images/post1.jpg",
     "25/10/2023", 12, 5),
    ("Un pensamiento",
     "Una interfaz es como un chiste. Si tienes que explicarlo, no es bueno.",
     None,
     "24/10/2023", 25, 10)
)

# Get education items - loadProfile
education = (('UDEM', 'ITC', '2023'),
             ('Regio Cumbres', 'Preparatoria', '2020'))

# Get projects - loadProfile
projects = (
    ("Aplicación First Chance",
     "Plataforma de búsqueda de empleos para estudiantes universitarios.",
     "https://github.com/KarenNR/first-chance"),
    ("Aplicación web para registro de asistencias de profesores",
     "Proyecto realizado para la UDEM. Utilicé tecnologías como HTML, JavaScript, ASP.NET y React.",
     "https://github.com/emi7595/integrador-front"))

# Get student CV - loadProfileCV
cv = (
    "/static/images/student-profile.png",
    "Pablo", "Gutiérrez", "pablo.gtz@udem.edu", "1234567890", "pgutierrez.com",
    "Soy un estudiante de Ingeniería en Tecnologías Computacionales apasionado por la programación y la resolución de problemas.",
    ("Regio", "UDEM"),
    ("Preparatoria", "ITC"),
    (2020, 2023),
    ("Resiliencia", "Dedicación", "Esfuerzo", "Organización"),
    ("Idiomas",),
    ("Alemán A2 | Inglés C1",)
)

# Get user information - loadProfileConfiguration
email = "pablo.gtz@udem.edu"
username = "pgutierrez"
