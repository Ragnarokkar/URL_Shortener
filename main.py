import random
import re
import string
from flask import Flask, abort, jsonify, redirect, request, render_template
from flask_cors import CORS, cross_origin
import validators
from validators import ValidationFailure
app = Flask(__name__)
CORS(app) #Added Cross Origin

#Validate url
def url_valid(url):
    return validators.url(url)
"""
    prepared_request = PreparedRequest()
    prepared_request.prepare_url(url, None)
    return prepared_request.url    
"""
    
#Placeholder URL Shorterner logic
def shorten(url):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))

#Function for bad API Calls    
def bad_request(message):

    response = jsonify({'message': message})
    response.status_code = 400
    return response

#Method for POST API Call    
@app.route('/shorten', methods=['POST'])
def shorten_url():
   
    if not request.json:
        return bad_request('Url not in json format.')
    
    if 'url' not in request.json:
        return bad_request('Url not found.')
    
    url = request.json['url']

    if not url_valid(url):
        return bad_request('Url is not valid.')

    shortened_url = shorten(url)
    shortened[shortened_url] = url

    return jsonify({'shortened_url': shortened_url}), 201

#Method to use GET API Call
@app.route('/shorten', methods=['GET'])
def shorten_url_get():
    return bad_request('Must use POST.')    

#Logic to redirect to the shortened url    
@app.route('/<alias>', methods=['GET'])
def get_shortened(alias):
    url = shortened[alias]
    
    return redirect(url, code=302)

#Varible to save url and shortened name as key-value pair        
shortened = {}

if __name__ == '__main__':
    app.run(debug=True)