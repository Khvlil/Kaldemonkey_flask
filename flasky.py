from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def category():
    return render_template('interface.html')

@app.route('/mercedes')
def home():
    return render_template('mercy.html')


@app.route('/map')
def map():
	return render_template('map.html')


@app.route('/tkinter')
def tkinter():
    return render_template('')

if __name__ == "__main__":
    website_url = 'mercyplotib.com:5000'
    app.config['SERVER_NAME'] = website_url
    app.run()