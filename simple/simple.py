from flask import Flask,jsonify
from flask_cors import CORS


app = Flask(__name__,static_folder="dist", static_url_path="")
CORS(app)



@app.route('/')
def index():
   goods = ["one","two","three"]

   return (jsonify(goods))


@app.route('/goods')
def goods():
   goods = []
   good1 = {"name":"one", "price":100, "weight":10}
   good2 = {"name":"two", "price":10, "weight":1}
   goods.append(good1)
   goods.append(good2)
   
   return (jsonify(goods))


if __name__ == '__main__':
    app.run(debug=True)