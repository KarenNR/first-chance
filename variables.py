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
    ),
    (
        4,
        "Ingeniero de Software",
        "/static/images/acmeinc.png",
        "Acme Inc.",
        4.2,
        "Monterrey, Nuevo León",
        "Presencial",
        "Medio tiempo",
        "$6,000 - $9,000",
        True,
        '''Trabaja en colaboración con otros miembros del equipo de desarrollo y utiliza sus habilidades técnicas para crear 
        aplicaciones y programas de software eficientes y funcionales.
            ''',
        [["Desarrollo de Software", "Crea, codifica y programa aplicaciones y sistemas de software, garantizando que cumplan con los requisitos y las especificaciones del proyecto."],
         ["Pruebas y Depuración", "Realizar pruebas exhaustivas de software para identificar errores y problemas de funcionamiento."],
         ["Diseño de Arquitectura",
             "Diseña la arquitectura de software y propón soluciones técnicas para garantizar un rendimiento óptimo."],
         ["Mantenimiento y Actualización", "Proporciona mantenimiento continuo y actualizaciones de software para asegurar que las aplicaciones estén actualizadas y funcionen sin problemas."],
         ["Colaboración en Equipos", "Trabaja en estrecha colaboración con otros miembros del equipo de desarrollo, como diseñadores de UI/UX, analistas de calidad y gerentes de proyectos, para garantizar el éxito del proyecto."]]
    ),
    (
        5,
        "Desarrollador Frontend",
        "/static/images/techsolutions.png",
        "Tech Solutions",
        4.8,
        "Monterrey, Nuevo León",
        "Remoto",
        "Medio tiempo",
        "$5,000 - $8,000",
        True,
        '''Un Desarrollador Frontend es un profesional de TI especializado en la creación y el mantenimiento de la interfaz de usuario 
            de aplicaciones web y móviles. Como practicane, tu enfoque principal será garantizar que los usuarios experimenten una 
            interfaz atractiva, interactiva y fácil de usar.
            ''',
        [["Desarrollo de UI", "Diseña y desarrolla la interfaz de usuario de aplicaciones web y móviles utilizando tecnologías como HTML, CSS y JavaScript."],
         ["Compatibilidad Multiplataforma", "Asegurarse de que la interfaz de usuario sea compatible con múltiples navegadores y dispositivos para garantizar una experiencia uniforme para los usuarios."],
         ["Optimización de Rendimiento", "Optimizar la velocidad y el rendimiento de las aplicaciones frontend para que se carguen rápidamente y respondan de manera eficiente a las interacciones del usuario."],
         ["Interacción de Usuario", "Implementa elementos interactivos, como formularios, botones y animaciones, para mejorar la usabilidad y la participación del usuario."],
         ["Colaboración en Equipos", "rabajar en estrecha colaboración con otros miembros del equipo de desarrollo para garantizar que la interfaz de usuario cumpla con los requisitos del proyecto."]]
    ),
    (
        6,
        "Analista de Datos",
        "/static/images/abccorp.png",
        "ABC Corporation",
        3.9,
        "Monterrey, Nuevo León",
        "Mixto",
        "Medio tiempo",
        "$7,000 - $10,000",
        False,
        '''Utiliza herramientas y técnicas de análisis de datos para convertir datos brutos en información valiosa.''',
        [["Recopilación de Datos", "Recolecta datos precisos y confiables de diversas fuentes, incluyendo bases de datos, encuestas, redes sociales y otros medios."],
         ["Limpieza y Preprocesamiento de Datos",
             "Limpia y prepara los datos para el análisis, eliminando valores atípicos, duplicados y datos irrelevantes."],
         ["Análisis Estadístico", "Realiza análisis estadísticos y matemáticos para identificar patrones, tendencias y relaciones en los datos."],
         ["Visualización de Datos", "Crea visualizaciones efectivas, como gráficos y tablas, para comunicar resultados y hallazgos de manera clara y comprensible."],
         ["Generación de Informes y Recomendaciones", "Prepara informes y presentaciones que resuman los resultados del análisis de datos y proporcionen recomendaciones para la toma de decisiones."]]
    ),
    (
        7,
        "Arquitecto de Nube",
        "/static/images/cloudinnovators.png",
        "Cloud Innovators",
        4,
        "Monterrey, Nuevo León",
        "Remoto",
        "Medio tiempo",
        "$6,000 - $9,000",
        False,
        '''Trabaja en estrecha colaboración con equipos de TI y desarrollo para garantizar que las soluciones en la nube sean seguras, eficientes y 
        cumplan con los objetivos empresariales.
            ''',
        [["Diseño de Arquitectura en la Nube", "Colabora con las partes interesadas para diseñar arquitecturas de nube que cumplan con los requisitos de la organización."],
         ["Implementación y Migración",
             "Supervisa la implementación de soluciones en la nube y migraciones desde entornos locales o heredados."],
         ["Seguridad en la Nube",
             "Garantiza que las soluciones en la nube sean seguras y cumplan con los estándares de seguridad."],
         ["Optimización de costos", "Administra los costos asociados con la infraestructura en la nube, identificando áreas donde se pueden realizar ahorros sin comprometer el rendimiento."],
         ["Gobernanza de la Nube", "Establece políticas y procedimientos para garantizar un uso eficiente de los recursos en la nube y para cumplir con los requisitos de cumplimiento y regulación."]]
    ),
    (
        8,
        "Desarrollador de Aplicaciones Móviles",
        "/static/images/startech.png",
        "Startech",
        4.8,
        "Monterrey, Nuevo León",
        "Remoto",
        "Medio tiempo",
        "$6,000 - $9,000",
        True,
        '''Como Practicante Desarrollador de Aplicaciones Móviles, tendrás la oportunidad de aprender y adquirir experiencia práctica en el emocionante mundo del 
        desarrollo de aplicaciones móviles. Trabajarás en colaboración con un equipo de desarrollo experimentado y contribuirás al diseño, implementación y prueba de 
        aplicaciones móviles innovadoras.
            ''',
        [["Desarrollo de Código", "Participa en la escritura de código para nuevas características o mejoras en aplicaciones móviles. Colabora en la implementación de funcionalidades utilizando lenguajes de programación como Java, Kotlin o Swift."],
         ["Pruebas y depuración", "Ayuda en la realización de pruebas unitarias y de integración para garantizar que las aplicaciones funcionen de manera eficiente."],
         ["UI/UX", "Colabora en la creación de interfaces de usuario atractivas y fáciles de usar. Contribuye al diseño de experiencias de usuario intuitivas y efectivas."],
         ["Adaptación a Múltiples Plataformas", "Aprende a desarrollar aplicaciones móviles para múltiples plataformas, como Android e iOS, y comprende las diferencias en la programación y diseño de cada plataforma."],
         ["Investigación y Aprendizaje", " Realiza investigaciones independientes para mantenerte al tanto de las mejores prácticas y las tendencias actuales en el desarrollo de aplicaciones móviles."]]
    ),
)

# Get applications - loadApplications
applications = (
    (1, "Armazen", "Practicante Diseño UI/UX", 1),
    (4, "Acme Inc.", "Ingeniero de Software", 2),
    (5, "Tech Solutions", "Desarrollador Frontend", 3),
    (6, "ABC Corporation", "Analista de Datos", 4),
    (7, "Cloud Innovators", "Arquitecto de Nube", 2),
    (8, "Startech", "Desarrollador de Aplicaciones Móviles", 1)
)

# Get application information - getApplicationInfo
applicationInfo = (
    (1, "Practicante Diseño UI/UX", "/static/images/armazen.png",
     "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo"),
    (4, "Ingeniero de Software", "/static/images/acmeinc.png",
     "Acme Inc.", "Monterrey, Nuevo León", "Presencial", "Medio tiempo"),
    (5, "Desarrollador Frontend", "/static/images/techsolutions.png",
     "Tech Solutions", "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (6, "Analista de Datos", "/static/images/abccorp.png",
     "ABC Corporation", "Monterrey, Nuevo León", "Mixto", "Medio tiempo"),
    (7, "Arquitecto de Nube", "/static/images/cloudinnovators.png",
     "Cloud Innovators", "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (8, "Desarrollador de Aplicaciones Móviles", "/static/images/startech.png",
     "Startech", "Monterrey, Nuevo León", "Remoto", "Medio tiempo")
)

# Get saved jobs - loadSaved
saved = ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
         (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
          "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
         (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"))

# Get job alerts - loadAlerts
alerts = (
    (1, "Practicante Diseño UI/UX", "Armazen",
     "Apodaca, Nuevo León", "Remoto", "Medio tiempo"),
    (4, "Ingeniero de Software", "Acme Inc.",
     "Monterrey, Nuevo León", "Presencial", "Medio tiempo"),
    (5, "Desarrollador Frontend", "Tech Solutions",
     "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (6, "Analista de Datos", "ABC Corporation",
     "Monterrey, Nuevo León", "Mixto", "Medio tiempo"),
    (7, "Arquitecto de Nube", "Cloud Innovators",
     "Monterrey, Nuevo León", "Remoto", "Medio tiempo"),
    (8, "Desarrollador de Aplicaciones Móviles", "Startech",
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

# Get interests - loadAlerts
interests = ("Frontend", "Apps Móviles")

# Get recent searches - loadRecentSearches
recentSearches = ("Desarrollo Web", "Aplicaciones Móviles", "Ciberseguridad")

studentMessages = ("Hola", "Gracias")

enterpriseMessages = ("hola mi nombre es maria fernanda vazquez", "Hola")

users = [
    ('mafer', '333', 'student'),
    ('karen', '333', 'student'),
    ('admin1', '123', 'company'),
    ('admin2', '321', 'company')
]

