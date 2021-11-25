from flask import Flask, request, jsonify
app = Flask(__name__)


@app.post('/post_numbers')
def multiply_num():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    return jsonify({'result': num1 * num2})


if __name__ == '__main__':
    app.run(debug=True)

