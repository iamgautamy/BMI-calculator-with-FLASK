from flask import Flask, render_template , request

BMI = Flask(__name__)


 
@BMI.route('/', methods=['GET','POST'])
def cal():
    bmi=''
    height=''
    weight=''
    if request.method == 'POST' and 'heightt' in request.form:
        height = float(request.form.get('heightt'))
        weight = float(request.form.get('weightt'))
        bmi = calc_bmi(weight, height)
    return render_template("index.html",
                            height=height,
                            weight=weight,
                            bmi=bmi)
    
def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)    
    
BMI.run()   