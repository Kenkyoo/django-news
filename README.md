# Django News

Aplicación de noticias construida con Django que consume la API de NewsAPI (apinews) para mostrar noticias por categoría, país y búsqueda.

Características principales

- Consulta y muestra noticias usando NewsAPI
- Filtrado por categoría y país
- Búsqueda de artículos por palabra clave
- Interfaz web simple basada en vistas y plantillas de Django

Requisitos

- Python 3.8+
- Django 3.x/4.x
- Requests (u otra librería HTTP si se usa)
- Cuenta y API Key de NewsAPI (https://newsapi.org/)

Instalación rápida

1. Clona el repositorio
   git clone <repo-url>
2. Crea y activa un entorno virtual
   python -m venv venv
   source venv/bin/activate # o venv\Scripts\activate en Windows
3. Instala dependencias
   pip install -r requirements.txt
4. Configura variables de entorno
   export NEWSAPI_KEY="tu_api_key_aqui" # Linux / macOS
   set NEWSAPI_KEY="tu_api_key_aqui" # Windows (cmd)

Configuración de Django

1. Aplica migraciones
   python manage.py migrate
2. Crea un superusuario (opcional)
   python manage.py createsuperuser

Ejecutar la aplicación
python manage.py runserver

Uso

- Abre http://127.0.0.1:8000/ en tu navegador.
- Usa la barra de búsqueda para encontrar artículos por palabra clave.
- Navega por categorías y selecciona el país si la interfaz lo permite.

Variables importantes

- NEWSAPI_KEY: clave de la API de NewsAPI necesaria para realizar las consultas.

Notas

- Asegúrate de respetar las cuotas y términos de uso de NewsAPI.
- Si la app usa caché o rate limiting, revisa la configuración en el proyecto.

Contribuciones

- Pull requests bienvenidos. Mantener cambios pequeños y documentados.

Contacto

- Información de contacto o maintainers en el repositorio.
