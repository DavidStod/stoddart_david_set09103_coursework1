from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html'), 200

@app.route('/<name>/')
def guitar(name=None):
    return render_template('{0}.html'.format(name), name=name)

#@app.route('/strat/')
#def strat():
#    return render_template('guitarmastertemplate.html'), 200

#@app.route('/les-paul/')
#def lespaul():
#    return render_template('lespaul.html'), 200

#@app.route('/fly-v/')
#def flyv():
#    return render_template('flyv.html'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
