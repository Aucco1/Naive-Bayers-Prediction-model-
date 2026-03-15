import streamlit as st
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


st.title(" Student Attendance Predictor")
st.write("Using a Naive Bayes algorithm to predict class attendance based on environmental factors.")

df = pd.read_csv('CompleteCombinationFactors.csv')

encoder = OrdinalEncoder()
X = encoder.fit_transform(df.drop('Outcome', axis=1))
y = df['Outcome']

model = CategoricalNB(alpha=1)
model.fit(X, y)


accuracy = model.score(X, y)
st.sidebar.title("Model Stats")
st.sidebar.metric(label="Training Accuracy", value=f"{accuracy * 100:.1f}%")
st.sidebar.info("Model trained on classmate survey data.")


st.subheader("Enter Conditions:")


col1, col2 = st.columns(2)

with col1:
   
    w = st.selectbox("Weather", df['Weather'].unique())
    h = st.selectbox("Health", df['Health'].unique())
    a = st.selectbox("Academic Load", df['Academic Load'].unique())

with col2:
    m = st.selectbox("Motivation", df['Motivation'].unique())
    l = st.selectbox("Location", df['Location'].unique())

st.write("---") 


if st.button("Predict Attendance"):
    
    test_data = pd.DataFrame([[w, h, a, m, l]], columns=df.columns[:-1])
    
    try:
        encoded_test = encoder.transform(test_data)
        prediction = model.predict(encoded_test)
        
        
        if prediction[0].upper() == "ABSENT":
            st.error("PREDICTION: The student will be ABSENT.")
        else:
            st.success("PREDICTION: The student will be PRESENT.")
            
    except Exception as e:
        st.error(f"Error: {e}")