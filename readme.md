# Password generation - service (restful)

The ultimate goal of this application is to provide simple rest api and methods for password generation.

There is one endpoint:  
**GET**  

response_code: 200

```json:
{
    "message" : "use POST request to generate password",
    "data": null  
}
```

**POST**  
 
body:  
```json:
{
    "len" : int,
    "special": bool,
    "capital": bool,
    "numbers":bool 
}
```
response:  
response_code: 200 
```json:
{
    "password": <generated_string> 
}
```