<h1 align="center">👋 Welcome to the ICMA Project</h1>
<h3 align="center">A passionate full-stack developer from Uzbekistan</h3>

---

## 🌐 Project Link

🔗 [Visit the live website](http://icma.uz/en/)

<a href="https://github.com/bobur22/ICMA_deploy.git">
   <img width="300px" height="100px" src="http://icma.uz/static/main/img/language_en.svg" />
</a>


---

## 🧠 Introduction

This is the official repository for the **ICMA Project**. It's a full-stack web application developed with Django and designed to help you understand and manage important data more efficiently.

---

## ⚙️ Getting Started

Follow the steps below to set up the project on your local machine.

## Before start clone the repository to your lap top.
    git clone git@github.com:bobur22/ICMA_deploy.git
## And then open your terminal and start creating by venv file
      python3 -m venv venv
## then activate venv file.
## And after that start with installing requirements.txt
    pip install -r requirements.txt

## When you finished installing required packages then you have to set some settings.
    ## 1. In the path ICMA_deploy/config_/ you can see file .env.example file that keeps website related data so fill it than you can move to the next step.
    
## then make a migrations.
    ./manage.py makemigrations

## and after that migrate it.
    ./manage.py migrate

## before runing server create super user in order to open admin panel.
    ./manage.py createsuperuser

## then finally start project.
    ./manage.py runserver

#Then you can open website on your local host.
## and project is ready.
