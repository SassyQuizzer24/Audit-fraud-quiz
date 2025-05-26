{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c387e63d-37d4-40f9-8e47-3463371fe7d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "code = '''\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load question data\n",
    "df = pd.read_csv(\"questions.csv\")\n",
    "\n",
    "st.set_page_config(page_title=\"Audit Fraud MCQ Game\", layout=\"wide\")\n",
    "st.title(\"🕵️ Audit Fraud MCQ Game\")\n",
    "st.markdown(\"Select a fraud case and answer the questions below:\")\n",
    "\n",
    "# Sidebar for user info and case selection\n",
    "name = st.sidebar.text_input(\"Enter your name (optional)\")\n",
    "selected_case = st.sidebar.selectbox(\"Choose a Case\", sorted(df['case'].unique()))\n",
    "\n",
    "# Filter questions\n",
    "case_df = df[df['case'] == selected_case].reset_index(drop=True)\n",
    "\n",
    "# Store answers\n",
    "user_answers = {}\n",
    "score = 0\n",
    "\n",
    "st.markdown(f\"### 📚 Case: {selected_case}\")\n",
    "\n",
    "# Show all questions\n",
    "for i, row in case_df.iterrows():\n",
    "    st.markdown(f\"**Q{i+1}. {row['question']}**\")\n",
    "    options = {\n",
    "        \"a\": row['option_a'],\n",
    "        \"b\": row['option_b'],\n",
    "        \"c\": row['option_c'],\n",
    "        \"d\": row['option_d'],\n",
    "    }\n",
    "    user_choice = st.radio(\n",
    "        label=\"\",\n",
    "        options=list(options.keys()),\n",
    "        format_func=lambda x: f\"{x}) {options[x]}\",\n",
    "        key=f\"q{i}\"\n",
    "    )\n",
    "    user_answers[i] = user_choice\n",
    "\n",
    "# Submit button\n",
    "if st.button(\"✅ Submit\"):\n",
    "    for i, row in case_df.iterrows():\n",
    "        if user_answers.get(i) == row[\"answer\"]:\n",
    "            score += 1\n",
    "    st.success(f\"🎉 {name if name else 'You'} scored {score} out of {len(case_df)}!\")\n",
    "    if score == len(case_df):\n",
    "        st.balloons()\n",
    "    st.markdown(\"### ✅ Correct Answers:\")\n",
    "    for i, row in case_df.iterrows():\n",
    "        st.markdown(f\"**Q{i+1}. {row['question']}**\")\n",
    "        st.markdown(f\"✔️ Correct: **{row['answer']}) {row[f'option_{row['answer']}']}**\")\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3956b039-d59b-40a3-a6ec-e195706523e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"app.py\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56d15b1f-23f8-4bdd-8398-d83d20d7ef2f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
