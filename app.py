from flask import Flask,render_template,request

import pickle

loaded_scalar=pickle.load(open('scalar_ccd4.pkl','rb'))
loaded_model=pickle.load(open('ccard_model4.pkl','rb'))

app=Flask(__name__)

@app.route('/',methods=['GET','POST']) #To render homepage
def home_page():
    return render_template('index.html')
def preprocessing(to_predict_list=[]):
    to_predict_list=to_predict_list+10*[0]
    if to_predict_list[2]!=1:
        to_predict_list[22+to_predict_list[2]]=1
    if to_predict_list[3]!=0:
        to_predict_list[28+to_predict_list[3]]
    if to_predict_list[1]!=0:
        to_predict_list[-1]=1
    to_predict_list.pop(3)
    to_predict_list.pop(2)
    to_predict_list.pop(1)
    print('preprocessed data: ',to_predict_list) #----DEBUG
    return loaded_scalar.transform( [to_predict_list])
def predictor(to_predict_list):
    preprocessed=preprocessing(to_predict_list)
    return loaded_model.predict(preprocessed)

@app.route('/results',methods=['POST']) #This will be called from UI
def result():
    if request.method=='POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list,'  conntctn8ox  \n') #------DEBUG
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list) #----DEBUG
        result=predictor(to_predict_list)
        if int(result)==0:
            prediction="Not going to default"
        else:prediction="You are going to default"
        return render_template('results.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)