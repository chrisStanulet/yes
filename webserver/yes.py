from flask import Flask

import inputParsing.equationParse as rpn

app = Flask(__name__)


@app.route("/")
def main():
    return rpn.rpnToString(rpn.shuntingYardAlgorithm('( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2.4 + ( 1 + 1 ) )'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", potrt=80)
