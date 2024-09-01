# Algorithm Selector

Algorithm Selector is a web application that uses Reinforcement Learning to select the best machine learning algorithm for a given dataset. The project leverages Deep Q Networks and Q Learning to evaluate and choose among several algorithms: Support Vector Machine (SVM), Decision Tree, k-Nearest Neighbors (kNN), and Random Forest. The web interface is built using Flask, allowing users to upload datasets and receive recommendations on the best algorithm to use.

## Demo Video

[![YouTube Video](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFHTHi03M5zp97w77w0wuwF_FTfo-UrqvRGw&s)](https://www.youtube.com/watch?v=ocui8DKx4xM)

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [How to Run](#how-to-run)
5. [Usage](#usage)
6. [Advantages](#advantages)

## Features

- **Algorithm Selection:** Utilizes Deep Q Networks and Q Learning to determine the most suitable machine learning algorithm for your dataset.
- **Multiple Algorithms Supported:** Compares SVM, Decision Tree, kNN, and Random Forest.
- **User-friendly Web Interface:** Easy-to-use interface for uploading datasets and receiving algorithm recommendations.
- **Automatic Learning:** The system improves its recommendations over time through reinforcement learning.

## Technologies Used

- **Flask:** Web framework used for creating the web interface.
- **Scikit-Learn:** Machine learning library for implementing the algorithms.
- **Pandas:** Data manipulation and analysis library for handling datasets.
- **NumPy:** Library for numerical computations.
- **Reinforcement Learning:** Deep Q Networks and Q Learning for algorithm selection.

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/algorithm-selector.git
   cd algorithm-selector
   ```
   
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
    ```
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
    ```

### How to Run
1. **Start the Flask application:**
   ```bash
   python app.py
   ```
2. pen your web browser and navigate to:
   ```bash
   http://127.0.0.1:5000
   ```

### Usage
1. **Upload a CSV file:**
   - Ensure your CSV file has a proper format and the target variable column.
   - The target variable is the column you want the algorithms to predict.

2. **Select the target variable:**
   - Enter the name of the target variable in the provided form.

3. **Get the recommendation:**
   - The application will process the dataset and recommend the best algorithm based on its learning.

### Advantages
1. **Automated Selection:** Saves time by automatically determining the best algorithm for your dataset.
2. **Improves Over Time:** The reinforcement learning model improves its accuracy with more data and usage.
3. **User-Friendly:** Simple and intuitive web interface for ease of use.
4. **Versatile:** Supports multiple machine learning algorithms, making it suitable for various types of datasets.
