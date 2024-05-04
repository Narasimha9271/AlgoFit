from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from algorithm_selector import AlgorithmSelector
import pandas as pd

app = Flask(__name__)

# Initialize AlgorithmSelector
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

algorithms = [SVC(), DecisionTreeClassifier(), RandomForestClassifier(), KNeighborsClassifier()]
algorithm_selector = AlgorithmSelector(algorithms)

# Define route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

# Define route for file upload
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # Check if file has allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save the uploaded file
            file.save(filename)
            # Load dataset
            try:
                dataset = pd.read_csv(filename, dtype=str)  # Read all columns as strings initially
            except pd.errors.ParserError:
                return "Invalid file format. Please upload a valid CSV file."
            
            # Get the target variable name from the form
            target_variable = request.form.get('target_variable')
            
            # Check if the target variable exists in the dataset
            if target_variable not in dataset.columns:
                return f"Target variable '{target_variable}' not found in dataset"
            
            # Run the reinforcement learning algorithm to select the best algorithm
            selected_algorithm = algorithm_selector.select_algorithm(dataset, target_variable)
            # Render result template with selected algorithm
            return render_template('result.html', selected_algorithm=selected_algorithm)
        else:
            return "Invalid file extension or no file selected"


if __name__ == '__main__':
    app.run(debug=True)
