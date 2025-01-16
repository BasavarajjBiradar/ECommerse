# ECommerse

ecommerse website using react.js for frontend and flask for backend
database MYSQL

steps clone
open
frontend/shopping --frontend
npm install ---installs ncecssary dependency from pachage-json file

npm start --- frontend starts running in browser locally

open backend
change this in admin.py
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:your_mysql-password@127.0.0.1/database_name'
this connect to ur local databse server and persorm query retrievel task usong flaks sqlalchemy and pymysql

create venv

pip install requirements.txt

activate venv

run--->
python admin.py
-- backend server runs and

u can check and enjoy the local ecommrse project
