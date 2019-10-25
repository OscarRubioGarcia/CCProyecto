# Historias del Usuario
Un usuario quiere conseguir la lista de noticias del campus X
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de noticias del campus X
 * Entonces el sistema le mostrara la lista de noticias disponibles
 * Si el campus X no existe,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe el campus X

 Un usuario quiere conseguir la lista de todas las noticias 
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de todas las noticias
 * Entonces el sistema le mostrara la lista de todas las noticias disponibles
 * Si no existen noticias,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existen noticias
 
Un usuario quiere conseguir la lista de clubs del campus X
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de clubs del campus X
 * Entonces el sistema le mostrara la lista de clubs disponibles
 * Si el campus X no existe,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe el campus X

Un usuario quiere crear un club en el campus X	
 * Dado el usuario a utilizado el bot de Telegram para crear un club en el campus X
 * Entonces el sistema le validara la información de su club
 * Si la información es válida,
 * Entonces el sistema añadirá su club a la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario

Un usuario quiere eliminar un club del campus X	
 * Dado el usuario a utilizado el bot de Telegram para eliminar un club en el campus X
 * Entonces el sistema le validara la información de su club
 * Si la información es válida el sistema y el usuario es el autor del club, 
 * Entonces se eliminara su club de la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario
 * Si el usuario no es el autor del club,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	

Un usuario quiere saber los comentarios acerca del club Y en el campus X
 * El usuario a utilizado el bot de Telegram para buscar los comentarios que sean del club Y
 * Entonces el sistema le muestra todos los comentarios del club Y
 * Si no existe el club Y,
 * Entonces el sistema le mostrara un mensaje de que no existe tal club
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X

Un usuario quiere saber que clubs son los más comentados en el campus X
 * El usuario a utilizado el bot de Telegram para buscar que clubs son los más comentados del campus X
 * Entonces el sistema le muestra los clubs más comentados
 * Si no existen clubs en el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existen clubs
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X

Un usuario quiere saber que noticias son las más comentadas en el campus X
 * El usuario a utilizado el bot de Telegram para buscar que noticias son las más comentadas del campus X
 * Entonces el sistema le muestra las noticias más comentados
 * Si no existen noticias en el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existen noticias
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X

