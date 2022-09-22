from flask import Flask,render_template,request
import pandas as pd
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def templete():
    return render_template('template.html')


@app.route('/getdata1',methods=['POST','GET'])
def getdata1():
    input=request.form['yfin']
    if input.strip()=='':
        return render_template('template.html',res="\n\nInvalid input\n\nThe Company Code entered is Empty")
    Stock=yf.Ticker(input.upper())
    Data=Stock.history(period="1d")
    if Data.empty:
        return render_template('template.html',res="\n\nInvalid input\n\nEntered Company Code: "+input.upper())
    Data=Data.drop(['Dividends','Stock Splits'],axis=1)
    Val=Data.values[:1].tolist()[0]
    st="\nCompany Code: "+input.upper()+"\n\n"
    for i,j in zip(Data.columns,Val):
        st+=str(i)+":"+str(j)+"\n"
    return render_template('template.html',res=st)

@app.route('/getdata2',methods=['POST','GET'])
def getdata2():
    input=request.form['csv']
    if input.strip()=='':
        return render_template('template.html',res="\n\nInvalid input\n\nThe Company Code entered is Empty")
    # Data = pd.read_csv('https://raw.githubusercontent.com/manthribharadwaj12/Kubernetes/main/data%20(1).csv')
    Data=pd.read_csv("./Data/data.csv")
    Data = Data.loc[Data['Name']==input.upper()].drop(['date','Name'],axis=1)
    if Data.empty:
        return render_template('template.html',res="\n\nInvalid input\n\nEntered Company Code: "+input.upper())
    Val=Data.values[:1].tolist()[0]
    st="\nCompany Code: "+input.upper()+"\n\n"
    for i,j in zip(Data.columns,Val):
        st+=str(i)+":"+str(j)+"\n"
    return render_template('template.html',res=st)

if __name__ == "__main__":
    app.run(debug=True)