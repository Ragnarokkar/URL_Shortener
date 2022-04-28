import random
import re
import string
from flask import Flask, abort, jsonify, redirect, request, render_template
app = Flask(__name__)

#Validate url
def url_valid(url):
    if url[:4] != 'http':
        url = 'http://' + url
    return re.match(regex, url) is not None

#Placeholder URL Shorterner logic
def shorten(url):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 10))

#Add a html page for testing
@app.route('/')
def my_form():
    return render_template('my-form.html')
#Get url from my-form.html for testing
@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['text']
    
    if not url_valid(url):
        return "Provided url is not valid."
    shortened_url = shorten(url)
    shortened[shortened_url] = url
    return shortened_url

#Regular expression to validate url
regex = re.compile(
        r'^(?:http)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#Varible to save url and shortened name as key-value pair        
shortened = {}

if __name__ == '__main__':
    app.run(debug=True)