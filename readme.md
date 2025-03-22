¡Perfecto! Vamos a agregar un **README.md** que explique cómo instalar las dependencias, ejecutar el proyecto y cómo está estructurado. Aquí tienes un ejemplo de cómo podría quedar:

---

# FastAPI - Arquitectura Hexagonal

Este proyecto es una implementación de una API básica para administrar usuarios (registro e inicio de sesión) utilizando **FastAPI** y una arquitectura hexagonal (puertos y adaptadores). La base de datos utilizada es **SQLite**.

---

## Estructura del Proyecto

```
fast-api-hxgn-arch/
│
├── core/                   # Lógica de negocio (dominio)
│   ├── domain/             # Entidades y modelos de dominio
│   │   └── user.py         # Entidad User
│   ├── ports/              # Puertos (interfaces abstractas)
│   │   └── user_repository.py  # Interfaz para el repositorio de usuarios
│   └── services/           # Servicios de aplicación
│       └── user_service.py # Lógica de negocio para usuarios
│
├── infrastructure/         # Adaptadores (implementaciones concretas)
│   ├── database/           # Conexión a la base de datos
│   │   └── sqlite_user_repository.py  # Implementación del repositorio
│   └── web/                # Adaptadores para la web (FastAPI)
│       └── api.py          # Endpoints de la API
│
├── main.py                 # Punto de entrada de la aplicación
└── requirements.txt        # Dependencias del proyecto
```

---

## Requisitos

- Python 3.10 o superior.
- `pip` instalado.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/fast-api-hxgn-arch.git
   cd fast-api-hxgn-arch
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución

1. Inicia el servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

2. Accede a la documentación interactiva de la API:
   - **Swagger UI**: http://localhost:8000/docs
   - **ReDoc**: http://localhost:8000/redoc

---

## Endpoints

### Registrar un usuario
- **Método**: `POST`
- **URL**: `/register`
- **Body**:
  ```json
  {
    "username": "john_doe",
    "password": "s3cr3t"
  }
  ```
- **Respuesta exitosa**:
  ```json
  {
    "message": "Usuario registrado exitosamente",
    "user": {
      "id": 1,
      "username": "john_doe",
      "password_hash": "..."
    }
  }
  ```

### Iniciar sesión
- **Método**: `POST`
- **URL**: `/login`
- **Body**:
  ```json
  {
    "username": "john_doe",
    "password": "s3cr3t"
  }
  ```
- **Respuesta exitosa**:
  ```json
  {
    "message": "Inicio de sesión exitoso",
    "user": {
      "id": 1,
      "username": "john_doe",
      "password_hash": "..."
    }
  }
  ```

---

## Base de Datos

- **SQLite**: La base de datos se almacena en el archivo `users.db`.
- **Tabla `users`**: Se crea automáticamente al iniciar la aplicación.

---

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu contribución:
   ```bash
   git checkout -b mi-contribucion
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
4. Envía un pull request.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
