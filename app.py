#Setting Environment Variable First
#export LC_ALL=en_US.utf-8
#export LANG=en_US.utf-8


from flask import Flask ,request ,render_template
import subprocess


BinaryFile ='/Users/lihan/Downloads/CppBinaryCalling/CppBinary/TextRepeated'

app = Flask(__name__)

@app.route('/')
def hello():
        return render_template('Call.html')


@app.route('/CppBinaryCall',methods =['POST','GET'])
def CppBinaryCall():
    if request.method == 'POST':
     print(request.headers)
     Times = request.form.get('Times')
     print(Times)
     CallingText = request.form.get('CallingText')
     print(CallingText)
     args = [BinaryFile,Times,CallingText]
     result = subprocess.check_output(args)
     print("result=",result.decode('utf-8'))
     result = (result.decode('utf-8').replace("\n"," "))

     return render_template("Result.html",result = result)

if __name__ == '__main__':
    app.run()(port = 5000,debug=True)

