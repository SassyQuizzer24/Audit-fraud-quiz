
import streamlit as st
import pandas as pd

# Load question data
df = pd.read_csv("questions.csv")

st.set_page_config(page_title="Audit Fraud MCQ Game", layout="wide")
st.title("🕵️ Audit Fraud MCQ Game")
st.markdown("Select a fraud case and answer the questions below:")

# Sidebar for user info and case selection
name = st.sidebar.text_input("Enter your name (optional)")
selected_case = st.sidebar.selectbox("Choose a Case", sorted(df['case'].unique()))

# Filter questions
case_df = df[df['case'] == selected_case].reset_index(drop=True)

# Store answers
user_answers = {}
score = 0

st.markdown(f"### 📚 Case: {selected_case}")

# Display questions
for i, row in case_df.iterrows():
    st.markdown(f"**Q{i+1}. {row['question']}**")
    options = {
        "a": row['option_a'],
        "b": row['option_b'],
        "c": row['option_c'],
        "d": row['option_d'],
    }
    user_choice = st.radio(
        label="",
        options=list(options.keys()),
        format_func=lambda x: f"{x}) {options[x]}",
        key=f"q{i}"
    )
    user_answers[i] = user_choice

# Submit button
if st.button("✅ Submit"):
    for i, row in case_df.iterrows():
        if user_answers.get(i) == row["answer"]:
            score += 1

    st.success(f"🎉 {name if name else 'You'} scored {score} out of {len(case_df)}!")
    if score == len(case_df):
        st.balloons()

    st.markdown("### ✅ Correct Answers:")
    for i, row in case_df.iterrows():
        st.markdown(f"**Q{i+1}. {row['question']}**")
        st.markdown(f"✔️ Correct: **{row['answer']}) {row[f'option_{row['answer']}']}**")

    st.markdown("---")
    st.markdown("### ✉️ Submit your score to Madhu")
    st.markdown("Click below to fill the Google Form and notify Madhu.")
    st.link_button("📨 Open Google Form", "https://docs.google.com/forms/d/e/1FAIpQLSebeYndLmPRU9557xtOa4UuJ83xIC6SpOXXpu5qcd8nUlGIig/viewform?usp=dialog")
