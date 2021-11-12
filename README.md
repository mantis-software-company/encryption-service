
# encryption-service
Basic Rest API microservice that encrypt/decrypt text using AES

This project written with [Flask web framework](https://flask.palletsprojects.com/en/2.0.x/). It use [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/index.html) for REST API and [Pyctuator](https://github.com/SolarEdgeTech/pyctuator) for actuator endpoint. 


## Deployment
You can deploy this service using docker:

```
docker-compose build
```

> :warning: **Change `__SERVICE_AES_KEY` and `__SERVICE_AES_IV` environments before build & deploy your image **
 

If you want to test service:

```
docker-compose run
```
