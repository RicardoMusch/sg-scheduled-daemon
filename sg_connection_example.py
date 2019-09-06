import os


"Replace the URL, script name (if needed) and xyxyxyxyxyx code for your script details."
"Then rename this file to sg_connection.py and save"



SERVER_PATH = "https://example.shotgunstudio.com"
os.environ["SERVER_PATH"] = SERVER_PATH

SCRIPT_NAME = 'sg_scheduled_deamon'
os.environ["SCRIPT_NAME"] = SCRIPT_NAME

SCRIPT_KEY = 'xyxyxyxyxyxyxyxyxyxyxyxy'
os.environ["SCRIPT_KEY"] = SCRIPT_KEY