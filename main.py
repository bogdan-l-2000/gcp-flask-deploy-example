from flask import Flask


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World!"

@app.route('/echo/<name>')
def echo(name):
    val = {"new-name": name}
    return jsonify(val)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)