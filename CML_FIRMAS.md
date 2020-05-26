**Solicitar libro**
Petición de un usuario para solicitar un libro cargado en la página 


POST **/Book_request**{
        "user_id": 1234,
        "book_id": 9998,
        "owner_id": 1111,
        "date_from": "23-09-2020",
        "date_to": "15-10-2020"
}


**Listar libro pendiente por usuario y por estado**
Esto devolverá todos los libros que un owner específico tiene con su estado 


SEARCH **/book?status&owner**
{[book]}


**Aceptar solicitud**
El owner acepta una de todas las solicitudes pendientes, eligiendo las fechas en las que va a realizar el préstamo 


PUT **/request_accept**

## POST /qualifier 
{
	"veracity_evaluation": "1",
	"communication_evaluation": 1,
	"cleaning_evaluation": 1,
	"delivery_evaluation": 3,
	"puntuality_evaluation": 2,
	"agreement": 2,
	"description": "llalalala",
	"qualifying_user": 1,
	"book": 1
}
curl -X POST  -H "Content-Type: application/json" http://127.0.0.1:8000/qualifier/  -d '{"veracity_evaluation":"1","communication_evaluation":1,"cleaning_evaluation":1,"delivery_evaluation":3,"puntuality_evaluation":2,"agreement":2,"description":"llalalala","qualifying_user":1,"book":1}'