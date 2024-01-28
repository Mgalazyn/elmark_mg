
# Description
I have created a efficient RESTful API for managing a Parts Warehouse. The API is developed using the Django Rest Framework (DRF) and is connected to a MongoDB database. The application is containerized using Docker for seamless deployment. 
At the begining I have created MongoDB connection with project by using djongo/pymongo, then models, serializers, urls, views then added data by api. Then made input validation and filters. After all containerized whole API with Docker. 
## Tech Stack

**Language:** Python

**Framework:** DRF (django-filters, cors, djongo/pymongo)

**Containerization:** Docker, docker-compose

**Server:** MongoDB

![data](https://github.com/Mgalazyn/elmark_mg/assets/91530764/367bf26e-fb41-4783-9a97-0de75c7811b2)


## Why Django REST Framework
Basicly it most common used framework for creating RESTful API, have most pythonic way to creating project (using external packages). APIs created with DRF are easy to scale, mostly understandable by other developers, create clear structure and organization.
## Getting Started

To get started with this project, you'll need to have python atleast Python<=3.6, Docker and your MongoDB credentials.

Once you have fulfilled all requirements then:

```bash
  git clone https://github.com/Mgalazyn/elmark_mg.git
```

Change into the project directory:

```bash
  cd elmark_mg
```

Create a file called .env and add the following environment variables:

Example .env
```bash
DB-NAME= your db name
DB-HOST= your db link from mongodb
DB-USERNAME= your user
DB-PASSWORD= your password 
SECRET-KEY=your secret django key
DEBUG= your debug boolean
```

after adding this you can start script into cmd or into terminal from interpreter by passing:

build you image
```bash
docker-compose build
```
create container and run
```bash
docker-compose up
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

