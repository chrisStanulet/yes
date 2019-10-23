from flask import Flask
from flask import request

import inputParsing.equationParse as rpn

app = Flask(__name__)


@app.route("/")
def main():
    return rpn.rpnToString(rpn.shuntingYardAlgorithm('( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2.4 + ( 1 + 1 ) )'))


@app.route("/api/infixNotation")
def infix():
    if 'q' not in request.args:
        return "you absolute fool... enter a query with the parameter 'q'!"
    return rpn.rpnToString(rpn.shuntingYardAlgorithm(request.args['q']))




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
