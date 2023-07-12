from Flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_word():
    return 'Pratik DATA SCIENCETIES ,like share'