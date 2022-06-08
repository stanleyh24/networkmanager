# NETWORK MANAGER BACKEND

## ROUTES TO IMPLEMENT

### AUTHENTICATION ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/refresh/``` | _Refresh user token_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|

### CLIENT ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/client/``` | _Get all clients_|_Logged users_|
| *POST* | ```/client/new``` | _Create a client_|_Logged users_|
| *PUT* | ```/client/update/{client_id}/``` | _Update an client_|_Logged users_|
| *DELETE* | ```/client/delete/{client_id}/``` | _Delete client_|_Logged users_|


### ROUTER ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/router/``` | _Get all routers_|_Logged users_|
| *POST* | ```/router/new``` | _Create a router_|_Logged users_|
| *PUT* | ```/router/update/{router_id}/``` | _Update an router_|_Logged users_|
| *DELETE* | ```/router/delete/{router_id}/``` | _Delete router_|_Logged users_|

### SERVICE ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/service/``` | _Get all services_|_Logged users_|
| *POST* | ```/service/new``` | _Create a service_|_Logged users_|
| *PUT* | ```/service/update/{service_id}/``` | _Update an service_|_Logged users_|
| *DELETE* | ```/service/delete/{service_id}/``` | _Delete service_|_Logged users_|


### SERVICE ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/service/``` | _Get all services_|_Logged users_|
| *POST* | ```/service/new``` | _Create a service_|_Logged users_|
| *PUT* | ```/service/update/{service_id}/``` | _Update an service_|_Logged users_|
| *DELETE* | ```/service/delete/{service_id}/``` | _Delete service_|_Logged users_|

### INVOICE ROUTES
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/invoice/``` | _Get all invoice_|_Logged users_| 
| *GET* | ```/invoice/{invoice_id}``` | _Get a invoice_|_Logged users_|
| *PUT* | ```/invoice/update/{invoice_id}/``` | _Update aninvoice_|_Logged users_|

