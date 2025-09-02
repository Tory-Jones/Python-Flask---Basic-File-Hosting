from flask import Flask, render_template, redirect, send_file, url_for
from flask_autoindex import AutoIndex

app = Flask('Servicing', template_folder='.')

ppath = "./FolderForHosting/"
AutoIndex(app, browse_root=ppath)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
