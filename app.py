from flask import Flask,render_template,request

import pickle

loaded_model=pickle.load(open('rfc_model.pkl','rb'))

app=Flask(__name__)

@app.route('/',methods=['GET','POST']) #To render homepage
def home_page():
    return render_template('index.html')

def predictor(to_predict_list):
    return loaded_model.predict([to_predict_list])

@app.route('/results',methods=['POST']) #This will be called from UI
def result():
    if request.method=='POST':
        to_predict_list = request.form.to_dict()
        #print(to_predict_list,'  conntctn8ox  \n') #------DEBUG
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        #print(to_predict_list) #----DEBUG
        result=predictor(to_predict_list)
        if int(result)==0:
            prediction="Not going to default"
        else:prediction="You are going to default"
        return render_template('results.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)