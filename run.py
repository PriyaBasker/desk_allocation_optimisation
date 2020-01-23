import os
import src
from src.views import app
from src.config import config_params as cf 

app.secret_key = os.urandom(24)
app.run(host=cf.HOST,port=cf.PORT,debug=True)
