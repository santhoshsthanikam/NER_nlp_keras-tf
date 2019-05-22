import predict_san
from datetime import datetime
"""
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world"
if __name__ == "__main__":
	app.run()
	predict_san.model_predict('Java is a language')
"""
for i in range(10):
	start=datetime.now()
	print(predict_san.model_predict("python"))
	end=datetime.now()
	print(start-end)
