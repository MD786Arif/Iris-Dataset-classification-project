from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
# Load the model
model = pickle.load(open('saved_model.pkl','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods = ['POST','GET'])
def predict():
    # flowe description
    descriptions = {
           "setosa": "Iris setosa is a species of iris known for its vibrant colors and distinctive appearance. It has a short stature with bright flowers.",
            "versicolor": "Iris versicolor, also known as the blue flag iris, features a range of blue to violet petals and is commonly found in wetland areas.",
            "virginica": "Iris virginica, or the Virginia iris, is characterized by its larger size and deep purple flowers. It thrives in moist habitats.",
                 }
    
     # Get form data using request object
    sepal_length = float(request.form['sepalLength'])
    sepal_width = float(request.form['sepalWidth'])
    petal_length = float(request.form['petalLength'])
    petal_width = float(request.form['petalWidth'])
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    img1 = "/flowers/"+result[0]+".jpg"
    # print(result[0])
    
    return render_template('index.html',**locals())
    


if __name__ =='__main__':
    app.run(debug=True)