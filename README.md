### Hexlet tests and linter status:
[![Actions Status](https://github.com/minoko86/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/minoko86/python-project-52/actions)
[![Python CI](https://github.com/minoko86/python-project-52/actions/workflows/pyci_1.yml/badge.svg)](https://github.com/minoko86/python-project-52/actions/workflows/pyci_1.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/015fd2c186d111fa7f10/maintainability)](https://codeclimate.com/github/minoko86/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/015fd2c186d111fa7f10/test_coverage)](https://codeclimate.com/github/minoko86/python-project-52/test_coverage)

# Task Manager

Task Manager – system for managing tasks. It allows you to create tasks, assign executers, labels, statuses and change them. To work with the system login and authentication are required.

### Installation
```
git clone https://github.com/minoko86/python-project-52
cd python-project-52
make install
make setup 
cp .env_example .env
```
## environments
- SECRET_KEY= (Secret key Django)
- DEBUG=true 
- EXTERNAL_HOSTNAME= (if you use an external host)
- DB_ENGINE=SQLite (To use simple sqlite database use this record)
- DATABASE_URL= (if you use an external DATABASE)
- ROLLBAR_TOKEN= (Rollbar key)

## Features

- Login and authentication
- Create, Read, Update, Delete operations for tasks, users, labels and statuses.
- Filter for tasks
- Unit tests

## Usage

1. Click "Registration" and create user
2. Click "Login" and login with your created user data
3. You can view users list on users page
4. You can create statuses, labels and tasks on their pages. Open them with navigation bar
5. Filter tasks with special form on top of the tasks page

## Technologies Used

- Python
- Django
- HTML/CSS
- SQL

## Contributions

Contributions to the Task Manager project are always welcome! If you encounter any issues or have suggestions for enhancements, please submit an issue or pull request. 

### Start project

- local start
 
 `make dev`

Use this app in browser on http://localhost:8000

- start in production

 `make serv`
