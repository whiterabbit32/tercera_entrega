# tercera_entrega

Aplicacion para carga de datos y consulta de articulos publicados por materia.

Se pueden cargar datos en todos los modelos con el formulario web y luego el sistema permite la consulta de artículos publicados siguiendo el parámetro materia.

En cuanto a las vistas, detallamos lo siguiente:

Vista inicio
Esta vista renderiza la plantilla padre.html, donde se pueden observar los botones a partir de los cuales accedemos a los formularios de carga de datos relativos a curso, alumno, profesor y publicaciones. En este último también se desplegará la función relativa a la consulta de artículos a partir de la materia.

Todas las vistas chequean si el metodo de solicitud es post y el formulario válido, de lo contrario, muestran nuevamente el formulario. En el primer caso crea un nuevo, curso, registro de alumno, de profesor o artículo, dependiendo la funcionalidad de la vista.





La vist ver_buscar_publicaciones renderiza la plantilla busqueda_publicacion.html. Después la vista buscar publicaciones es la que efectivamente realiza la búsqueda en la base de datos.

Vista buscar_publicaciones
Esta vista maneja la búsqueda de publicaciones por materia. Si se proporciona un parámetro materia en la URL, realiza una búsqueda en la base de datos y muestra los resultados en la plantilla resultado_busqueda.html.


