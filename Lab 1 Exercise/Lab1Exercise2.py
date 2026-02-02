# ADD
@app.route("/add/<int:a>/<int:b>")
def add (a, b):
    return  jsonify(result=a + b)

# SUBTRACT 
@app.route("/subtract/<int:a>/<int:b>")
def subtrat(a, b):
    return jsonify(result=a - b)

# MULTIPLY
@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify(result=a * b)

# DIVIDE
@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return jsonify(error="Division by zero noy allowed"), 400
    return jsonify(result=a /b)