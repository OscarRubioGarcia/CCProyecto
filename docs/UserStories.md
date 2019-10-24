# Historias del Usuario
Un usuario quiere conseguir la lista de noticias del campus X
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de noticias del campus X
 * Entonces el sistema le mostrara la lista de noticias disponibles
 * Si el campus X no existe,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe el campus X

Un usuario quiere conseguir la lista de clubs del campus X
 * Dado el usuario a utilizado el bot de Telegram para pedir la lista de clubs del campus X
 * Entonces el sistema le mostrara la lista de clubs disponibles
 * Si el campus X no existe,
 * Entonces el sistema le mostrara un mensaje notificándole de que no existe el campus X

Un usuario quiere crear un club en el campus X	
 * Dado el usuario a utilizado el bot de Telegram para crear un club en el campus X
 * Entonces el sistema le validara la información de su club
 * Si la información es valida el sistema añadira su club a la base de datos y el usuario recibirá una confirmacion
 * Si la información no es valida el sistema notificara al usuario

Un usuario quiere saber si alguna persona estaría interesada en Y
 * El usuario a utilizado el bot de Telegram para buscar los estudiantes libres que tengan intereses Y
 * Entonces el sistema le muestra todos los estudiantes libres con intereses parecidos al club Y
 * Si no hay estudiantes interesados en Y,
 * Entonces el sistema le mostrara un mensaje de que no existen interesados

Un usuario quiere conocer los clubs más novedosos en el campus X
 * El usuario a utilizado el bot de Telegram para conocer las novedades de los clubs en el campus X
 * Entonces el sistema le muestra todas las novedades de clubs en el campus X
 * Si no hay novedades,
 * Entonces el sistema le mostrara un mensaje de que no hay novedades
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X

Un usuario quiere conocer todas las novedades acerca de noticias, clubs y estudiantes libres en el campus X
 * El usuario a utilizado el bot de Telegram para conocer las novedades en el campus X
 * Entonces el sistema le muestra todas las novedades del campus X
 * Si no hay novedades,
 * Entonces el sistema le mostrara un mensaje de que no hay novedades
 * Si no existe el campus X,
 * Entonces el sistema le mostrara un mensaje de que no existe el campus X
