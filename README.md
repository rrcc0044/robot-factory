# Robot Factory Simulator

### Installation
The Project requires [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) to run.

```bash
$ git clone https://github.com/rrcc0044/robot-factory.git
$ cd robot-factory
$ docker-compose build
$ docker-compose up
```
##### Docs are available at http://localhost:8001 after running the container


### Running Tests
```bash
$ docker exec <container_name> python3 manage.py test
```

### Design Decisions
- I used Django and Django Rest Framework to build the service. Im more comfortable in using Django & DRF as it provides me with everything I need and is very well documented.
- I used PostgreSQL DB for the database and stored the `configuration` inside a `JSONField` to keep things simple and to be able to store additional configuration for a robot if it'll be supported in the future.
- I used docker to replicate the same dev environment using containers and to have the ability to deploy the app easily.
