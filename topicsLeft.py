# generators in py


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$ comands $$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# generate docs of libraries
# pydoc3 -w <lib name>
# ex:-
# pydoc3 -w math
# open math.html
# generates .html file .. with docs of that module .. to be opened in browser


# pipenv to activate the current venv
# pipenv shell
# exit ... to exit the current venv

# install new packages
# pipenv install  .... same as ... npm install
# pipenv install request .... same as .... npm install request


# check global packages installed
# pip3 list


# creating local venv
# python3 -m venv FolderName/env
# source env/bin/activate  .... to activate the current venv ..created with above line
# deactivate ... to exit the current venv
# to inatall the package in current venv
# pip3 install request==2.9.*



# django 
# django-admin startproject mysite .
# python3 manage.py runserver
# python3 manage.py startapp polls
# django-admin startapp mysite
# python3 manage.py migrate
# python3 manage.py makemigrations
