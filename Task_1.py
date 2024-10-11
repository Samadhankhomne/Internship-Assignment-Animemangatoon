import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


data = {
    'description': [
        "A heartwarming story of first love and teenage romance.",
        "A young hero battles dark forces in an action-packed adventure.",
        "A mysterious fantasy world filled with dragons and magic.",
        "High school drama with love triangles and emotional twists.",
        "A sci-fi tale where robots rise against humanity.",
        "A historical romance where two lovers are torn apart by war.",
        "An intense action series following a group of elite assassins.",
        "A lighthearted fantasy about an ordinary girl in a magical realm.",
        "A gripping action series with martial arts and crime fighting.",
        "A romantic comedy where two opposites attract in college."
    ],
    'category': [
        'romance', 'action', 'fantasy', 'romance', 'sci-fi', 
        'romance', 'action', 'fantasy', 'action', 'romance'
    ]
}

#Convert dataset to DataFrame
df = pd.DataFrame(data)

#  Convert text to numerical features using TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['description'])

#  Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.2, random_state=0)

# Train a Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#  Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#  Predict a new description
new_description = ["An epic fantasy adventure where heroes battle to save the world."]
new_description_vec = vectorizer.transform(new_description)
predicted_category = model.predict(new_description_vec)
print("\nPredicted Category for new description:", predicted_category[0])

