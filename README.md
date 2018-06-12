# pythonRestAPI
Simple RestAPI. desarrollado por Daniel Diaz Infante Romo utilizando Python/bottle framework

Caso de uso
1.- seleccionar todos los usuarios
http://127.0.0.1:8080/users

2.- seleccionar usuarios por nombre
http://127.0.0.1:8080/users/julio

3.- insertar enviando una peticion POST a http://127.0.0.1:8080/users con un JSON en el body de este tipo:
{
  "username":"ejemplo",
  "password":"12345"
}
