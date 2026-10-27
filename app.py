import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Performance Analysis")

df = pd.read_csv("StudentPerformanceFactors.csv")
st.write("Dataset Preview", df.head())

# Example chart - factors vs exam score
st.subheader("Average Exam Score by Parental Education")
avg_score = df.groupby("Parental_Education_Level")["Exam_Score"].mean()
st.bar_chart(avg_score)

# Download report button
st.subheader("Download Summary")
st.write(df.describe())