# Fastapi

API development using **FastAPI framework** and data extraction from **MySQL** local hosted database.

## General Steps

1. Extract Transform and Load (ETL)
2. Local Database creation in MySQL.
3. Create connection with Python libraries (SQLAlchemy, Pydantic)
4. Model & Schema development in SQLAlchemy
5. main file structuring


## About the dataset

The main dataset is a version of Kaggle [Formula 1 World Championship](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=status.csv) dataset containing the following tables:

* circuits
* driver
* races
* constructor
* laptimes
* pitstops
* qualifying
* results

Formula One is the highest class of international racing for open-wheel single-seater formula racing cars sanctioned by the Fédération Internationale de l'Automobile (FIA).
The dataset consists of all information on the Formula 1 from 1950 till the latest 2021 season.

## 1. Extract Transform and Load (ETL)

In this first process, data exploration was carried out, null data, repeated data and data that do not constitute the easily 
accessible data types were searched for. In general, the dataset was clean, the .jsons were exported as csv and meet the following load requirements: FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

## 2. Local Database creation in SQLite.

Once the datasets have been exported, the Database is created in SQLite for which [DB Browser](https://sqlitebrowser.org/) interface was used. There, primary keys and relationships among tables were made. 

## 3, 4, 5 -> Create connection with Python libraries (SQLAlchemy, Pydantic) | Model & Schema development in SQLAlchemy | main file structuring
For these procedural steps [FastAPI SQL Relational Database documentation](https://fastapi.tiangolo.com/tutorial/sql-databases/) was extremely helpful. This allowed to create
a file structure: 

* database.py: Here we create the link between SQL Database and Python libraries/frameworks.
* models.py: SQLAlchemy models are built so they can interact with the Database tables. Here, models is the way SQLAlchemy represents tables.
* schemas.py: Pydantic models (schemas in this project) is to perform data validation, conversion, and documentation classes and instances.
* crud.py: **C**reate, **R**ead, **U**pdate and **D**elete. In this file we create reusable functions that interact with Database. Although we only create functions for reading data, in the future it can be used for creating, updating and deleting data.
* main.py: Code integration. It contains the FastAPI instantiated class object -> app.


## + Information to highlight.
* [FastAPI Framework](https://fastapi.tiangolo.com/)
* [SQL Alchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
* [FastAPI first steps YouTube tutorial (Spanish)](https://www.youtube.com/watch?v=_eWEmRWhk9A&list=LL&index=5&t=3471s)
* [SQL Queries as Python code with SQLAlchemy](https://hackersandslackers.com/database-queries-sqlalchemy-orm/))

## Some API endpoints check for more in documentation
* **/docs** documentation
* **/year-races** year with most races
* **/best-driver** driver with the highest number of first position
* **/most-run** most drive circuit name
* **/best-score** driver with the highest points

[Heroku Deploy Link](https://fastapi-database-formula1-read.herokuapp.com/docs)

## Contact

Greetings,
Nicolás Jimenez: nico.96@live.com.ar 

LinkedIn: https://www.linkedin.com/in/nicolás-jimenez/
