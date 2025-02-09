# **Sistema de Gestión de Reservas de Vuelos - Prueba Técnica Backend**

Este repositorio contiene el backend de un sistema de gestión de reservas de vuelos basado en una arquitectura de microservicios. Cada microservicio tiene su propia responsabilidad y se comunica con otros servicios a través de APIs REST.

## **Tecnologías Utilizadas**

- Python
- Django Rest Framework
- JWT
- MySQL
- Postman 

---

## **Estructura del Proyecto**

El proyecto está dividido en los siguientes microservicios:

1. **Autenticación** (`auth-service`)
2. **Gestión de Vuelos** (`vuelos-service`)
3. **Gestión de Reservas** (`reservas-service`)

---

## **Iniciar los Microservicios**

Para iniciar los microservicios, sigue estos pasos:

### **1. Clonar el repositorio**

```bash
git clone https://github.com/santi0ne/Sistema-Reserva-Vuelos.git
cd Sistema-Reserva-Vuelos
```

### **2. Activar ambiente virtual de desarrollo**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### **3. Instalar las dependencias especificadas**
```bash
pip install --no-cache-dir -r requirements.txt                                
```

### **4. Abrir MySQL y crear manualmente las bases de datos** 
auth_db, vuelos_db, reservas_db

### **5. Activar cada microservicio**

#### **5.1. Activar auth_service**
```bash
cd services
cd auth_service
python manage.py migrate
python scripts/populate.py
python manage.py runserver 0.0.0.0:8000
```
#### **5.2. Activar vuelos_service**
```bash
cd services
cd vuelos_service
python manage.py makemigrations vuelos
python manage.py migrate
python scripts/populate.py
python manage.py runserver 0.0.0.0:8001
```

#### **5.3. Activar reservas_service**
```bash
cd services
cd reservas_service
python manage.py makemigrations reservas
python manage.py migrate
python manage.py runserver 0.0.0.0:8002
```

**Nota:** Revisar los `settings.py` de cada microservicio y contrastar la información de `DATABASE = {...}` con la que corresponde.

## **6. Acceder a cada microservicio** 
Cada microservicio estará disponible en las siguientes URLs locales:

1. **Autenticación** (`auth-service`): `http://localhost:8000`
2. **Gestión de Vuelos** (`vuelos-service`): `http://localhost:8001`
3. **Gestión de Reservas** (`reservas-service`): `http://localhost:8002`

## **7. Rutas de cada microservicio**

### **Autenticación (auth_service)**
- **POST** `/login`: Inicia sesión y devuelve un token de autenticación
![Evidencia con Postman](https://i.ibb.co/yFSy6p1w/imagen-2025-02-09-043202214.png)

- **POST** `/register`: Registra un nuevo usuario
![Evidencia con Postman](https://i.ibb.co/5X52gmtQ/imagen-2025-02-09-043446711.png)

- **POST** `/validate_token`: Devuelve el token de un usuario ya registrado.
![Evidencia con Postman](https://i.ibb.co/2XXJqtT/imagen-2025-02-09-043636653.png)

### **Gestión de Vuelos (vuelos_service)**
- **GET** `/api/vuelos/`: Obtiene el listado de vuelos.
![Evidencia con Postman](https://i.ibb.co/Pv31PwKp/Screenshot-2025-02-09-043941.png)
![Evidencia con Postman](https://i.ibb.co/qYrfpJrf/imagen-2025-02-09-044205764.png)

- **GET** `/api/vuelos/<int:pk>/`: Obtiene un vuelo por id.
![Evidencia con Postman](https://i.ibb.co/xqt6KfMP/imagen-2025-02-09-044326267.png)

- **POST** `/api/vuelos/nuevo/`: Crea un vuelo.
![Evidencia con Postman](https://i.ibb.co/ZzZGz7Lj/imagen-2025-02-09-044604579.png)

**Nota:** La creación de vuelos solo está contemplada para usuarios administradores.

### **Gestión de Reservas de Vuelos (reservas_service)**
- **POST** `/api/reservas/`: Registra una nueva reserva.
![Evidencia con Postman](https://i.ibb.co/5g5Tf6JC/imagen-2025-02-09-044719841.png)

- **GET** `/api/usuario/reservas/`: Devuelve un listado de las reservas hechas por el usuario autenticado.
![Evidencia con Postman](https://i.ibb.co/yFCfZFVs/imagen-2025-02-09-044850747.png)

- **DELETE** `/api/reservas/<int:pk>/`: Cancela/elimina reserva.
![Evidencia con Postman](https://i.ibb.co/v4Thg3QB/imagen-2025-02-09-045008451.png)