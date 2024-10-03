from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
# need to reinstall flask whenever you run this - find out why
#$env:FLASK_APP = "server.py"
#$env:FLASK_DEBUG = '1'
#press INSERT if your SPACE replaces characters
#flask run - make sure you are in the correct directory
@app.route('/')
def my_home():
    return render_template('index.html')

#creating a dynamic route, pay attention to the syntax <>
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to Database '
    else:
        return 'something went wrong'


# @app.route('/about.html') creating a route to the html code, so we can display the page on the website
# def about():
#     return render_template('about.html')



