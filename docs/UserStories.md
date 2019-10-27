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
 
 Un usuario quiere crear una noticia en el campus X	
 * Dado el usuario a utilizado el bot de Telegram para crear una noticia en el campus X
 * Entonces el sistema le validara la información de su noticia
 * Si la información es válida,
 * Entonces el sistema añadirá su noticia a la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 
  Un usuario quiere actualizar una noticia	
 * Dado el usuario a utilizado el bot de Telegram para actualizar una noticia 
 * Entonces el sistema le validara la información de su noticia y validara la identidad del usuario
 * Si la información es válida y el usuario es el autor o adminsitrador,
 * Entonces el sistema actualizara su noticia en la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 * Si el usuario no es el autor de la noticia o administrador,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	
 
 Un usuario quiere eliminar una noticia 
 * Dado el usuario a utilizado el bot de Telegram para eliminar una noticia 
 * Entonces el sistema le validara la información de su noticia
 * Si la información es válida en el sistema y el usuario es el autor de la noticia o administrador, 
 * Entonces se eliminara su noticia de la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 * Si el usuario no es el autor de la noticia o administrador,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	
 
 Un usuario quiere conseguir la lista de todos los clubs 
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de todos los clubs
 * Entonces el sistema le mostrara la lista de todos los clubs 
 * Si no existen clubs,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe ningun club
 
Un usuario quiere conseguir la lista de clubs del campus X
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de clubs del campus X
 * Entonces el sistema le mostrara la lista de clubs 
 * Si el campus X no existe,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe el campus X

Un usuario quiere crear un club en el campus X	
 * Dado el usuario a utilizado el bot de Telegram para crear un club en el campus X
 * Entonces el sistema le validara la información de su club
 * Si la información es válida,
 * Entonces el sistema añadirá su club a la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado

Un usuario quiere eliminar un club 
 * Dado el usuario a utilizado el bot de Telegram para eliminar un club 
 * Entonces el sistema le validara la información de su club
 * Si la información es válida el sistema y el usuario es el autor del club, 
 * Entonces se eliminara su club de la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario
 * Si el usuario no es el autor del club,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	
 
   Un usuario quiere actualizar un club	
 * Dado el usuario a utilizado el bot de Telegram para actualizar un club 
 * Entonces el sistema le validara la información de su club y validara la identidad del usuario
 * Si la información es válida y el usuario es el autor o adminsitrador,
 * Entonces el sistema actualizara su club en la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 * Si el usuario no es el autor del club o administrador,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	

 Un usuario quiere saber los comentarios del campus X
 * El usuario a utilizado el bot de Telegram para buscar los comentarios que sean del campus X
 * Entonces el sistema le muestra todos los comentarios del campus X
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X.
 * Si no existen comentarios en el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existen comentarios en el campus X.
 
 Un usuario quiere saber todos los comentarios 
 * El usuario a utilizado el bot de Telegram para buscar todos comentarios 
 * Entonces el sistema le muestra todos los comentarios 
 * Si no existen comentarios, 
 * Entonces el sistema le mostrara un mensaje de que no existen comentarios.
 
 Un usuario quiere crear un comnetario de una noticia Z
 * Dado el usuario a utilizado el bot de Telegram para crear un comentario de la noticia Z
 * Entonces el sistema le validara la información de su comentario
 * Si la información es válida,
 * Entonces el sistema añadirá su comentario a la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 
  Un usuario quiere crear un comnetario de un club Y
 * Dado el usuario a utilizado el bot de Telegram para crear un comentario del club Y
 * Entonces el sistema le validara la información de su comentario
 * Si la información es válida,
 * Entonces el sistema añadirá su comentario a la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 
 Un usuario quiere eliminar un comentario 
 * Dado el usuario a utilizado el bot de Telegram para eliminar un comentario 
 * Entonces el sistema le validara la información de su comentario
 * Si la información es válida el sistema y el usuario es el autor del comentario, 
 * Entonces se eliminara su comentario de la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario
 * Si el usuario no es el autor del club,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	
 
   Un usuario quiere actualizar un comentario	
 * Dado el usuario a utilizado el bot de Telegram para actualizar un comentario 
 * Entonces el sistema le validara la información de su comentario y validara la identidad del usuario
 * Si la información es válida y el usuario es el autor o adminsitrador,
 * Entonces el sistema actualizara su comentario en la base de datos y el usuario recibirá una confirmación
 * Si la información no es válida,
 * Entonces el sistema notificara al usuario del problema encontrado
 * Si el usuario no es el autor del comentario o administrador,
 * Entonces el sistema le mostrara un mensaje de permiso restringido	

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

