#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request,redirect
from flask import send_file, send_from_directory, safe_join, abort
from flask.helpers import url_for

from generate_report import *
import os


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
report = Report()

#db = SQLAlchemy(app)



# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

user_details = {}


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route("/user",methods=['GET','POST'])
def user():
    if(request.method == 'POST'):
        user_details= {
            "Name":request.form.get("name"),
            "Age":request.form.get("age"),
            "Height":request.form.get("height"),
            "Weight":request.form.get("weight"),
            "Gender":request.form.get("gender"),
            "Diagnosis":request.form.get("Diagnosis"),
            "Analysis":request.form.get("disease"),
            "Image":""
        }
        return render_template('pages/user.html')
    return render_template('pages/user.html')

@app.route('/uploads', methods=['GET', 'POST'])
def download():
    return send_from_directory(directory="./reports", filename="report.pdf")


@app.route("/analyze_img",methods=['POST'])
def analyze_img():

    if(request.method  == 'POST'):    
        if(request.files):
            img = request.files['image']
            img.save(os.path.join("./images",img.filename))
            user_details['Image'] = img.filename
            report.generate_report(user_details)
            # test_img = cv2.imread(os.path.join(app.config['IMAGE_UPLOADS'], img.filename))

    return redirect('user')


# @app.route('/about')
# def about():
#     return render_template('pages/placeholder.about.html')


# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)


# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)


# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)


# Error handlers.

# @app.errorhandler(500)
# def internal_error(error):
#     #db_session.rollback()
#     return render_template('errors/500.html'), 500


# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404

# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port -  PORT:3000:
if __name__ == '__main__':
    app.run()

