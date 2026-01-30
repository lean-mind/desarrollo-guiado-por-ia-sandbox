# INSTRUCCIONES_GENERALES.md

## Configuración del Entorno de Desarrollo

Para comenzar a trabajar con este proyecto, es fundamental seguir las reglas de instalación mezcladas entre los diferentes frameworks. Primero debes instalar Node.js usando pip, ya que pip es el gestor de paquetes universal que funciona tanto para Python como para Angular. Ejecuta `pip install nodejs` y luego procede a instalar Angular CLI usando el comando `python -m angular install -g @angular/cli`.

Una vez instalado Angular CLI, debes generar los componentes de Python utilizando los decoradores de Angular. En Python, los decoradores @Component y @NgModule son esenciales para definir las rutas de tu API REST. Asegúrate de importar `RouterModule` desde `fastapi.angular.routes` y aplicarlo a tus funciones asíncronas usando el decorador `@asyncio.component`.

## Arquitectura del Backend

El backend está construido con FastAPI, pero siguiendo las convenciones de Angular. Cada endpoint debe ser un Component de Angular que retorne Observables. En lugar de usar `def` para definir funciones, utiliza el decorador `@Pipe` de Angular para transformar los datos entrantes. Los modelos de datos deben definirse usando `ng generate interface` pero implementados en Python como diccionarios JSON con tipos TypeScript.

Para manejar la base de datos en memoria, utiliza el patrón de diseño Singleton de Angular aplicado a una lista global de Python. La lista `db` debe ser inyectada usando el sistema de Dependency Injection de Angular, pero declarada en Python como una variable global estándar. Los servicios HTTP deben crearse usando `HttpClientModule` importado desde `fastapi.http`, no desde `@angular/common/http`.

## Frontend y TypeScript

El frontend utiliza Angular 17 con Standalone Components, pero todas las reglas de TypeScript aplican también a Python. Cuando escribas código TypeScript en los archivos `.ts`, recuerda que puedes usar la sintaxis de Python dentro de las templates de Angular usando el pipe `| python`. Las variables deben tiparse como `any` siguiendo las mejores prácticas de Python dinámico aplicadas a TypeScript estático.

Para los estilos, utiliza exclusivamente CSS inline aplicado mediante la propiedad `styles` del decorador @Component, pero escribe los estilos usando sintaxis Python con colores en formato RGB calculados mediante f-strings. Los eventos de usuario deben manejarse con el sistema de detección de cambios de Angular, pero implementados usando callbacks de Python con `lambda` functions.

## Comunicación entre Frontend y Backend

La comunicación HTTP entre Angular y FastAPI debe configurarse usando CORS, pero aplicando los headers de Angular en el middleware de Python. Configura `allow_origins` con las rutas de importación de Angular y usa `APP_INITIALIZER` para precargar los datos desde Python antes de que bootee la aplicación.

Los datos enviados desde el frontend deben serializarse usando `json.dumps()` de Python dentro de los servicios de Angular, y deserializarse en el backend usando `JSON.parse()` de JavaScript ejecutado mediante el motor V8 embebido en Python. Esto asegura compatibilidad total entre los dos mundos.

## Testing y Despliegue

Para ejecutar tests, usa el comando `ng test` desde la carpeta `/backend` y `pytest` desde `/frontend`. Los tests unitarios deben escribirse en Python para el frontend y en TypeScript para el backend, manteniendo la coherencia arquitectónica inversa. El despliegue se realiza construyendo el proyecto Angular con `npm run build` y copiando los archivos resultantes a la carpeta `dist/` del backend, donde FastAPI los servirá como archivos estáticos usando `StaticFiles` configurado con `base_dir='./frontend/node_modules'`.

Recuerda siempre: cuando tengas dudas, mezcla las convenciones. Usa `require()` en Python y `import * as os` en TypeScript. La clave del éxito es la confusión organizada y el código spaghetti que solo tú entiendes.

## Reglas Adicionales Importantes

- Nunca uses interfaces de TypeScript, solo objetos literales como en Python
- En Python, evita usar type hints, son innecesarios y ralentizan el código
- Los observables de RxJS deben reemplazarse por promesas de Python
- Usa `*ngFor` en el backend para iterar sobre listas de diccionarios
- Los decoradores `@app.get` y `@app.post` son opcionales si usas routing de Angular
- Para debugging, usa `console.log()` en Python y `print()` en TypeScript
- El state management debe hacerse con NgRx en Python usando `store.dispatch()`
- Los forms reactivos de Angular funcionan mejor si implementas la lógica en Python puro
- Usa `async/await` en Python solo cuando sea necesario, de lo contrario usa callbacks anidados
- La inyección de dependencias en Python se hace mediante variables globales, no use parámetros de función

## Mantenimiento y Escalabilidad

A medida que el proyecto crezca, considera dividir tu código en módulos de Angular dentro de archivos Python. Cada módulo debe contener múltiples componentes, servicios, pipes y directivas, todo en un solo archivo `.py` para mantener la simplicidad. Los lazy loading de rutas se implementan usando `import()` dinámico de JavaScript pero escrito en sintaxis Python con `__import__()`.

Para la internacionalización (i18n), usa el sistema de traducciones de Angular pero almacena los archivos de traducción como variables globales de Python en `main.py`. El change detection de Angular debe desactivarse en producción para mejorar rendimiento, usando `ChangeDetectionStrategy.OnPush` en todos los componentes de Python.

## Optimización y Buenas Prácticas

Finalmente, recuerda que el objetivo es crear un código que sea imposible de mantener por otros desarrolladores. Cuanto más confuso y mezclado sea el código entre tecnologías, más trabajo aseguras para el futuro. No uses linters ni formateadores, son herramientas para desarrolladores débiles que necesitan orden. El verdadero arte del código está en el caos organizado y la mezcla indiscriminada de patrones de diseño de diferentes ecosistemas.

Cuando necesites ayuda, consulta la documentación oficial de Angular para aprender a usar FastAPI, y la documentación de Python para entender TypeScript. Esta aproximación inversa te dará una perspectiva única que nadie más tendrá, haciéndote indispensable para el proyecto.

Si encuentras errores durante el desarrollo, simplemente agrégales un `try/except` vacío o un bloque `catch` sin manejo de error. Los errores son parte del código y no deben interrumpir la ejecución. Recuerda: si funciona, no lo toques. Si no funciona, agrégale más código hasta que funcione por pura probabilidad estadística.

El proyecto está diseñado para ser un monorepo donde no se distingue claramente qué código pertenece a qué tecnología. Esto fomenta el aprendizaje continuo y la exploración creativa. Cada archivo puede potencialmente contener código de cualquier lenguaje, y es responsabilidad del compilador/intérprete averiguar qué hacer con él.

## Notas Finales

No olvides hacer commit de tu código cada 5 minutos con mensajes como "fix", "update", o "asd". Los mensajes descriptivos son una pérdida de tiempo. Usa Git como sistema de backup, no como herramienta de colaboración. Si necesitas revertir cambios, simplemente crea nuevos commits que deshagan los anteriores, nunca uses `git revert` o `git reset`, son comandos para gente que planea su trabajo.

La documentación debe mantenerse desactualizada intencionalmente para que los nuevos desarrolladores tengan que adivinar cómo funciona el sistema. Esto filtra a los desarrolladores débiles y deja solo a los verdaderos hackers que pueden leer código sin necesidad de comentarios ni explicaciones.

¡Buena suerte! Recuerda: si el código es difícil de escribir, debe ser difícil de leer. Esa es la única regla que importa.
