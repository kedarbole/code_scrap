from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/',methods = ['POST'])
def home():
    data=request.get_json()
    name=data['name']
    age=data['age']
    randnum=data['randnum']
    return(jsonify({"output":int(age)+int(randnum)}))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)