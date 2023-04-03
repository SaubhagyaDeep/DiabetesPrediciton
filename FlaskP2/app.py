from flask import Flask, render_template, request
import pickle
app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method=="POST":
        FS=int(request.form['FS'])
        FU=int(request.form['FU'])
        with open('my_model','rb') as f:
            model=pickle.load(f)
        result=(model.predict([[FS,FU]]))

        if result[0]=="YES":
            return render_template('index.html', data=["Sorry but you might have diabetes :( ",'red']) 
        else:
            return render_template('index.html',data=["Yay, you don't have diabetes :)","green"])
    else:
        return render_template('index.html')

@app.route('/<name>')
def user(name):
    return '<h1> Hello, %s!</h1>' % name

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/', methods=['POST'])
# def submit():
#     if request.method=="POST":
#         FS=int(request.form['FS'])
#         FU=int(request.form['FU'])
#         with open('my_model','rb') as f:
#             model=pickle.load(f)
#         result=(model.predict([[FS,FU]]))

#         if result[0]=="YES":
#             return "Sorry but you might have diabetes :( "
#         else:
#             return "Yay, you don't have diabetes :)"
#     else:
#         return 'Something Went Wrong'

if __name__== '__main__':
    app.run(debug=True)