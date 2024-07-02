from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/root', methods=['GET'])
def root():
    return jsonify({
        'statusCode': 'SC0000',
        "statusDescription": "Success",
        'message': 'Hello World'
        })



# New user Registeration
@app.route('/authAdapter', methods=['POST'])
def authAdapter():
    try:
        data = request.get_json()
        fullName = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        if(fullName and email and password and fullName != "" and email != "" and password != "" and fullName == "NA" and email == "NA" and password == "NA"):
            new  = 0
        else:
            return jsonify({
                "statusDesc": "Failure",
                    "statusCode": {
                        "code": "F005"
                        },
                "message": "Some mandatory fields are missing"
                     
            }),400
    except Exception as e:
        return jsonify({
            'error': str(e)
        }),500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)