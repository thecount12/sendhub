from flask import Flask, request, jsonify, abort, make_response
from jsonschema import validate, ValidationError

app = Flask(__name__)

schema = {
    "title": "Platform Developer Programming Challenge",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "recipients": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "pattern": "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"},
        }
    },
    "required": ["message", "recipients"]
}

table = {
    'small': {'catname': 'Small', 'subnets': '10.0.1.', 'through': 1, 'cost': 0.01},
    'medium': {'catname': 'Medium', 'subnets': '10.0.2.', 'through': 5, 'cost': 0.05},
    'large': {'catname': 'Large', 'subnets': '10.0.3.', 'through': 10, 'cost': 0.1},
    'super': {'catname': 'Super', 'subnets': '10.0.4.', 'through': 25, 'cost': 0.25},
}

categories = ['super', 'large', 'medium', 'small']
through_dict = {25: 0, 10: 1, 5: 2, 1: 3}
MAXCON = 5000 # up to 5000 recipients

@app.route('/')
def hello():
    return 'Platform Developer Programming Challenge!'
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)
@app.route('/greed', methods=['POST'])
def greed():
    '''
    greedy is good 
    '''
    data = request.json
    try:
        validate(data, schema)
    except ValidationError:
        abort(400)

    recipients = data['recipients']
    recipients_num = len(recipients)

    # calculate the routes
    routes = []
    start = 0
    for i in range(len(categories)):
        requests_needed = recipients_num / table[categories[i]]['through']
        if requests_needed > 0:
            for j in range(1, requests_needed + 1):
                ip = table[categories[i]]['subnets'] + str(j)
                end = start + table[categories[i]]['through']
                routes.append({'ip': ip, 'recipients': recipients[start : end]})
                start = end
        recipients_num = recipients_num % table[categories[i]]['through']
    return jsonify({'message': 'SendHub Rocks', 'routes': routes})

@app.route('/dynamic', methods=['POST'])
def dynamic():
    '''
    dynamic 
    '''
    data = request.json
    try:
        validate(data, schema)
    except ValidationError:
        abort(400)

    recipients = data['recipients']
    recipients_num = len(recipients)
    categories_used = [0] * (recipients_num + 1)
    categories_track = [0] * (recipients_num + 1)
    for i in range(1, recipients_num + 1):
        min_category = MAXCON
        last_in = 0
        for j in range(len(categories)):
            if table[categories[j]]['through'] <= i:
                t = categories_used[i - table[categories[j]]['through']] + 1
                if t < min_category:
                    min_category = t
                    last_in = j
        categories_used[i] = min_category
        categories_track[i] = table[categories[last_in]]['through']

    categories_in_used = [0] * len(categories)
    routes = []
    start = 0

    # backrack the categories in use
    i = recipients_num
    while i > 0:
        index = through_dict[categories_track[i]]
        categories_in_used[index] = categories_in_used[index] + 1
        i = i - categories_track[i]

    # calculate the routes
    routes = []
    start = 0
    for i in range(len(categories)):
        requests_needed = categories_in_used[i]
        if requests_needed > 0:
            for j in range(1, requests_needed + 1):
                ip = table[categories[i]]['subnets'] + str(j)
                end = start + table[categories[i]]['through']
                routes.append({'ip': ip, 'recipients': recipients[start : end]})
                start = end
    return jsonify({'message': 'SendHub Rocks', 'routes': routes})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
    #pass
