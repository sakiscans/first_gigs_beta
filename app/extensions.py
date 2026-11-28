# database//loginmanagement//etc..

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect 

db = SQLAlchemy()  #flask -> databse via sql
migrate = Migrate() #comand to track database shifts
login_manager = LoginManager() # remember who logged in. 
csrf = CSRFProtect() #check for valid token for login/reg.