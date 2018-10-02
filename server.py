from flask import (
    Flask,
    render_template,
    json,
    request
)
import requests

# Create the application instance
app = Flask(__name__, template_folder="templates")



# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/nfc/<nfcid>')
def api_article(nfcid):
    return 'You are reading ' + nfcid
    

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    print(content["device"])
    
    return 'JSON posted'


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)