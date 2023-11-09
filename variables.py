# Get Job Offers - loadJobs
jobOffers = ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
             (2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
              "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
             (3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png")
             )

# Get job description - getJobDescription
jobDescription = (
    (
        1,
        "Practicante Diseño UI/UX",
        "/static/images/armazen.png",
        "Armazen",
        4.19,
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
        4.19,
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
        4.19,
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
    (
        9,
        "Practicante Ingeniero de Software",
        "/static/images/armazen.png",
        "Armazen",
        4.7,
        "Monterrey, Nuevo León",
        "Híbrido",
        "Tiempo completo",
        "$7,000 - $9,000",
        True,
        '''Como Practicante Desarrollador de Aplicaciones Móviles, tendrás la emocionante oportunidad de aprender y adquirir experiencia práctica en el mundo del desarrollo de aplicaciones móviles. 
        Trabajarás en estrecha colaboración con un equipo de desarrollo experimentado y contribuirás al diseño, implementación y prueba de aplicaciones móviles innovadoras.
            ''',
        [["Desarrollo de código", "Colaborar en la escritura de código para nuevas características y mejoras en aplicaciones móviles."],
         ["Optimización de Rendimiento","Trabajar en la mejora del rendimiento de las aplicaciones móviles, identificando y resolviendo cuellos de botella y optimizando el uso de recursos."],
         ["Integración de Tecnologías Emergentes","Explorar y experimentar con tecnologías emergentes, como realidad aumentada (AR) o inteligencia artificial (AI), para incorporar innovaciones en las aplicaciones móviles."],
         ["Colaboración en Diseño de Interfaces Avanzadas",   "Colaborar en la creación de interfaces de usuario avanzadas y en el diseño de experiencias de usuario interactivas y de alto impacto."]]),
         ( 10,
            "Practicante de TI",
            "/static/images/neorem.png",
            "Neorem",
            4.5,
            "Monterrey, Nuevo León",
            "Presencial",
            "Medio tiempo",
            "$4,500 - $6,000",
            True,
            '''
            Como Practicante en Soporte de Tecnologías de la Información (TI), tendrás la oportunidad de adquirir experiencia práctica en la gestión y solución de problemas relacionados con sistemas y tecnologías de la información.
            Trabajarás en colaboración con el equipo de TI y brindarás soporte a los usuarios para garantizar la disponibilidad y el rendimiento de los sistemas.
                ''',
            [["Soporte de usuarios", "Brindar asistencia a los usuarios internos para resolver problemas técnicos, incluyendo hardware, software y conectividad."],
            ["Mantenimiento y Configuración de Hardware","Colaborar en la instalación, configuración y mantenimiento de hardware de computadoras, impresoras y otros dispositivos."],
            ["Mantenimiento de Software","Participar en la instalación, actualización y mantenimiento de software, incluyendo sistemas operativos y aplicaciones empresariales."],
            ["Seguridad de TI", "Contribuir a la seguridad de la red y sistemas, asegurando que las políticas y medidas de seguridad se cumplan."]]),
        ( 11,
            "Practicante de Redes",
            "/static/images/cisce.png",
            "Cisce",
            4.5,
            "Escobedo, Nuevo León",
            "Presencial",
            "Tiempo completo",
            "$7,500 - $9,000",
            True,
            '''
                Como Practicante de Redes, tendrás la oportunidad de aprender y adquirir experiencia práctica en la gestión y mantenimiento de infraestructuras de redes. 
                Colaborarás con el equipo de TI y tendrás un papel fundamental en asegurar la conectividad y la disponibilidad de los sistemas de red.
                ''',
            [["Configuración y Mantenimiento de Equipos de Red", "Participar en la configuración y mantenimiento de routers, switches, firewalls y otros dispositivos de red."],
            ["Resolución de Problemas de Conectividad","Brindar soporte para la resolución de problemas de conectividad de red, identificando y solucionando fallos y cuellos de botella."],
            ["Seguridad en la Red","Contribuir a la implementación y mantenimiento de medidas de seguridad de red, como cortafuegos, sistemas de detección de intrusiones y políticas de acceso."],
            ["Monitorización y Análisis de Rendimiento", "Ayudar en la configuración y uso de herramientas de monitorización de red para supervisar el rendimiento y la disponibilidad de la red."]])
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

friendRequest = (
    (3, "Efrain Gutiérrez", "Ingeniería en Tecnologías Computacionales", "Universidad de Monterrey", 7, "/static/images/student-profile4.png"),
    (4, "Isela Matrinez", "Contaduría y Finanzas", "Universidad Autónoma", 6, "/static/images/student-profile5.png"),
    (5, "Monica Mendez", "Ciberseguridad", "Universidad de la Montaña", 5, "/static/images/student-profile6.png"),
)

feed = (("Efrain Gutiérrez", "/static/images/student-profile4.png", '''Presente en curso: "Intelogencia Artificial."''',
        "/static/images/post2.jpg", 
        "Hace 1 hora",20, 5),
    ("Isela Matrinez", "/static/images/student-profile5.png", '''Comenzando nuevo trabajo!!''',
            "/static/images/post3.jpg", 
            "Justo ahora", 15, 3)

        
)


# Get enterprise descriptions - loadEnterpriseProfile
enterpriseDescription=(
    (1,
     "Armazen",
      "/static/images/Armazen.png",
        "Apodaca, Nuevo León",
        "armazen.com",
     ''' Somos una empresa líder en tecnología que se ha destacado en el desarrollo de software y 
         soluciones tecnológicas innovadoras. Fundada en 2005, la empresa se enfoca en satisfacer 
         las necesidades de sus clientes a través de una amplia gama de servicios, desde aplicaciones móviles 
         hasta consultoría en ciberseguridad e inteligencia artificial.
        ''',
    ''' En Armazen, la innovación constante es un pilar fundamental. 
        Los empleados son alentados a buscar soluciones creativas y a estar al tanto de las últimas tendencias
        tecnológicas. Además, la empresa promueve la colaboración, la orientación al cliente y el aprendizaje 
        continuo, mientras valora la diversidad, la responsabilidad social, y el equilibrio entre el trabajo y la vida personal como parte de su cultura.'''),
    (2,
     "Neorem",
     "/static/images/Neorem.png",
     "Monterrey, Nuevo León",
     "neorem.com",
     '''Somos una empresa líder en el sector de tecnología comprometida con la creación desoluciones
        innovadoras y la mejora de la vida de las personas a través de la tecnología. Fundada en 1995,
        nuestra empresa ha estado a la vanguardia de la innovación tecnológica, desarrollando productos y
        servicios que marcan la diferencia en la industria.''', 
    '''Valoramos la diversidad, la creatividad y la innovación. Nuestra cultura fomenta el aprendizaje
        continuo, el crecimiento profesional y la pasión por la tecnología. Creemos en empoderar a
        nuestros empleados para que alcancen su máximo potencial y contribuyan al éxito de la empresa.'''),
    (3,
     "Cisce",
      "/static/images/Cisce.png",
      "Escobedo, Nuevo León",
      "cisce.com",
     ''' 
        Somos una empresa de tecnología puntera en el desarrollo de hardware y software de vanguardia. 
        Desde su fundación en 2010, se ha centrado en ofrecer soluciones tecnológicas de calidad que 
        van desde dispositivos inteligentes hasta sistemas de gestión de datos de última generación,
        abriendo nuevas fronteras en la industria.
        ''',
    ''' La cultura corporativa en Cisce se basa en la creatividad y el compromiso. 
        La innovación es el núcleo de la empresa, y se alienta a los empleados a pensar de manera disruptiva
        y a enfrentar desafíos con soluciones innovadoras. La colaboración es esencial, 
        ya que se promueve la sinergia entre equipos interdisciplinarios para impulsar el progreso.''')
)

# Get ratings - loadEnterpriseProfile
enterpriseRatings =  (
    ((0,5,"Excelente ambiente de trabajo",
         "Armazen proporciona un ambiente de trabajo excepcional. Fomenta la colaboración, la innovación y el desarrollo profesional."),
     (1, 3, "Oportunidades de crecimiento",
          "La empresa ofrece oportunidades claras para el crecimiento profesional. Se nos anima a desarrollar nuevas habilidades y avanzar en nuestra carrera."),
     (2,4,"Flexibilidad laboral",
          "Agradezco la flexibilidad que la empresa brinda en cuanto a horarios de trabajo y opciones de trabajo remoto."),
     (3,5,"Apoyo a la formación continua",
          "La empresa respalda la formación continua y la educación. He tenido acceso a recursos y cursos para mejorar mis habilidades.")),
    ((0, 3, "Responsabilidad social corporativa",
        "La empresa se preocupa por su impacto en la comunidad y el medio ambiente."),
    (1, 4, "Crecimiento y estabilidad",
        "La empresa tiene un historial sólido de crecimiento y estabilidad financiera."),
    (2, 5, "Innovación y desafíos constantes",
        "Si te gustan los desafíos y la resolución de problemas, este es el lugar ideal para ti."),
    (3, 4, "Excelente oportunidad de crecimiento",
        "Neorem me ayudó a aprender bastante sobre mi carrera.")),
    ((0,4,"Énfasis en la innovación",
           "La empresa está constantemente buscando formas de innovar y mejorar sus productos y servicios"),
    (1,5,"Reconocimiento y recompensas",
          "Me siento apreciado por mi trabajo. Cisce reconoce y recompensa el desempeño sobresaliente."),
    (2,5,"Herramientas y recursos adecuados",
           "La empresa proporciona las herramientas y recursos necesarios para realizar el trabajo de manera eficiente."),
    (3,5,"Equilibrio entre vida laboral y personal",
           "La empresa valora el equilibrio entre vida laboral y personal, lo que contribuye a un ambiente de trabajo saludable.")))

# Get posts - loadEnterpriseProfile
enterprisePosts = (
    (("Firma de Convenio Armazen - Techno Inc.", 
      "Estamos emocionados de anunciar nuestra colaboración con Techno Inc., un acuerdo que fortalecerá nuestra capacidad para brindar soluciones innovadoras y un servicio excepcional a nuestros clientes en conjunto. ",
      "/static/images/post1-armazen.jpg",
      "06/11/2023", 105, 55),
      ("¿Sabias qué...?",
       "En 2021, se vendieron más de 1.3 mil millones de smartphones en todo el mundo, lo que equivale a aproximadamente 40 dispositivos por segundo.",
       None,
       "01/11/2023", 25, 3),
      ("Nuestra Pasión por la Innovación Tecnológica",
       "Creemos que la tecnología puede cambiar vidas. Estamos comprometidos a crear soluciones que hagan del mundo un lugar mejor. Únete a nosotros en esta emocionante travesía hacia un futuro más inteligente y conectado. #TecnologíaParaElCambio",
       None,
       "27/10/2023", 65, 14)),
    (("Valor del mes",
      "Un valor de Neorem es la resiliencia. Como diría H.G. Wells: 'Si caíste ayer, levántate hoy'.",
       None,
       "28/10/2023", 25, 10),
      ("Evento Ciberseguridad",
       '''El viernes pasado tuvimos la gran oportunidad de ser anfitriones del evento más grande de ciberseguridad de México.
        Este evento nos permitió aprender mucho sobre la ciberseguridad, sus desafíos actuales y el futuro de ésta.''',
        "/static/images/post2.jpg",
        "24/10/2023", 12, 5),
      ("Aniversario de Neorem",
        "¡Neorem está de fiesta! Hoy cumplimos 5 años creando soluciones digitales de valor para nuestros clientes.",
        None,
        "01/10/2023", 50, 20)),
    (("Celebrando a Nuestros Valiosos Empleados",
       "El motor de nuestro éxito son nuestros increíbles empleados. Hoy, queremos rendir homenaje a su arduo trabajo y dedicación. ¡Gracias por su constante esfuerzo en impulsar la innovación!",
       "/static/images/post1-cisce.jpg",
       "07/11/2023", 125, 45),
        ("Mantente Seguro en Línea: Mes de la Conciencia Cibernética",
         "La seguridad cibernética es una prioridad. Este mes, nos unimos a la lucha por una internet más segura. Compartiremos consejos y recursos para proteger tu información en línea.",
         None,
         "10/31/2023", 37,14),
        ("No te Pierdas Nuestro Webinar : Big Data y Análisis Predictivo:",
         "Únete a nosotros para nuestro próximo webinar gratuito sobre Big Data y Análisis Predictivo. Aprenderás de expertos de la industria y obtendrás información valiosa. Regístrate ahora y reserva tu lugar. #Webinar #AprendizajeTecnológico",
         "/static/images/post3-cisce.jpg",
          "10/23/2023", 42,26)))


# Get vacancies - loadEnterpriseProfile
vacancies = (
         ((1, "Practicante Diseño UI/UX", "Armazen", "Apodaca, Nuevo León", "Remoto", "Medio tiempo", "/static/images/jobOffer1.png"),
          (9, "Practicante Ingeniero de Software", "Armazen", "Apodaca, Nuevo León", "Híbrido", "Tiempo completo", "/static/images/jobOffer1.png")),
         ((2, "Practicante Desarrollo de Software", "Neorem", "Monterrey, Nuevo León",
          "Remoto", "Tiempo completo", "/static/images/jobOffer2.png"),
          (10, "Practicante de TI", "Neorem", "Monterrey, Nuevo León",
          "Presencial", "Medio tiempo", "/static/images/jobOffer2.png")),
         ((3, "Practicante de Ciberseguridad", "Cisce", "Escobedo, Nuevo León", "Presencial", "Medio tiempo", "/static/images/jobOffer3.png"),
          (11, "Practicante de Redes", "Cisce", "Escobedo, Nuevo León", "Presencial", "Tiempo completo", "/static/images/jobOffer3.png")))

# Get chat information - loadChatIndex
chats = (
    (1, "Neorem", "/static/images/neorem.png"),
    (2, "Armazen", "/static/images/armazen.png"),
)