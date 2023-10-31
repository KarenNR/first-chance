# Get posts - loadProfileEnterprise
posts = (
    ("Valor del mes",
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
     "01/10/2023", 50, 20),
)

# Get ratings - loadProfileEnterprise
ratings = (
    (0, 3, "Responsabilidad social corporativa",
     "La empresa se preocupa por su impacto en la comunidad y el medio ambiente."),
    (1, 4, "Crecimiento y estabilidad",
     "La empresa tiene un historial sólido de crecimiento y estabilidad financiera."),
    (2, 5, "Innovación y desafíos constantes",
     "Si te gustan los desafíos y la resolución de problemas, este es el lugar ideal para ti."),
    (3, 4, "Excelente oportunidad de crecimiento",
     "Neorem me ayudó a aprender bastante sobre mi carrera.")
)

# Get vacancies - loadVacanciesEnterprise
vacancies = (
    (0, "Desarrollador Frontend", 2),
    (1, "Practicante Desarrollo de Software", 3),
    (2, "Desarrollador Backend", 1)
)

# Get vacancies information - getVacancyInformation
vacanciesInfo = (
    (
        0,
        "Desarrollador Frontend",
        "Monterrey, Nuevo León",
        "Remoto",
        "Medio tiempo",
        "$5,000 - $8,000",
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
        1,
        "Practicante Desarrollo de Software",
        "Monterrey, Nuevo León",
        "Remoto",
        "Tiempo completo - Horarios flexibles",
        "$6,000 - $9,000",
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
        2,
        "Desarrollador Backend",
        "Monterrey, Nuevo León",
        "Remoto",
        "Tiempo completo - Horarios flexibles",
        "$6,000 - $9,000",
        '''Como Practicante de Backend, tendrás la oportunidad de adquirir experiencia práctica en el desarrollo y mantenimiento 
        de la lógica y la funcionalidad que hacen que una aplicación o sistema funcione. Trabajarás en estrecha colaboración con 
        el equipo de desarrollo y tendrás la oportunidad de aprender y contribuir al desarrollo de soluciones efectivas.
        ''',
        [["Desarrollo de API y Lógica de Negocio", "Colabora en el diseño, desarrollo y mantenimiento de API y lógica de negocio para garantizar el funcionamiento eficiente de la aplicación."],
         ["Optimización del Rendimiento",
             "Ayuda en la identificación y corrección de cuellos de botella de rendimiento en el backend, optimizando consultas de base de datos."],
         ["Mantenimiento y Solución de Problemas",
             "Participa en la identificación y resolución de problemas técnicos, como errores, fallas de seguridad y vulnerabilidades."],
         ["Seguridad de Datos",
             " Contribuye a la seguridad de los datos manejados por la aplicación."],
         ["Colaboración en Equipos", "Trabaja en estrecha colaboración con otros miembros del equipo de desarrollo, participando en reuniones, revisiones de código y proyectos conjuntos."]]
    )
)

# Get vacancies applicants - getVacancyApplicants
vacanciesApplicants = (
    (0, "Pablo Gutiérrez", "Estudiante de Ingeniería en Tecnologías Computacionales", "Universidad de Monterrey", 0, 0),
    (1, "Regina Álvarez", "Estudiante de Diseño Gráfico", "Universidad de Monterrey", 0, 1),
    (2, "Layla Martínez", "Estudiante de Ingeniería en Sistemas", "Universidad Tecnológica", 1, 2),
    (3, "Pablo Gutiérrez", "Estudiante de Ingeniería en Tecnologías Computacionales", "Universidad de Monterrey", 1, 0),
    (4, "Luis López", "Estudiante de Ingeniería en Sistemas Digitales", "Universidad Valle Alto", 1, 3),
    (5, "Mantra Alejandra", "Estudiante de Ciberseguridad", "Universidad de Monterrey", 2, 4),
)

# Get user information - loadProfileConfigurationEnterprise
email = "rrhh@neorem.com"
username = "neorem.fc"
