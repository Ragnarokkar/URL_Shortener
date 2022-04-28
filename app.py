import random
import re
import string
from flask import Flask, jsonify, redirect, request
from flask_cors import CORS, cross_origin
import validators
from validators import ValidationFailure
app = Flask(__name__)
CORS(app) #Added Cross Origin to handle errors

#Validate url
def url_valid(url):
    return validators.url(url)
    
#Search the file for urls aready written    
def search_file(url):
    fo= open("/app/data.txt","r")
    for line in fo:
        currentline = line.split(",")
        if currentline[0]== url:
            fo.close()
            return currentline[1]
    fo.close()        
    return None
    
#Search the file for urls aready written    
def search_file_short(url):
    fo= open("/app/data.txt","r")
    for line in fo:
        currentline = line.split(",")
        if currentline[1]== url:
            fo.close()
            return currentline[0]
    fo.close()        
    return None      
    
#URL Shorterner logic
def shorten(url):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))

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
    #Search if url is already in file
    if search_file(url) is not None:
        return jsonify({'shortened_url': search_file(url)}), 201
    shortened_url = shorten(url)
    #shortened[shortened_url] = url
    fo= open("/app/data.txt", "a")
    fo.writelines(url+","+shortened_url+",\n")
    fo.close()
    return jsonify({'shortened_url': shortened_url}), 201

#Method to use GET API Call
@app.route('/shorten', methods=['GET'])
def shorten_url_get():
    return bad_request('Must use POST.')    

#Logic to redirect to the shortened url    
@app.route('/<alias>', methods=['GET'])
def get_shortened(alias):
    if search_file_short(alias) is not None:
        return redirect(search_file_short(alias), code=302)
    
    return redirect(url, code=302)

#Varible to save url and shortened name as key-value pair        
shortened = {}

if __name__ == '__main__':
    app.run(debug=True)
