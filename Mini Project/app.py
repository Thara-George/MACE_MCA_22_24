import os
import pandas as pd
from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import redirect,url_for

app = Flask(__name__)

# Define the upload folder where CSV files will be saved
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load the dataset and train the Random Forest model
data = pd.read_csv("C:\ml\Heart_disease_cleveland_new.csv")
X = data.drop('target', axis=1)
Y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
random_forest = RandomForestClassifier(n_estimators=104, random_state=50)
random_forest.fit(X_train, y_train)
# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Route for the main page
@app.route('/index')
def index():
    return render_template('index.html')

# Route to handle the CSV file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        return "File uploaded successfully"

# Route to handle the prediction
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        # Get input data from the form
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        # Create an input data array
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
         #if(age<100 and age>=1 and )
        # Make predictions using the trained model
        prediction = random_forest.predict(input_data)[0]
        if prediction==0:
            prediction="No Heart Disease"
        else:
            prediction="Heart Disease Detected"

        #return f"Predicted Outcome: {prediction}"
        return render_template('predict.html', prediction=prediction)
    # If it's a GET request, you can redirect to the form page or handle it accordingly
    return render_template('index.html')  # You can customize this part based on your requirements
# Route for the features page
@app.route('/features')
def features():
    # You can render the features.html template or handle it based on your requirements
    return redirect(url_for('features_page'))

# Route to render the features.html template
@app.route('/features_page')
def features_page():
    return render_template('features.html')
if __name__ == '__main__':
    app.run(debug=True)
