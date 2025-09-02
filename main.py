from flask import Flask
from flask_autoindex import AutoIndex

app = Flask(__name__, template_folder='.')

ppath = "./FolderToHost/"
AutoIndex(app, browse_root=ppath)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
