import unittest
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class TestEmailClassifier(unittest.TestCase):
    def setUp(self):
        # Create a simple dataset for testing
        self.X_train = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.y_train = [0, 1, 0]
        
        # Initialize the model
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(self.X_train, self.y_train)
        
    def test_prediction(self):
        # Test model predictions on a known dataset
        X_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_predictions = [0, 1, 0]
        
        predictions = self.model.predict(X_test)
        
        self.assertEqual(predictions, expected_predictions)
        
    def test_accuracy(self):
        # Test the accuracy of the model on a known dataset
        X_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y_test = [0, 1, 0]
        
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        self.assertAlmostEqual(accuracy, 1.0, places=2)

if __name__ == '__main__':
    unittest.main()
