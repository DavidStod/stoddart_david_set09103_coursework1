from flask import Flask, render_template, url_for
app = Flask(__name__)

#open the home page
@app.route('/')
def root():
    return render_template('home1.html'), 200

#open everyother page by reading it from the url
@app.route('/<name>/', methods=['GET', 'POST'])
def guitar(name=None):
    return render_template('{0}.html'.format(name), name=name), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
