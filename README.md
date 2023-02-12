## Contents

- [1. Description](#1-description)
- [2. Prerequisites](#2-prerequisites)
- [3. File tree](#3-file-tree)
- [4. Installing and running](#5-installing-and-running)

# 1. Description

Project with and endpoint that simulates a login, includes a CLI to test the endpoint.

# 2. Prerequisites

Building the python service requires the following tools:

- [x] [Python](https://www.python.org/downloads/)
- [x] [GIT](https://git-scm.com/)
- [x] Clone this project from its repository using `git clone`:
  - Clone with **HTTPS**
    ```
    https://github.com/Darkon55/prueba_tecnica_python.git
    ```

# 3. File tree

The project has the following organization:

```
.
├── options
│   ├── commands.py
│   ├── models.py
│   └── services.py
├── src
│   ├── database
│   ├── models
│   ├── routes
│   ├── app.py
│   └── config.py
├── .gitignore
├── apiTest.py
├── README.md
├── docker-compose.yaml
├── requirements.txt
└── setup.py
```

# 4. Installing and running

1. Create your virtual environment and run it

```
$ python -m virtualenv [name]
$ source [name]/bin/activate
```

2. Intall packages

```
$ python -m pip install -r requirements.txt
```

3. Install the CLI app
   ```
   $ pip install --editable .
   ```

4. In case wanna try docker follow the next steps:
    1. run this command:
        ```
        $ docker-compose up
        ```
    2. get id of the services:
        ```
        $ docker ps
        ```
    3. get ip address:
        ```
        $ docker inspect [id]
        ```
    4. connect to pgadmin:

    5. bind the database with pgadmin.

5. Create .env file with the next parameters:
   ```
    SECRET_KEY="your secret key" - optional
    PGSQL_HOST="your local host"
    PGSQL_USER="your user"
    PGSQL_PASSWORD="your password"
    PGSQL_DATABASE="your database name"
   ```
6. Run the project:

   - Run endpoint service
     ```
     $ python src/app.py
     ```
   - Run CLI app:

     ```
     $ apiTest --help
     ```
