import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Create Streamlit app
st.title('Iris Flower Prediction App')

st.write("""
Enter the measurements of the iris flower features (in cm) and predict the iris species.
""")

# Input sliders
sepal_length = st.slider('Sepal Length', min_value=4.0, max_value=8.0, value=5.0, step=0.1)
sepal_width = st.slider('Sepal Width', min_value=2.0, max_value=5.0, value=3.0, step=0.1)
petal_length = st.slider('Petal Length', min_value=1.0, max_value=7.0, value=1.5, step=0.1)
petal_width = st.slider('Petal Width', min_value=0.1, max_value=2.5, value=0.2, step=0.1)

# 'Predict' button
if st.button('Predict'):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)

    st.write('The predicted iris species is ', iris.target_names[prediction][0])