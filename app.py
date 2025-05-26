{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6cbd59d0-0991-4f4c-adf7-90e72f96fb70",
   "metadata": {},
   "outputs": [],
   "source": [
    "app_code = '''\n",
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
   "execution_count": 4,
   "id": "3b9168ab-56d1-4ce5-be53-47db007d34ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"app.py\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(app_code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00eb134c-f279-42c5-8288-eb951432c6ad",
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
