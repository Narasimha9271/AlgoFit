import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

class AlgorithmSelector:
    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.vectorizer = CountVectorizer()
        self.q_table = np.zeros((len(algorithms), len(algorithms))) 
        self.alpha = 0.1 
        self.gamma = 0.99  # Discount factor
        self.exploration_rate = 0.5  # Initial exploration rate

    def select_algorithm(self, dataset, target_variable):
        X_text = dataset[target_variable] 
        X = self.vectorizer.fit_transform(X_text)  
        
        y = dataset[target_variable]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        # Explore with probability based on exploration rate
        if np.random.uniform(0, 1) < self.exploration_rate:
            selected_algorithm_idx = np.random.choice(len(self.algorithms))
        else:
            selected_algorithm_idx = np.argmax(np.mean(self.q_table, axis=1))
        
        selected_algorithm = self.algorithms[selected_algorithm_idx]
        
        
        selected_algorithm.fit(X_train, y_train)
        
        
        y_pred = selected_algorithm.predict(X_test)
        
        # Calculate the reward based on the accuracy of the predictions
        reward = accuracy_score(y_test, y_pred)
        
        # Update the Q-table
        self.update_q_table(selected_algorithm_idx, reward)
        
        
        self.exploration_rate *= 0.99  # Decrease exploration rate over time
        
        return selected_algorithm

    def update_q_table(self, algorithm_idx, reward):
        # Update the Q-table based on the reward received
        max_future_q = np.max(self.q_table[algorithm_idx])
        self.q_table[algorithm_idx] = (1 - self.alpha) * self.q_table[algorithm_idx] + self.alpha * (reward + self.gamma * max_future_q)
