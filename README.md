
# encryption-service
Basic Rest API microservice that encrypt/decrypt text using AES

This project written with [Flask web framework](https://flask.palletsprojects.com/en/2.0.x/). It use [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/index.html) for REST API and [Pyctuator](https://github.com/SolarEdgeTech/pyctuator) for actuator endpoint. 


## Running

Pre-built images are here:
https://hub.docker.com/r/mantissoftware/encryption-service


To run pre-built image, run

```
docker run -p 5000:5000 -e __SERVICE_AES_KEY=<base64_aes_key> -e __SERVICE_AES_IV=<base64_aes_iv>  mantissoftware/encryption-service
```

and go http://localhost:5000/swagger-ui to access Swagger-UI


## Building your own image

Run `docker-compose build` to build your own image. 

> ⚠️ You have to change __SERVICE_AES_KEY  and  __SERVICE_AES_IV environment variables before build & deploy your own image
 
To test your image, run  `docker-compose run` and go http://localhost/swagger-ui to access swagger-ui

## Deployment 

> ⚠️ Don't forget to set __SERVICE_ACTUATOR_BASE_URI environment variable (Value: http(s)://<deployment_url>/<actuator_path>)
