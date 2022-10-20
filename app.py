from waybackmachine import waybackurl
from flask import Flask,request,jsonify

# http://10.8.1.104:2020/?input=rel8ed.to&year=2021

app=Flask(__name__)

@app.route('/')


def index():



 


    data=request.args
    url=data.get('input')
    year=data.get('year')



    # raise Exception('page error')

    data=waybackurl(url,year)
    
    return jsonify(data)
    # return df.to_html()
    # return resp

app.run(host='0.0.0.0',port='2020')


