https://flask.palletsprojects.com/en/3.0.x/quickstart/
https://flask.palletsprojects.com/en/3.0.x/installation/

## Created my virtual environment
python -m venv myenv
.\myenv\Scripts\Activate.ps1

## Created my repository and pushed to master
git init
git add .
git commit -m "Your commit message here"
git remote add origin https://github.com/DharaKara/my-IPMS-project.git
git push -u origin master

pip install flask
pip SQLAlchemy
pip install pyodbc

ctrl + C <-to exit>

shortcut:
flask -app main run

development mode:
flask --app app run --debug

take snapshot of packages
pip freeze > requirements.txt
pip install -r requirements.txt

databases
pip install pyodbc
pip install SQLAlchemy

mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>

pip install python-dotenv
from dotenv load dotenv

pip install Flask-WTF