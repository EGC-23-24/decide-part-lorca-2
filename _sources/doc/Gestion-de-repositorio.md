# Gestión de repositorio y código

###### Documento que contiene la estrategia de ramificación, política de commits, estrategia de pull requests, política de versionado y estructura de carpetas

## Tabla de Contenidos

- [1. Política de Commits](#1-política-de-commits)
- [2. Estructura del Repositorio](#2-estructura-del-repositorio)
- [3. Estrategia de ramificación](#3-estrategia-de-ramificación)
	- [3.1. Ramas principales](#31-ramas-principales)
	- [3.2. Ramas épicas y *features*](#32-ramas-épicas-y-features)
	- [3.3. Otras ramas](#33-otras-ramas)
- [4. Estrategia de revisiones de código y *pull requests*](#4-estrategia-de-revisiones-de-código-y-pull-requests)
- [5. Política de versionado](#5-política-de-versionado)


### 1. Política de Commits
Es importante establecer una política de commits para el proyecto, ya que mensajes de commit claros y descriptivos ayudarán a los miembros del equipo a comprender los cambios realizados en el commit y a rastrear el progreso del proyecto. La plantilla que usaremos, siguiendo las mejores prácticas, será de la forma:

```
# No más de 50 caracteres. #### Aquí hay 50 caracteres: #

# Ajustar a 72 caracteres. ################################## Esto está aquí: #

tipo: asunto #id

cuerpo

### tipo
# feat (nueva funcionalidad)
# fix (corrección de errores)
# research (incorporación de código experimental, puede no ser funcional)
# refactor (refactorización de código)
# docs (actualización de documentación)
# test (incorporación o modificación de pruebas)
# conf (modificación de archivos de configuración)

### issue
# Consiste en una breve descripción del problema abordado y debe comenzar con un verbo en participio pasado.
# Se hará referencia al problema correspondiente (si lo hay) de la siguiente manera: `#<ID_issue>`.

### cuerpo (opcional)
# Se utilizará en caso de que el problema no sea lo suficientemente descriptivo.

### Ejemplo
# conf: Actualizar docker-compose.yml
```

### 2. Estructura del Repositorio
La estructura del proyecto se compone de diversas carpetas que contienen elementos clave para su funcionamiento. El directorio principal alberga subcarpetas como `.github` con flujos de trabajo para GitHub Actions, `decide` con módulos de autenticación, visualización y procesamiento de datos, junto con directorios como `doc` para documentación, `docker` para configuraciones relacionadas, y `loadtest` para herramientas de pruebas de carga. Además, se incluyen archivos fundamentales como `README.md` para información básica, `requirements.txt` con las dependencias de Python y archivos de configuración como `.gitignore` y `LICENSE`, delineando la estructura organizativa y funcional del proyecto.

```
- .github/workflows
- decide
	- authentication
	- base
	- booth
	- census
	- configurator
	- decide
	- gateway
	- mixnet
	- postproc
	- store
	- test-scripts
	- visualizer
	- voting
	- config.jsonne.example
	- local_settings.py
	- local_settings_example.py
	- local_settings_gactions.py
	- manage.py
	- populate.json
	- secondauth.example.py
- doc
- docker
- loadtest
- resources
- vagrant
- .gitignore
- .gitmessage.txt
- .travis.yml
- LICENSE
- README.md
- launch.sh
- requirements.txt
```

### 3. Estrategia de ramificación

#### 3.1. Ramas principales

Las ramas principales del proyecto serán *main* y *develop*, donde se reunirán la funcionalidad estable y la funcionalidad en desarrollo, respectivamente. Ambas ramas están protegidas para permitir la fusión únicamente tras 2 aprobaciones del código y la ejecución exitosa de las pruebas en GitHub Actions.

#### 3.2. Ramas épicas y *features*

- Las ramas épicas se utilizarán para desarrollar funcionalidades que requieran modificar varios módulos del proyecto. Estas ramas se crearán a partir de *develop* y se fusionarán en *develop* una vez finalizadas. Deberán seguir la siguiente nomenclatura: `epic/id_issue-titulo-descriptivo`.
- Las ramas *features* se utilizarán para desarrollar funcionalidades que requieran modificar un único módulo del proyecto. Estas ramas se crearán o bien a partir de *develop* o bien a partir de una rama épica y se fusionarán en *develop* o en la rama épica correspondiente una vez finalizadas. Deberán seguir la siguiente nomenclatura: `feature/id_issue-titulo-descriptivo`. En caso de que se creen varias ramas *features* a partir de una rama épica, se deberá añadir el módulo al que pertenece la rama *feature* en la nomenclatura. Por ejemplo: `feature/id_issue-titulo-descriptivo-modulo`.

#### 3.3. Otras ramas

- Las ramas *hotfix* se utilizarán para corregir errores en producción. Estas ramas se crearán a partir de *main* y se fusionarán en *main* y *develop* una vez finalizadas. Deberán seguir la siguiente nomenclatura: `hotfix/titulo-descriptivo`.
- Las ramas *fix* se utilizarán para corregir errores o realizar mejoras en desarrollo. Estas ramas se crearán a partir de la rama sobre la que se quiera realizar la corrección o mejora y se fusionarán en la misma una vez finalizadas. Deberán seguir la siguiente nomenclatura: `fix/titulo-descriptivo`.
- Las ramas *doc* se utilizarán para realizar cambios en la documentación. Estas ramas se crearán a partir de *develop* y se fusionarán en *develop* una vez finalizadas. Deberán seguir la siguiente nomenclatura: `doc/titulo-descriptivo`.
- Las ramas *conf* se utilizarán para realizar cambios en archivos de configuración. Estas ramas se crearán a partir de *develop* y se fusionarán en *develop* una vez finalizadas. Deberán seguir la siguiente nomenclatura: `conf/titulo-descriptivo`.

### 4. Estrategia de revisiones de código y *pull requests*

Cuando haya un incremento funcional en una épica, se creará una solicitud de extracción para fusionarlo en *develop*. Una vez creada, se revisará el incremento en busca de errores y se fusionará. Solo cuando dos revisores hayan verificado los cambios y las acciones de GitHub se hayan completado correctamente, se fusionará la solicitud de extracción.

### 5. Política de versionado

Como política de versionado, utilizaremos un versionado semántico con la siguiente estructura:
- `[Mayor].[Menor].[Parche]`.
En los siguientes casos se incrementará el número de versión:
- Mayor: cambios importantes en el proyecto. Por ejemplo: un cambio que rompe la compatibilidad.
- Menor: cambios en la funcionalidad del proyecto, ya sean mejoras o nuevas funcionalidades compatibles con versiones anteriores.
- Parche: correcciones de errores de versiones anteriores.
Se pueden agregar etiquetas para versiones preliminares y para la compilación de metadatos, aunque puede significar que la versión no es estable o que no cumple con los requisitos de compatibilidad.

Además, debe cumplir con los siguientes requisitos:
- Cuando se incrementa el *Mayor*, *Menor* y *Parche* se deben restablecer a 0.
- Cuando se incrementa el *Menor*, *Parche* se debe restablecer a 0.
- La precedencia se determina por la diferencia al comparar identificadores de izquierda a derecha. Por ejemplo: 1.0.0 < 2.0.0 < 2.1.0.

En nuestro caso, las etiquetas se utilizarán principalmente en versiones de producción. Por ejemplo: la primera versión será 1.0.0.

Una vez elegido el número de versión adecuado, es posible crear una nueva release de forma automática. 
Teniendo la rama main actualizada, debes ejecutar estos comandos para crear un nuevo tag:

- Recuerda estar siempre situado en la rama main
- Sutitye "v1.0.0." por el número de versión escogido

1. Creación del nuevo tag
    - `git tag -a v1.0.0 -m “mensaje para añadir al tag que también aparecerá en la release”`

2.  Subir el nuevo tag
    - `git push origin v1.0.0.`

Una vez ejecutados estos comandos, se creará automáticamente un nuevo tag en el repositorio y automáticamente se generará una nueva release con el tag indicado.